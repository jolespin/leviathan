#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess, glob
from collections import defaultdict
import pandas as pd
# from pandas.errors import EmptyDataError
# from Bio.SeqIO.FastaIO import SimpleFastaParser
from tqdm import tqdm
# from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from pyexeggutor import (
    # open_file_reader,
    # open_file_writer,
    read_pickle, 
    # write_pickle,
    read_json,
    # write_json,
    build_logger,
    # reset_logger,
    # format_duration,
    # format_header,
    get_file_size,
    format_bytes,
    # get_directory_tree,
    # get_directory_size,
    # get_md5hash_from_directory,
    RunShellCommand,
)

from leviathan.profile_taxonomy import(
    check_genome_database,
    check_reads_format,
    run_sylph_reads_sketcher,
    run_sylph_profiler,
)

def main(args=None):
    # Options
    # =======
    # Path info
    python_executable = sys.executable
    bin_directory = "/".join(python_executable.split("/")[:-1])
    script_directory  =  os.path.dirname(os.path.abspath( __file__ ))
    script_filename = __program__
    description = """
    Running: {} v{} via Python v{} | {}""".format(__program__, sys.version.split(" ")[0], python_executable, script_filename)
    usage = f"{__program__} -1 forward.fq[.gz] -2 reverse.fq[.gz] -n sample_name -o project_directory --index_directory path/to/leviathan_index/"
    epilog = "Copyright 2024 New Atlantis Labs (jolespin@newatlantis.io)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # Pipeline
    parser_io = parser.add_argument_group('I/O arguments')
    parser_io.add_argument("-1","--forward_reads", type=str,  help = "path/to/forward_reads.fq[.gz] (Cannot be used with -s/--read_sketch)")
    parser_io.add_argument("-2","--reverse_reads", type=str,  help = "path/to/reverse_reads.fq[.gz] (Cannot be used with -s/--read_sketch)")
    parser_io.add_argument("-s","--reads_sketch", type=str, help = "path/to/reads_sketch.sylsp (e.g., sylph sketch output) (Cannot be used with -1/--forward_reads and -2/--reverse_reads)")
    parser_io.add_argument("-n", "--name", type=str, required=True, help="Name of sample")
    parser_io.add_argument("-o","--project_directory", type=str, default="leviathan_output/profiling/taxonomy", help = "path/to/project_directory (e.g., leviathan_output/profiling/taxonomy]")
    parser_io.add_argument("-d","--index_directory", type=str, required=True, help = "path/to/index_directory/")
    parser_io.add_argument("-f","--output_format", type=str, choices={"tsv", "parquet"}, default="parquet", help = "Output format [Default: parquet]")

    # Utilities
    parser_utility = parser.add_argument_group('Utility arguments')
    parser_utility.add_argument("-p","--n_jobs", type=int, default=1,  help = "Number of threads to use.  Use -1 for all available. [Default: 1]")

    # Sylph
    parser_sylph_sketch = parser.add_argument_group('Sylph reads sketcher arguments (Fastq)')
    parser_sylph_sketch.add_argument("--sylph_executable", type=str, help="Sylph executable [Default: $PATH]")
    parser_sylph_sketch.add_argument("--sylph_k", type=int, choices={21,31}, default=31,  help="Sylph |  Value of k. Only k = 21, 31 are currently supported. [Default: 31]")
    parser_sylph_sketch.add_argument("--sylph_minimum_spacing", type=int,  default=30,  help="Sylph |  Minimum spacing between selected k-mers on the genomes [Default: 30]")
    parser_sylph_sketch.add_argument("--sylph_subsampling_rate", type=int, default=200,  help="Sylph | Subsampling rate.	[Default: 200]")
    parser_sylph_sketch.add_argument("--sylph_sketch_options", type=str, default="", help="Sylph | More options for `sylph sketch` (e.g. --arg=1 ) [Default: '']")

    parser_sylph_profile = parser.add_argument_group('Sylph profile arguments')
    parser_sylph_profile.add_argument("--sylph_profile_minimum_ani", type=float, default=95, help="Sylph profile | Minimum adjusted ANI to consider (0-100). [Default: 95]")
    parser_sylph_profile.add_argument("--sylph_profile_minimum_number_kmers", type=int, default=20, help="Sylph profile | Exclude genomes with less than this number of sampled k-mers.  Default is 50 in Sylph but lowering to 20 accounts for viruses and small CPR genomes. [Default: 20]")
    parser_sylph_profile.add_argument("--sylph_profile_minimum_count_correct", type=int, default=3, help="Sylph profile | Minimum k-mer multiplicity needed for coverage correction. Higher values gives more precision but lower sensitivity [Default: 3]")
    parser_sylph_profile.add_argument("--sylph_profile_options", type=str, default="", help="Sylph profile | More options for `sylph profile` (e.g. --arg 1 ) [Default: '']")


    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan profile-taxonomy")

    # Commands
    logger.info(f"Command: {sys.argv}")

    # Threads
    if opts.n_jobs == -1:
        from multiprocessing import cpu_count 
        opts.n_jobs = cpu_count()
        logger.info(f"Setting --n_jobs to maximum threads {opts.n_jobs}")

    assert opts.n_jobs >= 1, "--n_jobs must be ≥ 1.  To select all available threads, use -1."
    
    # Executables
    # * Sylph
    if not opts.sylph_executable:
        opts.sylph_executable = os.path.join(bin_directory, "sylph")
    if not os.path.exists(opts.sylph_executable):
        msg = f"sylph executable not doesn't exist: {opts.sylph_executable}"
        logger.critical(msg)
        raise FileNotFoundError(msg)
    
    # Config
    config = read_json(os.path.join(opts.index_directory, "config.json"))

    # Determine input reads format
    input_reads_format = check_reads_format(
        forward_reads=opts.forward_reads, 
        reverse_reads=opts.reverse_reads, 
        reads_sketch=opts.reads_sketch,
        logger=logger,
        )

    # Check Sylph database
    check_genome_database(
        index_directory=opts.index_directory, 
        logger=logger,
        )
    
    # Output
    output_directory = os.path.join(opts.project_directory, opts.name)
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(os.path.join(output_directory, "output"), exist_ok=True)
    os.makedirs(os.path.join(output_directory, "intermediate"), exist_ok=True)
    os.makedirs(os.path.join(output_directory, "logs"), exist_ok=True)
    os.makedirs(os.path.join(output_directory, "tmp"), exist_ok=True)

    if input_reads_format == "paired":
        # Process and check inputs
        logger.info("Sketching reads")

        # ==========================
        # Build Sylph reads sketcher
        # ==========================
        cmd_sylph_reads_sketcher = run_sylph_reads_sketcher(
                        logger=logger,
                        log_directory=os.path.join(output_directory, "logs"), 
                        sylph_executable=opts.sylph_executable, 
                        n_jobs=opts.n_jobs, 
                        output_directory=os.path.join(output_directory, "intermediate"), 
                        forward_reads=opts.forward_reads, 
                        reverse_reads=opts.reverse_reads,
                        k=opts.sylph_k, 
                        minimum_spacing=opts.sylph_minimum_spacing, 
                        subsampling_rate=opts.sylph_subsampling_rate, 
                        sylph_sketch_options=opts.sylph_sketch_options, 

        )
        opts.reads_sketch = os.path.join(output_directory, "intermediate", "reads.sylsp")
        logger.info(f"Setting --reads_sketch to {opts.reads_sketch}")
    else:
        logger.info(f"Skipping read sketching and using {opts.reads_sketch}")
        if opts.reads_sketch is None:
            raise ValueError("Please either provide -1/-2 paired reads or -s/--reads_sketch")

        
    # ====================
    # Build Sylph profiler
    # ====================
    # Run Sylph
    logger.info("Running Sylph profiler")
    cmd_sylph_profiler = run_sylph_profiler(
        logger=logger,
        log_directory=os.path.join(output_directory, "logs"), 
        sylph_executable=opts.sylph_executable, 
        n_jobs=opts.n_jobs, 
        output_directory=os.path.join(output_directory, "output"), 
        index_directory=opts.index_directory,
        reads=opts.reads_sketch, 
        minimum_ani=opts.sylph_profile_minimum_ani, 
        minimum_number_kmers=opts.sylph_profile_minimum_number_kmers, 
        minimum_count_correct=opts.sylph_profile_minimum_count_correct, 
        sylph_profile_options=opts.sylph_profile_options, 
    )

    # =======================
    # Process genome metadata
    # =======================
    logger.info("Processing genome metadata")
    
    genomefilepath_to_genomeid = dict()
    genome_to_genomecluster = dict()
    
    genome_to_data = read_pickle(os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz"))
    for id_genome, data in tqdm(genome_to_data.items(), "Getting filepaths associated with genomes"):
        filepath = data["filepath"] 
        genomefilepath_to_genomeid[filepath] = id_genome
        genome_to_genomecluster[id_genome] = data["id_genome_cluster"]
    del genome_to_data
       
    # ===================================
    # Reformat taxonomic abundance tables
    # ===================================
    genome_abundance_filepath = os.path.join(output_directory, "output", f"taxonomic_abundance.genomes.{opts.output_format}")
    if not opts.output_format != "parquet":
        genome_abundance_filepath += ".gz"

    
    logger.info(f"Reformatting taxonomic abundance: {genome_abundance_filepath}")
    df_sylph = pd.read_csv(os.path.join(output_directory, "output", "sylph_profile.tsv.gz"), sep="\t", index_col=0)
    genome_to_abundance = df_sylph.reset_index().set_index("Genome_file")["Taxonomic_abundance"]
    genome_to_abundance.index = genome_to_abundance.index.map(lambda filepath:genomefilepath_to_genomeid[filepath])
    genome_to_abundance.index.name = "id_genome"
    genome_to_abundance = genome_to_abundance.to_frame("abundance")
    if opts.output_format == "parquet":
        genome_to_abundance.to_parquet(genome_abundance_filepath, index=True)
    elif opts.output_format == "tsv":
        genome_to_abundance.to_csv(genome_abundance_filepath, sep="\t")
    
    if config["contains_genome_cluster_mapping"]:
        genomecluster_abundance_filepath = os.path.join(output_directory, "output", f"taxonomic_abundance.genome_clusters.{opts.output_format}")
        if not opts.output_format != "parquet":
            genomecluster_abundance_filepath += ".gz"
        logger.info(f"Aggregating taxonomic abundance for genome clusters: {genomecluster_abundance_filepath}")
        genomecluster_to_abundance = genome_to_abundance["abundance"].groupby(genome_to_genomecluster).sum()
        genomecluster_to_abundance.index.name = "id_genome_cluster"
        genomecluster_to_abundance = genomecluster_to_abundance.to_frame("abundance")
        if opts.output_format == "parquet":
            genomecluster_to_abundance.to_parquet(genomecluster_abundance_filepath, index=True)
        elif opts.output_format == "tsv":
            genomecluster_to_abundance.to_csv(genomecluster_abundance_filepath, sep="\t")

    # ===================================
    # Reformat sequence abundance tables
    # ===================================
    genome_abundance_filepath = os.path.join(output_directory, "output", f"sequence_abundance.genomes.{opts.output_format}")
    if not opts.output_format != "parquet":
        genome_abundance_filepath += ".gz"

    
    logger.info(f"Reformatting sequence abundance: {genome_abundance_filepath}")
    df_sylph = pd.read_csv(os.path.join(output_directory, "output", "sylph_profile.tsv.gz"), sep="\t", index_col=0)
    genome_to_abundance = df_sylph.reset_index().set_index("Genome_file")["Sequence_abundance"]
    genome_to_abundance.index = genome_to_abundance.index.map(lambda filepath:genomefilepath_to_genomeid[filepath])
    genome_to_abundance.index.name = "id_genome"
    genome_to_abundance = genome_to_abundance.to_frame("abundance")
    if opts.output_format == "parquet":
        genome_to_abundance.to_parquet(genome_abundance_filepath, index=True)
    elif opts.output_format == "tsv":
        genome_to_abundance.to_csv(genome_abundance_filepath, sep="\t")
    
    if config["contains_genome_cluster_mapping"]:
        genomecluster_abundance_filepath = os.path.join(output_directory, "output", f"sequence_abundance.genome_clusters.{opts.output_format}")
        if not opts.output_format != "parquet":
            genomecluster_abundance_filepath += ".gz"
        logger.info(f"Aggregating sequence abundance for genome clusters: {genomecluster_abundance_filepath}")
        genomecluster_to_abundance = genome_to_abundance["abundance"].groupby(genome_to_genomecluster).sum()
        genomecluster_to_abundance.index.name = "id_genome_cluster"
        genomecluster_to_abundance = genomecluster_to_abundance.to_frame("abundance")
        if opts.output_format == "parquet":
            genomecluster_to_abundance.to_parquet(genomecluster_abundance_filepath, index=True)
        elif opts.output_format == "tsv":
            genomecluster_to_abundance.to_csv(genomecluster_abundance_filepath, sep="\t")
            
    # ========
    # Complete
    # ========    
    logger.info(f"Completed taxonomic profiling: {opts.name}")
    for filepath in glob.glob(os.path.join(output_directory, "output","*")):
        filesize = get_file_size(filepath, format=True)
        logger.info(f"Output: {filepath} ({filesize})")

if __name__ == "__main__":
    main()