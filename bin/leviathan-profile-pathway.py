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
    check_file,
    RunShellCommand,
)
from leviathan.index import(
    check_salmon_index,
)

from leviathan.profile_pathway import(
    run_salmon_quant,
    reformat_gene_abundance,
    reformat_feature_abundance,
    build_wide_feature_prevalence_matrix,
    build_feature_prevalence_dictionary,
    build_feature_pathway_dictionary,
    calculate_pathway_coverage,
    aggregate_pathway_abundance_and_append_coverage,
    aggregate_feature_abundance_for_clusters,
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
    # parser_io.add_argument("--ont", type=str,  help = "path/to/ont_reads.fq[.gz] (Cannot be used with -s/--read_sketch)")

    parser_io.add_argument("-n", "--name", type=str, required=True, help="Name of sample")
    parser_io.add_argument("-o","--project_directory", type=str, default="leviathan_output/profiling/pathway", help = "path/to/project_directory (e.g., leviathan_output/profiling/pathway]")
    parser_io.add_argument("-d","--index_directory", type=str, required=True, help = "path/to/index_directory/")

    # Utilities
    parser_utility = parser.add_argument_group('Utility arguments')
    parser_utility.add_argument("-p","--n_jobs", type=int, default=1,  help = "Number of threads to use.  Use -1 for all available. [Default: 1]")

    # Salmon
    parser_salmon_quant = parser.add_argument_group('salmon quant arguments')
    parser_salmon_quant.add_argument("--salmon_executable", type=str, help="salmon executable [Default: $PATH]")
    parser_salmon_quant.add_argument("-m", "--minimum_score_fraction", type=float, default=0.87, help="The fraction of the optimal possible alignment score that a mapping must achieve in order to be considered \"valid\" --- should be in (0,1]. (relaxed: 0.65, strict: 0.87) [Default: 0.87]")
    parser_salmon_quant.add_argument("--salmon_quant_options", type=str, default="", help="salmon quant| More options (e.g. --arg=1 ) https://salmon.readthedocs.io/en/latest/ [Default: '']")

    # Features
    parser_features = parser.add_argument_group('Features arguments')
    parser_features.add_argument("--no_split_feature_abundances", action="store_true", help="Do not split feature abundances [Default: if one gene is assigned to N enzyme features, then distribute the abundance equally across all N features)")

    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan profile-pathway")

    # Commands
    logger.info(f"Command: {sys.argv}")

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
        msg = f"salmon executable not doesn't exist: {opts.salmon_executable}"
        logger.critical(msg)
        raise FileNotFoundError(msg)
    
    # Config
    config = read_json(os.path.join(opts.index_directory, "config.json"))

    # Check Salmon database
    logger.info("Checking Salmon index") 
    check_salmon_index(
        salmon_index_directory=os.path.join(opts.index_directory, "salmon_index"),
        logger=logger,
        )
    
    # Check gene metadata
    gene_data_filepath = os.path.join(opts.index_directory, "database", "gene_to_data.pkl.gz")
    logger.info(f"Checking gene metadata: {gene_data_filepath}")
    check_file(gene_data_filepath, minimum_filesize=48)
    
    # Check gene metadata
    genome_data_filepath = os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz")
    logger.info(f"Checking genome metadata: {genome_data_filepath}")
    check_file(genome_data_filepath, minimum_filesize=48)
    
    # Check pathway metadata
    if config["contains_pathways"]:
        pathway_data_filepath = os.path.join(opts.index_directory, "database", "pathway_to_data.pkl.gz")
        logger.info(f"Checking pathway metadata: {pathway_data_filepath}")
        check_file(pathway_data_filepath, minimum_filesize=48)
    else:
        logger.warning(f"No pathways available in index: {opts.index_directory}.  Feature-level profiling will be completed but pathway abundances and coverage will not be in output.")

    # Output
    output_directory = os.path.join(opts.project_directory, opts.name)
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(os.path.join(output_directory, "output"), exist_ok=True)
    os.makedirs(os.path.join(output_directory, "intermediate"), exist_ok=True)
    os.makedirs(os.path.join(output_directory, "logs"), exist_ok=True)
    os.makedirs(os.path.join(output_directory, "tmp"), exist_ok=True)
    
    # =====================
    # Loading gene metadata
    # =====================
    logger.info("Loading gene data") 
    gene_to_data = read_pickle(os.path.join(opts.index_directory, "database", "gene_to_data.pkl.gz"))

    # =======================
    # Loading genome metadata
    # =======================
    logger.info("Loading genome data") 
    genome_to_data = read_pickle(os.path.join(opts.index_directory, "database", "genome_to_data.pkl.gz"))

    # =======================
    # Loading pathway metadata
    # =======================
    if config["contains_pathways"]:
        logger.info("Loading pathway data") 
        pathway_to_data = read_pickle(os.path.join(opts.index_directory, "database", "pathway_to_data.pkl.gz"))

    # ====================
    # Build Salmon profiler
    # ====================
    # Run Salmon quant
    logger.info("Running Salmon quant")
    cmd_salmon_quant = run_salmon_quant(
        logger=logger,
        log_directory=os.path.join(output_directory, "logs"), 
        salmon_executable=opts.salmon_executable, 
        n_jobs=opts.n_jobs, 
        output_directory=os.path.join(output_directory, "intermediate"), 
        index_directory=opts.index_directory,
        forward_reads=opts.forward_reads, 
        reverse_reads=opts.reverse_reads, 
        minimum_score_fraction=opts.minimum_score_fraction, 
        salmon_quant_options=opts.salmon_quant_options, 
    )
       
    # ===============================
    # Abundance and prevalence tables
    # ===============================
    level="genome"
    gene_abundance_filepath = os.path.join(output_directory, "output", f"gene_abundances.{level}s.tsv.gz")
    logger.info(f"[level={level}] Reformatting gene abundance: {gene_abundance_filepath}")
    
    df_quant = pd.read_csv(os.path.join(output_directory, "intermediate", "quant.sf"), sep="\t", index_col=0)
    df_gene_abundance = reformat_gene_abundance(df_quant, gene_to_data)
    df_gene_abundance.to_csv(gene_abundance_filepath, sep="\t")
    
    feature_abundance_filepath = os.path.join(output_directory, "output", f"feature_abundances.{level}s.tsv.gz")
    logger.info(f"[level={level}] Calculating feature abundance: {feature_abundance_filepath}")
    df_feature_abundance = reformat_feature_abundance(df_gene_abundance, gene_to_data, split_feature_abundances=not opts.no_split_feature_abundances)
    df_feature_abundance.to_csv(feature_abundance_filepath, sep="\t")
    
    feature_prevalence_filepath = os.path.join(output_directory, "output", f"feature_prevalence.{level}s.tsv.gz")
    logger.info(f"[level={level}] Calculating feature prevalence: {feature_prevalence_filepath}")
    df_feature_prevalence = build_wide_feature_prevalence_matrix(df_feature_abundance, threshold=0)
    df_feature_prevalence.to_csv(feature_prevalence_filepath, sep="\t")
    
    feature_prevalence_binary_filepath = os.path.join(output_directory, "output", f"feature_prevalence-binary.{level}s.tsv.gz")
    logger.info(f"[level={level}] Reformatting binary feature prevalence: {feature_prevalence_binary_filepath}")
    df_feature_prevalence_binary = (df_feature_prevalence > 0).astype(int)
    df_feature_prevalence_binary.to_csv(feature_prevalence_binary_filepath, sep="\t")
    
    if config["contains_pathways"]:
        logger.info(f"[level={level}] Building binary feature prevalence to dictionary")
        genome_to_features = build_feature_prevalence_dictionary(df_feature_prevalence_binary)
        logger.info(f"[level={level}] Building feature to pathways dictionary")
        feature_to_pathways = build_feature_pathway_dictionary(pathway_to_data)
        logger.info(f"[level={level}] Calculating pathway coverage")
        coverages = calculate_pathway_coverage(genome_to_features, pathway_to_data)
        
        pathway_abundances_filepath = os.path.join(output_directory, "output", f"pathway_abundances.{level}s.tsv.gz")
        logger.info(f"[level={level}] Aggregating pathway abundances and appending coverages: {pathway_abundances_filepath}")
        df_pathway_abundances = aggregate_pathway_abundance_and_append_coverage(df_feature_abundance, feature_to_pathways, coverages, index_names = [f"id_{level}", "id_pathway"])
        df_pathway_abundances.to_csv(pathway_abundances_filepath, sep="\t")

    if config["contains_genome_cluster_mapping"]:
        level="genome_cluster"

        feature_prevalence_filepath = os.path.join(output_directory, "output", "feature_abundances.genome_clusters.tsv.gz")
        logger.info(f"[level=genome_cluster] Calculating feature abundance: {feature_prevalence_filepath}")
        df_feature_abundance = aggregate_feature_abundance_for_clusters(df_feature_abundance, genome_to_data)
        df_feature_abundance.to_csv(feature_prevalence_filepath, sep="\t")
        
        feature_ratio_filepath = os.path.join(output_directory, "output", "feature_prevalence-ratio.genome_clusters.tsv.gz")
        logger.info(f"[level=genome_cluster] Calculating feature prevalence ratios: {feature_ratio_filepath}")
        df_feature_prevalence_ratio = (df_feature_prevalence > 0).groupby(lambda x: genome_to_data[x]["id_genome_cluster"]).mean()
        df_feature_prevalence_ratio.to_csv(feature_ratio_filepath, sep="\t")
        
        feature_prevalence_filepath = os.path.join(output_directory, "output", "feature_prevalence.genome_clusters.tsv.gz")
        logger.info(f"[level=genome_cluster] Calculating feature prevalence: {feature_prevalence_filepath}")
        df_feature_prevalence = df_feature_prevalence.groupby(lambda x: genome_to_data[x]["id_genome_cluster"]).sum()
        df_feature_prevalence.to_csv(feature_prevalence_filepath, sep="\t")
        
        feature_prevalence_binary_filepath = os.path.join(output_directory, "output", "feature_prevalence-binary.genome_clusters.tsv.gz")
        logger.info(f"[level=genome_cluster] Reformatting binary feature prevalence: {feature_prevalence_binary_filepath}")
        df_feature_prevalence_binary = (df_feature_prevalence > 0).astype(int)
        df_feature_prevalence_binary.to_csv(feature_prevalence_binary_filepath, sep="\t")
        
        if config["contains_pathways"]:
            logger.info(f"[level={level}] Building binary feature prevalence to dictionary")
            genome_to_features = build_feature_prevalence_dictionary(df_feature_prevalence_binary)
            logger.info(f"[level={level}] Building feature to pathways dictionary")
            feature_to_pathways = build_feature_pathway_dictionary(pathway_to_data)
            logger.info(f"[level={level}] Calculating pathway coverage")
            coverages = calculate_pathway_coverage(genome_to_features, pathway_to_data)
            
            pathway_abundances_filepath = os.path.join(output_directory, "output", f"pathway_abundances.{level}s.tsv.gz")
            logger.info(f"[level={level}] Aggregating pathway abundances and appending coverages: {pathway_abundances_filepath}")
            df_pathway_abundances = aggregate_pathway_abundance_and_append_coverage(df_feature_abundance, feature_to_pathways, coverages, index_names = [f"id_{level}", "id_pathway"])
            df_pathway_abundances.to_csv(pathway_abundances_filepath, sep="\t")


    # ========
    # Complete
    # ========    
    logger.info(f"Completed pathway profiling: {opts.name}")
    for filepath in glob.glob(os.path.join(output_directory, "output","*")):
        filesize = get_file_size(filepath, format=True)
        logger.info(f"Output: {filepath} ({filesize})")

if __name__ == "__main__":
    main()
    
    

    
