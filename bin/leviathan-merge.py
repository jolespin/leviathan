#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess
from collections import defaultdict
from itertools import product, chain
from pandas.errors import EmptyDataError
from tqdm import tqdm
from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from pyexeggutor import (
    open_file_reader,
    # open_file_writer,
    read_pickle, 
    # write_pickle,
    read_json,
    # write_json,
    build_logger,
    # reset_logger,
    # format_duration,
    # format_header,
    format_bytes,
    # get_directory_tree,
    get_directory_size,
    get_md5hash_from_file,
    get_md5hash_from_directory,
    # RunShellCommand,
)

from leviathan.utils import (
    merge_taxonomic_profiling_tables,
    merge_pathway_profiling_tables,
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
    usage = f"{__program__} -t path/to/taxonomic_profiling_directory/ -p path/to/pathway_profiling_directory/ -o path/to/output_directory/"
    epilog = "Copyright 2024 New Atlantis Labs (jolespin@newatlantis.io)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # Pipeline
    parser.add_argument("-t","--taxonomic_profiling_directory", type=str, help = "path/to/profiling/taxonomy/")
    parser.add_argument("-p","--pathway_profiling_directory", type=str, help = "path/to/profiling/pathway/")
    parser.add_argument("-o","--output_directory", type=str,  help = "path/to/output_directory. Default is either --taxonomic_profiling_directory and --pathway_profiling_directory")
    parser.add_argument("-f","--output_format", type=str, choices={"tsv", "pickle", "parquet"}, default="parquet", help = "Output format [Default: parquet]")
    parser.add_argument("-z","--fillna_with_zeros", action="store_true", help = "Fill missing values with 0.  This will take a lot longer to write to disk.")
    parser.add_argument("-s","--sparse", action="store_true", help = "Output pd.SparseDtype.  This will take a lot longer to write to disk.  Only applicable when --output_format=pickle.")


    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan merge")

    # Commands
    logger.info(f"Command: {sys.argv}")
     
    # I/O
    if opts.output_format == "parquet":
        logger.warn(f"--output_format parquet results in transposed output relative to tsv and pickle (n=genomes, m=features).  To avoid memory constraints, parquet will have features as rows and genomes/genome-clusters as columns.")
    ## Taxonomic Profiling
    proceed_with_merging_taxonomic_profiles = False
    taxonomic_profiling_output_directory = None
    if opts.taxonomic_profiling_directory:
        if os.path.exists(opts.taxonomic_profiling_directory):
            proceed_with_merging_taxonomic_profiles = True
            if not opts.output_directory:
                taxonomic_profiling_output_directory = opts.taxonomic_profiling_directory
            else:
                taxonomic_profiling_output_directory = opts.output_directory
        logger.info(f"Creating taxonomic profiling output directory (if it does not exist): {taxonomic_profiling_output_directory}")
        os.makedirs(taxonomic_profiling_output_directory, exist_ok=True)
        
    ## Pathway Profiling
    proceed_with_merging_pathway_profiles = False
    pathway_profiling_output_directory = None
    if opts.pathway_profiling_directory:
        if os.path.exists(opts.pathway_profiling_directory):
            proceed_with_merging_pathway_profiles = True
            if not opts.output_directory:
                pathway_profiling_output_directory = opts.pathway_profiling_directory
            else:
                pathway_profiling_output_directory = opts.output_directory
        logger.info(f"Creating pathway profiling output directory (if it does not exist): {pathway_profiling_output_directory}")
        os.makedirs(pathway_profiling_output_directory, exist_ok=True)
        
    # Run
    ## Taxonomic Profiling
    if proceed_with_merging_taxonomic_profiles:
        for level in ["genomes", "genome_clusters"]:
            logger.info(f"Merging taxonomic profiles for level={level}")

            try:
                X = merge_taxonomic_profiling_tables(
                    profiling_directory=opts.taxonomic_profiling_directory, 
                    level=level, 
                    fillna_with_zeros=bool(opts.fillna_with_zeros), 
                    sparse=opts.sparse if opts.output_format == "pickle" else False,
                )
                if X.empty:
                    raise EmptyDataError(f"Merging taxonomic profiles for level={level} in {opts.taxonomic_profiling_directory} resulted in empty DataFrame")
                
                logger.info(f"Taxonomic profiles for level={level} have {X.shape[0]} rows and {X.shape[1]} columns")

                if opts.output_format == "parquet":
                    filepath = os.path.join(taxonomic_profiling_output_directory, f"taxonomic_abundance.{level}.parquet")
                    logger.info(f"Writing output: {filepath}")
                    X.T.to_parquet(filepath, index=True)
                elif opts.output_format == "tsv":
                    filepath = os.path.join(taxonomic_profiling_output_directory, f"taxonomic_abundance.{level}.tsv.gz")
                    logger.info(f"Writing output: {filepath}")
                    X.to_csv(filepath, sep="\t")
                elif opts.output_format == "pickle":
                    filepath = os.path.join(taxonomic_profiling_output_directory, f"taxonomic_abundance.{level}.pkl.gz")
                    logger.info(f"Writing output: {filepath}")
                    X.to_pickle(filepath, sep="\t")

            except Exception as e:
                logger.info(f"No level={level} files found in {opts.taxonomic_profiling_directory}: {e}")
        logger.info(f"Completed merging taxonomic profiling tables: {taxonomic_profiling_output_directory}")

    ## Pathway Profiling
    if proceed_with_merging_pathway_profiles:

        levels = ["genomes", "genome_clusters"]
        abundance_data_types = ["feature_abundances", "gene_abundances", "pathway_abundances"]
        prevalence_data_types = ["feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio"]
        metrics = ["number_of_reads", "tpm", "coverage"]
        
        argument_combinations = chain(
            product(levels, abundance_data_types, metrics),
            product(levels, prevalence_data_types, ["number_of_reads"]), # Expects an argument but it's not actually used

        )

        for level, data_type, metric in argument_combinations:
            illegal_conditions = [
                (level == "genome_cluster") and (data_type == "gene_abundances"),
                (level == "genomes") and (data_type == "feature_prevalence-ratio"),
                (data_type != "pathway_abundances") and (metric == "coverage"),
            ]
            if not any(illegal_conditions):
                try:
 
                    if data_type in prevalence_data_types:
                        X = merge_pathway_profiling_tables(
                            profiling_directory=opts.pathway_profiling_directory, 
                            data_type=data_type, 
                            level=level, 
                            metric=metric, 
                            fillna_with_zeros=bool(opts.fillna_with_zeros), 
                            sparse=opts.sparse if opts.output_format == "pickle" else False)
                        if X.empty:
                            raise EmptyDataError(f"Merging pathway profiles for level={level}, data_type={data_type} in {opts.pathway_profiling_directory} resulted in empty DataFrame")
                        if opts.output_format == "parquet":
                            X = X.T
                        logger.info(f"Pathway profiles for level={level}, data_type={data_type} have {X.shape[0]} rows and {X.shape[1]} columns")
                    
                        if opts.output_format == "parquet":
                            filepath = os.path.join(pathway_profiling_output_directory, f"{data_type}.{level}.parquet")
                            logger.info(f"Writing output: {filepath}")
                            X.to_parquet(filepath, index=True)
                        elif opts.output_format == "tsv":
                            filepath = os.path.join(pathway_profiling_output_directory, f"{data_type}.{level}.tsv.gz")
                            logger.info(f"Writing output: {filepath}")
                            X.to_csv(filepath, sep="\t")
                        elif opts.output_format == "pickle":
                            filepath = os.path.join(pathway_profiling_output_directory, f"{data_type}.{level}.pkl.gz")
                            logger.info(f"Writing output: {filepath}")
                            X.to_pickle(filepath, sep="\t")
                    else:
                        X = merge_pathway_profiling_tables(
                            profiling_directory=opts.pathway_profiling_directory, 
                            data_type=data_type, 
                            level=level, 
                            metric=metric, 
                            fillna_with_zeros=bool(opts.fillna_with_zeros), 
                            sparse=opts.sparse if opts.output_format == "pickle" else False,
                        )
                        if X.empty:
                            raise EmptyDataError(f"Merging pathway profiles for level={level}, data_type={data_type}, metric={metric} in {opts.pathway_profiling_directory} resulted in empty DataFrame")
                        if opts.output_format == "parquet":
                            X = X.T
                        logger.info(f"Pathway profiles for level={level}, data_type={data_type}, metric={metric} have {X.shape[0]} rows and {X.shape[1]} columns")
                        
                        if opts.output_format == "parquet":
                            filepath = os.path.join(pathway_profiling_output_directory, f"{data_type}.{level}.{metric}.parquet")
                            logger.info(f"Writing output: {filepath}")
                            X.to_parquet(filepath, index=True)
                        elif opts.output_format == "tsv":
                            filepath = os.path.join(pathway_profiling_output_directory, f"{data_type}.{level}.{metric}.tsv.gz")
                            logger.info(f"Writing output: {filepath}")
                            X.to_csv(filepath, sep="\t")
                        elif opts.output_format == "pickle":
                            filepath = os.path.join(pathway_profiling_output_directory, f"{data_type}.{level}.{metric}.pkl.gz")
                            logger.info(f"Writing output: {filepath}")
                            X.to_pickle(filepath, sep="\t")

                except Exception as e:
                    logger.warning(f"Not able to merge {data_type}.{level}.{metric} files from {opts.pathway_profiling_directory}: {e}")
        logger.info(f"Completed merging pathway profiling tables: {pathway_profiling_output_directory}")


if __name__ == "__main__":
    main()


    
