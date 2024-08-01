#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess
from collections import defaultdict
from tqdm import tqdm
# from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from .utils import (
    # open_file_reader,
    # open_file_writer,
    # read_pickle, 
    # write_pickle,
    # read_json,
    # write_json,
    # build_logger,
    # reset_logger,
    # get_timestamp,
    # format_duration,
    # format_header,
    format_bytes,
    get_file_size,
    profile_peak_memory,
    RunShellCommand,
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


    
    

    
