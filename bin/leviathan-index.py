#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess
from collections import defaultdict
from pandas.errors import EmptyDataError
from Bio.SeqIO.FastaIO import SimpleFastaParser
from tqdm import tqdm
from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from leviathan.utils import (
    open_file_reader,
    open_file_writer,
    read_pickle, 
    write_pickle,
    read_json,
    write_json,
    build_logger,
    reset_logger,
    format_duration,
    format_header,
    format_memory,
    RunShellCommand,
)

from leviathan.index import(
    process_and_check_inputs,
    load_database_and_check_inputs,
    check_salmon_index,
    run_salmon_indexer,
    run_sylph_sketcher,
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
    usage = f"{__program__} --fasta path/to/cds.fasta --feature_mapping path/to/features.tsv --genomes path/to/genomes.tsv  --index_directory path/to/leviathan_index/"
    epilog = "Copyright 2024 New Atlantis Labs (jolespin@newatlantis.io)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # Pipeline
    parser_io = parser.add_argument_group('I/O arguments')
    parser_io.add_argument("-f","--fasta", type=str,  help = "path/to/cds.fasta") # default="stdin"?
    parser_io.add_argument("-m","--feature_mapping", type=str,  help = "path/to/feature_mapping.tsv [id_gene, feature_set, id_genome, (Optional: id_genome_cluster)] (No header)")
    parser_io.add_argument("-g","--genomes", type=str, help = "path/to/genomes.tsv [id_genome, path/to/genome] (No header)")
    parser_io.add_argument("-o","--index_directory", type=str, required=True, help = "path/to/index_directory/")
    parser_io.add_argument("-u", "--update_with_genomes", action="store_true",  help = "Update databases with genomes for Sylph sketches")

    # Utilities
    parser_utility = parser.add_argument_group('Utility arguments')
    parser_utility.add_argument("-p","--n_jobs", type=int, default=1,  help = "Number of threads to use [Default: 1]")
    # parser_utility.add_argument("-c", "--cleanup", action="store_true",  help = "Remove temporary files")

    # Salmon
    parser_salmon_index = parser.add_argument_group('salmon index arguments')
    parser_salmon_index.add_argument("--salmon_executable", type=str, help="salmon executable [Default: $PATH]")
    parser_salmon_index.add_argument("--salmon_index_options", type=str, default="", help="salmon index| More options (e.g. --arg=1 ) https://salmon.readthedocs.io/en/latest/ [Default: '']")

    # Sylph
    parser_sylph_sketch = parser.add_argument_group('Sylph sketch arguments (Fastq)')
    parser_sylph_sketch.add_argument("--sylph_executable", type=str, help="Sylph executable [Default: $PATH]")
    parser_sylph_sketch.add_argument("--sylph_k", type=int, choices={21,31}, default=31,  help="Sylph |  Value of k. Only k = 21, 31 are currently supported. [Default: 31]")
    parser_sylph_sketch.add_argument("--sylph_minimum_spacing", type=int,  default=30,  help="Sylph |  Minimum spacing between selected k-mers on the genomes [Default: 30]")
    parser_sylph_sketch.add_argument("--sylph_subsampling_rate", type=int, default=200,  help="Sylph | Subsampling rate.	[Default: 200]")
    parser_sylph_sketch.add_argument("--sylph_sketch_options", type=str, default="", help="Sylph | More options for `sylph sketch` (e.g. --arg=1 ) [Default: '']")

    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan index")
     
    # Post-processing argument dependencies
    if opts.update_with_genomes:
        if not opts.genomes:
            msg = "--genomes is required when --update_with_genomes is specified"
            logger.critical(msg)
            parser.error(msg)
        # Check salmon index
        check_salmon_index(os.path.join(opts.index_directory, "salmon_index"))
        
        # Required files without --update_with_genomes
        if not opts.fasta or not opts.feature_mapping:
            msg = "--fasta and --feature_mapping are required when --update_with_genomes is not specified"
            logger.critical(msg)
            parser.error(msg)
        if not opts.genomes:
            logger.warning("--genomes not provided but can incoporated post hoc by rerunning with --update_with_genomes")

    # Threads
    if opts.n_jobs == -1:
        from multiprocessing import cpu_count 
        opts.n_jobs = cpu_count()
    assert opts.n_jobs >= 1, "--n_jobs must be ≥ 1.  To select all available threads, use -1."
    
    # Executables
    # * Salmon
    if not opts.salmon_executable:
        opts.salmon_executable = os.path.join(bin_directory, "salmon")
    if not os.path.exists(opts.salmon_executable):
        msg = f"salmon executable not doesn't exist: {opts.salmon_executable}"
        logger.critical(msg)
        raise FileNotFoundError(msg)
    # * Sylph
    if not opts.sylph_executable:
        opts.sylph_executable = os.path.join(bin_directory, "sylph")
    if not os.path.exists(opts.sylph_executable):
        msg = f"sylph executable not doesn't exist: {opts.sylph_executable}"
        logger.critical(msg)
        raise FileNotFoundError(msg)

    # Index directory
    if all([
        os.path.exists(opts.index_directory),
        not opts.update_with_genomes,
        ]):
        msg = f"--index_directory {opts.index_directory} already exists.  If you want to update with genomes, please use --update_with_genomes or remove directory to overwrite"
        logger.critical(msg)
        raise FileNotFoundError(msg)
    
    os.makedirs(os.path.join(opts.index_directory, "database"), exist_ok=True)
    os.makedirs(os.path.join(opts.index_directory, "logs"), exist_ok=True)
    os.makedirs(os.path.join(opts.index_directory, "tmp"), exist_ok=True)

    if not opts.update_with_genomes:
        # Process and check inputs
        logger.info("Processing and checking input files")

        config, gene_to_data, genome_to_data = process_and_check_inputs(
            fasta=opts.fasta, 
            feature_mapping=opts.feature_mapping, 
            genomes=opts.genomes,
            logger=logger,
            )
        
        # Write database files
        logger.info("Writing config and database files")
        write_json(config, os.path.join(opts.index_directory, "database", "config.json"))
        write_pickle(gene_to_data, os.path.join(opts.index_directory, "database", "gene_to_data.pkl.gz"))
        write_pickle(genome_to_data, os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz"))

        # ==================
        # Build Salmon Index
        # ==================
        logger.info("Running Salmon indexer")
        cmd_salmon_indexer = run_salmon_indexer(
                        salmon_executable=opts.salmon_executable,
                        n_jobs=opts.n_jobs,
                        fasta=opts.fasta,
                        index_directory=opts.index_directory,
                        index_options=opts.salmon_index_options,
        )
    else:
        # Process and check inputs
        logger.info("Loading previously built database and checking genomes for database update")
        config, gene_to_data, genome_to_data = load_database_and_check_inputs(
            index_directory=opts.index_directory, 
            genomes=opts.genomes,
            logger=logger,
            )
        
        # Update database files
        logger.info("Rewriting config and database files")
        write_json(config, os.path.join(opts.index_directory, "database", "config.json"))
        write_pickle(genome_to_data, os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz"))
        
 
    # ==================
    # Build Sylph Sketch
    # ==================
    if config["contains_genome_filepaths"]:
        logger.info("Writing genome filepaths for Sylph")

        # Write filepaths
        genome_filepaths = os.path.join(opts.index_directory, "tmp", "genome_filepaths.list")
        with open_file_writer(genome_filepaths) as f:
            for id_genome, data in tqdm(genome_to_data.items(), f"Writing genome filepaths for Sylph: {genome_filepaths}"):
                print(data["filepath"], file=f)
                
        # Run Sylph
        logger.info("Running Sylph sketcher")
        cmd_sylph_sketcher = run_sylph_sketcher(
            sylph_executable=opts.sylph_executable, 
            n_jobs=opts.n_jobs, 
            genome_filepaths=genome_filepaths, 
            index_directory=opts.index_directory,
            k=opts.sylph_k, 
            minimum_spacing=opts.sylph_minimum_spacing, 
            subsampling_rate=opts.sylph_subsampling_rate, 
            sylph_sketch_options=opts.sylph_sketch_options,
        )

    else:
        logger.warning("--genomes not provided so Leviathan is not building Sylph sketches")
    
if __name__ == "__main__":
    main()
    
    

    
