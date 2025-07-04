#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess, shutil
from collections import defaultdict
from importlib.resources import files as resource_files
# from pandas.errors import EmptyDataError
# from Bio.SeqIO.FastaIO import SimpleFastaParser
from tqdm import tqdm
# from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from pyexeggutor import (
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
    format_bytes,
    get_timestamp,
    get_directory_tree,
    get_directory_size,
    get_md5hash_from_directory,
    RunShellCommand,
)

from leviathan.index import(
    process_genomic_databases_and_check_inputs,
    update_genome_database_with_fasta_filepaths_and_check_inputs,
    load_pathway_database_and_check_inputs,
    check_salmon_index,
    run_salmon_indexer,
    run_sylph_genomes_sketcher,
    run_kegg_pathway_downloader,
)

DEFAULT_PATHWAY_DATABASE = str(resource_files('kegg_pathway_profiler').joinpath('data/database.pkl.gz'))
if not os.path.exists(DEFAULT_PATHWAY_DATABASE):
    DEFAULT_PATHWAY_DATABASE = None

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
    parser_io.add_argument("-d","--index_directory", type=str, required=True, help = "path/to/index_directory/ (Recommended: leviathan_output/index/ if this will only be used for one project or a centralized location if it will be used for multiple projects)")
    parser_io.add_argument("-u", "--update_with_genomes", action="store_true",  help = "Update databases with genomes for Sylph sketches")

    # Utilities
    parser_utility = parser.add_argument_group('Utility arguments')
    parser_utility.add_argument("-p","--n_jobs", type=int, default=1,  help = "Number of threads to use.  Use -1 for all available. [Default: 1]")
    parser_utility.add_argument("--no_check", action="store_true",  help = "Don't check to ensure --genomes set equals --feature_mapping genome set")

    # Salmon
    parser_salmon_index = parser.add_argument_group('salmon index arguments')
    parser_salmon_index.add_argument("--salmon_executable", type=str, help="salmon executable [Default: $PATH]")
    parser_salmon_index.add_argument("--salmon_index_options", type=str, default="", help="salmon index | More options (e.g. --arg=1 ) https://salmon.readthedocs.io/en/latest/ [Default: '']")

    # Sylph
    parser_sylph_sketch = parser.add_argument_group('Sylph genomes sketcher arguments (Fastq)')
    parser_sylph_sketch.add_argument("--sylph_executable", type=str, help="Sylph executable [Default: $PATH]")
    parser_sylph_sketch.add_argument("--sylph_k", type=int, choices={21,31}, default=31,  help="Sylph |  Value of k. Only k = 21, 31 are currently supported. [Default: 31]")
    parser_sylph_sketch.add_argument("--sylph_minimum_spacing", type=int,  default=30,  help="Sylph |  Minimum spacing between selected k-mers on the genomes [Default: 30]")
    parser_sylph_sketch.add_argument("--sylph_subsampling_rate", type=int, default=200,  help="Sylph | Subsampling rate.	[Default: 200]")
    parser_sylph_sketch.add_argument("--sylph_sketch_options", type=str, default="", help="Sylph | More options for `sylph sketch` (e.g. --arg=1 ) [Default: '']")

    # Pathway
    parser_pathways = parser.add_argument_group('Pathway database arguments')
    parser_pathways.add_argument("--pathway_database_downloader_executable", type=str, help="KEGG Pathway profiler `build-pathway-database.py` executable. Ignored if --database is provided. [Default: $PATH]")
    parser_pathways.add_argument("--no_intermediate_files", action="store_true",  help = "Don't write intermediate files when downloading database")
    parser_pathways.add_argument("--pathway_database", type=str, default=DEFAULT_PATHWAY_DATABASE, help=f"Pathway database formatted as a Python pkl[.gz].  See documentation for details.  If no database is provided, then a database will be generated if KEGG orthologs are provided as features. [Default: {DEFAULT_PATHWAY_DATABASE}]")

    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan index")

    # Commands
    logger.info(f"Command: {sys.argv}")

    # Checks
    if not opts.no_check:
        genomes_with_filepaths = set()
        with open_file_reader(opts.genomes) as f:
            for line in f:
                line = line.strip()
                if line:
                    id_genome, filepath = line.split("\t")
                    genomes_with_filepaths.add(id_genome)

        genomes_with_features = set()
        with open_file_reader(opts.feature_mapping) as f:
            for line in f:
                line = line.strip()
                if line:
                    fields = line.split("\t")
                    id_genome = fields[2]
                    genomes_with_features.add(id_genome)
        if genomes_with_filepaths == genomes_with_features:
            msg = "All genomes in --genomes are in --feature_mapping"
            logger.info(msg)
        else:
            msg = f"{len(genomes_with_filepaths) - len(genomes_with_features)} genomes in --genomes are missing from --feature_mapping"
            logger.critical(msg)
            parser.error(msg)
     
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
        logger.info(f"Setting --n_jobs to maximum threads {opts.n_jobs}")

    assert opts.n_jobs >= 1, "--n_jobs must be ≥ 1.  To select all available threads, use -1."
    
    # Executables
    # * Salmon
    if not opts.salmon_executable:
        opts.salmon_executable = os.path.join(bin_directory, "salmon")
    if not os.path.exists(opts.salmon_executable):
        msg = f"salmon executable doesn't exist: {opts.salmon_executable}"
        logger.critical(msg)
        raise FileNotFoundError(msg)
    
    # * Sylph
    if not opts.sylph_executable:
        opts.sylph_executable = os.path.join(bin_directory, "sylph")
    if not os.path.exists(opts.sylph_executable):
        msg = f"sylph executable doesn't exist: {opts.sylph_executable}"
        logger.critical(msg)
        raise FileNotFoundError(msg)
    
    # * KEGG Pathway Profiler
    if opts.pathway_database:
        logger.info(f"Database provided: {opts.pathway_database}")
        if opts.pathway_database_downloader_executable:
            logger.info(f"Ignoring --pathway_database_downloader_executable {opts.pathway_database_downloader_executable}")
    else:
        if not opts.pathway_database_downloader_executable:
            opts.pathway_database_downloader_executable = os.path.join(bin_directory, "build-pathway-database.py")
        if not os.path.exists(opts.pathway_database_downloader_executable):
            msg = f"KEGG Pathway Profiler's `build-pathway-database.py` executable doesn't exist: {opts.pathway_database_downloader_executable}. Please install or provide a custom database."
            logger.critical(msg)
            raise FileNotFoundError(msg)
    
    # Index directory
    if all([
        os.path.exists(opts.index_directory),
        not opts.update_with_genomes,
        ]):
        msg = f"--index_directory {opts.index_directory} already exists.  If you want to update with genomes, please use --update_with_genomes or remove directory to overwrite"
        logger.critical(msg)
        raise FileExistsError(msg)
    
    os.makedirs(os.path.join(opts.index_directory, "database"), exist_ok=True)
    os.makedirs(os.path.join(opts.index_directory, "logs"), exist_ok=True)
    os.makedirs(os.path.join(opts.index_directory, "tmp"), exist_ok=True)

    if not opts.update_with_genomes:
        # Setup config
        logger.info("Setting up config")

        config = dict(
            fasta_filepath=opts.fasta,
            feature_mapping_filepath=opts.feature_mapping,
            contains_genome_cluster_mapping=False,
            contains_genome_filepaths=False,
            timestamp=get_timestamp(),
        )
        # Genomes and genes database
        # --------------------------
        # Process genomes/genes and check inputs
        logger.info("Processing and checking input files")
        
        config, gene_to_data, genome_to_data = process_genomic_databases_and_check_inputs(
            fasta=opts.fasta, 
            feature_mapping=opts.feature_mapping, 
            genomes=opts.genomes,
            logger=logger,
            config=config,
            )
        
        # Pathway database
        # ----------------
        # Fetch database
        config["contains_pathways"] = False
        if opts.pathway_database:
            logger.info(f"Pathway database provided and copying to index: {opts.pathway_database}")
            shutil.copy(opts.pathway_database, os.path.join(opts.index_directory, "database", "pathway_to_data.pkl.gz"), follow_symlinks=True)
            config["contains_pathways"] = True
        else:
            if config["feature_type_is_kegg_ortholog"]:
                # Run KEGG Pathway Downloader
                logger.info("Running KEGG Pathway downloader")
                cmd_kegg_pathway_downloader = run_kegg_pathway_downloader(
                    logger=logger,
                    log_directory = os.path.join(opts.index_directory, "logs"),
                    pathway_database_downloader_executable=opts.pathway_database_downloader_executable,
                    index_directory=opts.index_directory,
                    no_intermediate_files=bool(opts.no_intermediate_files),
                    )
                config["contains_pathways"] = True
            else:
                logger.warning("No pathway database was provided and features were not determined to be KEGG orthologs so automatic database compilation is not available.  Pathway profiling will not include pathway coverage or abundances.")

        # Check pathway database
        if config["contains_pathways"]:
            config, pathway_to_data = load_pathway_database_and_check_inputs(
                index_directory=opts.index_directory, 
                gene_to_data=gene_to_data, 
                logger=logger, 
                config=config,
                )

        # Write database files
        logger.info("Writing config and database files")
        write_json(config, os.path.join(opts.index_directory,  "config.json"))
        write_pickle(gene_to_data, os.path.join(opts.index_directory, "database", "gene_to_data.pkl.gz"))
        write_pickle(genome_to_data, os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz"))

        # ==================
        # Build Salmon Index
        # ==================
        cmd_salmon_indexer = run_salmon_indexer(
                        logger=logger,
                        log_directory = os.path.join(opts.index_directory, "logs"),
                        salmon_executable=opts.salmon_executable,
                        n_jobs=opts.n_jobs,
                        fasta=opts.fasta,
                        index_directory=opts.index_directory,
                        index_options=opts.salmon_index_options,
        )
        
    else:
        # Load config
        config_filepath = os.path.join(opts.index_directory, "config.json")
        logger.info(f"Loading config: {config_filepath}")
        config = read_json(config_filepath)

        # Process and check inputs
        logger.info("Loading previously built database and checking genomes for database update")
        config, gene_to_data, genome_to_data = update_genome_database_with_fasta_filepaths_and_check_inputs(
            index_directory=opts.index_directory, 
            genomes=opts.genomes,
            logger=logger,
            config=config,
            )
        
        # Update database files
        genome_to_data_filepath = os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz")
        logger.info(f"Rewriting config and database files: {genome_to_data_filepath}")
        write_json(config, config_filepath)
        write_pickle(genome_to_data, genome_to_data_filepath)
        

    # ==================
    # Build Sylph Sketch
    # ==================
    if config["contains_genome_filepaths"]:
        logger.info("Writing genome filepaths for Sylph")

        # Write filepaths
        genome_filepaths = os.path.join(opts.index_directory, "tmp", "genome_filepaths.list")
        with open_file_writer(genome_filepaths) as f:
            for id_genome, data in tqdm(genome_to_data.items(), f"Writing filepaths: {genome_filepaths}"):
                print(data["filepath"], file=f)
                
        # Run Sylph
        logger.info("Running Sylph genome sketcher")
        cmd_sylph_genomes_sketcher = run_sylph_genomes_sketcher(
            logger=logger,
            log_directory = os.path.join(opts.index_directory, "logs"),
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
        
    # ========
    # Hash
    # ========   
    md5hash_filepath = os.path.join(opts.index_directory, "md5hashes.json")
    logger.info(f"Calculating md5 hashes: {md5hash_filepath}")
    file_to_hash = get_md5hash_from_directory(opts.index_directory)
    write_json(file_to_hash, md5hash_filepath)

    # ========
    # Complete
    # ========    
    logger.info(f"Completed building leviathan index: {opts.index_directory}")
    logger.info(f"Directory size of leviathan index: {format_bytes(get_directory_size(opts.index_directory))}")
    logger.info(f"Directory structure of leviathan index:\n{get_directory_tree(opts.index_directory, ascii=True)}")
    logger.info(f"Finished running leviathan-index:{opts.index_directory}")

if __name__ == "__main__":
    main()
    
    

    
