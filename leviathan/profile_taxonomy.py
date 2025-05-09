#!/usr/bin/env python
import sys
import os
import glob
import pandas as pd
from tqdm import tqdm
# from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from pyexeggutor import (
    format_bytes,
    get_file_size,
    RunShellCommand,
    check_argument_choice,
)

    
def check_reads_format(forward_reads, reverse_reads, reads_sketch, logger):
    input_reads_format = None
    if any([forward_reads, reverse_reads]):
        assert forward_reads != reverse_reads, f"You probably mislabeled the input files because `forward_reads` should not be the same as `reverse_reads`: {forward_reads}"
        assert forward_reads is not None, "If running in --input_reads_format paired mode, --forward_reads and --reverse_reads are needed."
        assert reverse_reads is not None, "If running in --input_reads_format paired mode, --forward_reads and --reverse_reads are needed."
        input_reads_format = "paired"
    if reads_sketch is not None:
        assert forward_reads is None, "If running in --input_reads_format sketch mode, you cannot provide --forward_reads, --reverse_reads"
        assert reverse_reads is None, "If running in --input_reads_format sketch mode, you cannot provide --forward_reads, --reverse_reads"
        input_reads_format = "sketch"
    if input_reads_format is None:
        msg = "Could not determine input reads format.  Please provide either paired fastq or a Sylph sketch."
        logger.critical(msg)
        raise ValueError(msg)
    logger.info(f"Auto-detecting reads format: {input_reads_format}")
    return input_reads_format

def check_genome_database(index_directory, logger):
    # Sylph
    genomes_database_filepath = os.path.join(index_directory, "database", "genomes.syldb")
    if not os.path.exists(genomes_database_filepath):
        msg = f"Could not find the following genomes database: {genomes_database_filepath}. Please ensure you used --genomes when building index with `leviathan index`.  If not, you can update using the --update_with_genomes argument and retry."
        logger.critical(msg)
        raise FileNotFoundError(msg)
    else:
        filesize = get_file_size(genomes_database_filepath, format=True)
        logger.info(f"The following genomes database was found: {genomes_database_filepath} ({filesize})")
        
    # Pickle
    genomes_data_filepath = os.path.join(index_directory, "database", "genome_to_data.pkl.gz")
    if not os.path.exists(genomes_data_filepath):
        msg = f"Could not find the following genomic data: {genomes_data_filepath}. Please ensure you used --genomes when building index with `leviathan index`.  If not, you can update using the --update_with_genomes argument and retry."
        logger.critical(msg)
        raise FileNotFoundError(msg)
    else:
        filesize = get_file_size(genomes_data_filepath, format=True)
        logger.info(f"The following genomes database was found: {genomes_data_filepath} ({filesize})")
    
        
# Run Sylph reads sketcher
def run_sylph_reads_sketcher(logger, log_directory, sylph_executable, n_jobs, output_directory, forward_reads, reverse_reads, k, minimum_spacing, subsampling_rate, sylph_sketch_options):
    forward_reads_filename = os.path.split(forward_reads)[-1]
    cmd = RunShellCommand(
        command=[
            sylph_executable,
            "sketch",
            "-t",
            n_jobs,
            "-k",
            k,
            "-c",
            subsampling_rate,
            "--min-spacing",
            minimum_spacing,
            "-d",
            output_directory,
            "-1",
            forward_reads,
            "-2",
            reverse_reads,
            "&&",
            "mv",
            os.path.join(output_directory, f"{forward_reads_filename}.paired.sylsp"),
            os.path.join(output_directory, "reads.sylsp"),
            
        ],
        name="sylph_reads_sketcher",
        validate_input_filepaths=[
            forward_reads,
            reverse_reads,
        ],
        validate_output_filepaths=[
            forward_reads,
            reverse_reads,
            os.path.join(output_directory, "reads.sylsp"),
        ],
    )
    
    # Run
    logger.info(f"[{cmd.name}] running command: {cmd.command}")
    cmd.run()
    logger.info(f"[{cmd.name}] duration: {cmd.duration_}")
    logger.info(f"[{cmd.name}] peak memory: {format_bytes(cmd.peak_memory_)}")

    # Dump
    logger.info(f"[{cmd.name}] dumping stdout, stderr, and return code: {log_directory}")
    cmd.dump(log_directory)
    
    # Validate
    logger.info(f"[{cmd.name}] checking return code status: {cmd.returncode_}")
    cmd.check_status()
    return cmd

# Run Sylph profile
def run_sylph_profiler(logger, log_directory, sylph_executable, n_jobs, output_directory, index_directory,  reads, minimum_ani, minimum_number_kmers, minimum_count_correct, sylph_profile_options):
    cmd = RunShellCommand(
        command=[
            sylph_executable,
            "profile",
            "--estimate-unknown",
            "-t",
            n_jobs,
            "--minimum-ani",
            minimum_ani,
            "--min-number-kmers",
            minimum_number_kmers,
            "--min-count-correct",
            minimum_count_correct,
            sylph_profile_options,
            os.path.join(index_directory, "database", "genomes.syldb"),
            reads,
            "|",
            "gzip", # pigz?
            ">",
            os.path.join(output_directory, "sylph_profile.tsv.gz"),
        ],
        name="sylph_profiler",
        validate_input_filepaths=[
            os.path.join(index_directory, "database", "genomes.syldb"),
            reads,
        ],
        validate_output_filepaths=[
            os.path.join(output_directory, "sylph_profile.tsv.gz"),
        ]
    )
    
    # Run
    logger.info(f"[{cmd.name}] running command: {cmd.command}")
    cmd.run()
    logger.info(f"[{cmd.name}] duration: {cmd.duration_}")
    logger.info(f"[{cmd.name}] peak memory: {format_bytes(cmd.peak_memory_)}")

    # Dump
    logger.info(f"[{cmd.name}] dumping stdout, stderr, and return code: {log_directory}")
    cmd.dump(log_directory)
    
    # Validate
    logger.info(f"[{cmd.name}] checking return code status: {cmd.returncode_}")
    cmd.check_status()
    return cmd

def merge_taxonomic_profiling_tables_as_pandas(profiling_directory:str, level="genome", fillna_with_zeros:bool=False, sparse:bool=False):
    
    """
    Merge taxonomic profiling at the genome or genome cluster level.

    Parameters
    ----------
    profiling_directory : str
        Directory containing the profiling output.
    level : str, optional
        Level at which to merge the taxonomic profiling. Options are
        "genome" or "genome_cluster". Default is "genome".
    fillna_with_zeros : bool, optional
        Whether to fill missing values with zeros. Default is False.
    sparse : bool, optional
        Whether to return a pd.Sparse type. Default is False.
        
    Returns
    -------
    pd.DataFrame
        Merged taxonomic profiling at the specified level.

    Raises
    ------
    KeyError
        If `level` is not in {"genome", "genome_cluster"}.
    FileNotFoundError
        If no files are found in the specified directory.

    Files:
    * taxonomic_abundance.genome_clusters.parquet
    * taxonomic_abundance.genomes.parquet
    """
    choices = {"genomes", "genome_clusters"}
    if level not in choices:
        raise KeyError(f"level must be in {choices}")
    
    output = dict()

    # Genomes
    if level == "genomes":
        filepaths = glob.glob(f"{profiling_directory}/*/output/taxonomic_abundance.genomes.parquet")
        if filepaths:
            for filepath in tqdm(filepaths, f"Merging {level}-level taxonomic abundances"):
                id_sample = filepath.split("/")[-3]
                output[id_sample] = pd.read_parquet(filepath).squeeze("columns")
        else:
            raise FileNotFoundError(f"Could not find any taxonomic_abundance.genomes.parquet files in {profiling_directory}")
     
    # Genome clusters
    elif level == "genome_clusters":
        filepaths = glob.glob(f"{profiling_directory}/*/output/taxonomic_abundance.genome_clusters.parquet")
        output = dict()
        if filepaths:
            for filepath in tqdm(filepaths, f"Merging {level}-level taxonomic abundances"):
                id_sample = filepath.split("/")[-3]
                # output[id_sample] = pd.read_csv(filepath, sep="\t", index_col=0).squeeze("columns")
                output[id_sample] = pd.read_parquet(filepath).squeeze("columns")

        else:
            raise FileNotFoundError(f"Could not find any taxonomic_abundance.genome_clusters.parquet files in {profiling_directory}")
        
    X = pd.DataFrame(output).T
    missing_value_fill=pd.NA
    if fillna_with_zeros:
        X = X.fillna(0.0)
        missing_value_fill = 0.0
    if sparse:
        X = X.astype(pd.SparseDtype("float", missing_value_fill))
    return X


    
    

    
