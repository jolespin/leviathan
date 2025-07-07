#!/usr/bin/env python
import sys
import os
import argparse
from collections import defaultdict
from itertools import (
    product, 
    chain,
)
from pandas.errors import EmptyDataError
from tqdm import tqdm
import xarray as xr

from pyexeggutor import (
    build_logger,
)

from leviathan.profile_taxonomy import (
    merge_taxonomic_profiling_tables_as_xarray,
)
from leviathan.profile_pathway import (
    merge_pathway_profiling_tables_as_xarray,
)

__program__ = os.path.split(sys.argv[0])[-1]


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
    epilog = "Copyright 2025 Josh L. Espinoza (jol.espinoz@gmail.com)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # Pipeline
    parser.add_argument("-t","--taxonomic_profiling_directory", type=str, help = "path/to/profiling/taxonomy/")
    parser.add_argument("-p","--pathway_profiling_directory", type=str, help = "path/to/profiling/pathway/")
    parser.add_argument("-o","--output_directory", type=str,  help = "path/to/output_directory. Default is either --taxonomic_profiling_directory and --pathway_profiling_directory")
    parser.add_argument("-z","--fillna_with_zeros", action="store_true", help = "Fill missing values with 0.  This will take a lot longer to write to disk.")
    parser.add_argument("-e", "--xarray_engine", type=str, choices={"h5netcdf", "netcdf4"}, default="h5netcdf", help = "Xarray backend engine [Default: h5netcdf]")
    parser.add_argument("-c", "--xarray_compression_level", type=int, choices=set(range(0, 10)), default=4, help = "netCDF gzip compression level. Use 0 for no compression. [Default: 4]")
    
    # ------------------
    # Pending options
    # ------------------

    # ------------------
    # Deprecated options
    # ------------------
    # parser.add_argument("-f","--output_format", type=str, choices={"tsv", "pickle", "parquet"}, default="parquet", help = "Output format [Default: parquet]")
    # parser.add_argument("-s","--sparse", action="store_true", help = "Output pd.SparseDtype.  This will take a lot longer to write to disk.  Only applicable when --output_format=pickle.")
    # parser.add_argument("--no_transpose_pathway_profiling", action="store_true", help = "Do not transpose pathway profiling tables.  If you do not transpose them, it will use much more memory to read/write unless --output_format pickle")

    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan merge")

    # Commands
    logger.info(f"Command: {sys.argv}")
     
    # I/O
    # if opts.output_format == "parquet":
        # logger.warn(f"--output_format parquet results in transposed output relative to tsv and pickle (n=genomes, m=features).  To avoid memory constraints, parquet will have features as rows and genomes/genome-clusters as columns.")
        
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
        else:
            msg = f"Taxonomic profiling output directory does not exist: {opts.taxonomic_profiling_directory}"
            logger.critical(msg)
            raise Exception(msg)

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
        else:
            msg = f"Pathway profiling output directory does not exist: {opts.pathway_profiling_directory}"
            logger.critical(msg)
            raise Exception(msg)
        
    # Run
    ## Taxonomic Profiling
    if proceed_with_merging_taxonomic_profiles:
        for level in ["genomes", "genome_clusters"]:
            logger.info(f"Merging taxonomic profiles for level={level}")

            try:
                # Filepath
                filepath = os.path.join(taxonomic_profiling_output_directory, f"taxonomic_abundances.{level}.nc")

                X = merge_taxonomic_profiling_tables_as_xarray(
                    profiling_directory=opts.taxonomic_profiling_directory, 
                    level=level, 
                    fillna_with_zeros=bool(opts.fillna_with_zeros), 
                )
                n = X.sizes["samples"]
                m = X.sizes[level]

                error_msg = f"Merging taxonomic profiles for level={level} in {opts.taxonomic_profiling_directory} resulted in empty xr.DataArray"
                info_msg = f"Taxonomy profiles for level={level} have {n} samples, {m} {level}"

                if len(X) == 0:
                    raise EmptyDataError(error_msg)
                    
                logger.info(info_msg)

                if opts.xarray_compression_level:
                    logger.info(f"Setting gzip compression: {opts.xarray_compression_level}")
                    X.encoding.update({"compression": "gzip", "compression_opts": opts.xarray_compression_level})
                
                # logger.info(f"Adding DataArray ({name}) to DataSet group {group}")
                # group_to_dataset[group][name] = X
                mode = "w"
                logger.info(f"Writing output: {filepath} [mode={mode}]")
                X.to_netcdf(filepath, engine=opts.xarray_engine, mode=mode)
                del X
     
            except Exception as e:
                logger.warning(f"No level={level} files found in {opts.taxonomic_profiling_directory}: {e}")
                
        logger.info(f"Completed merging taxonomic profiling tables: {taxonomic_profiling_output_directory}")

    ## Pathway Profiling
    if proceed_with_merging_pathway_profiles:

        levels = ["genomes", "genome_clusters"]
        abundance_data_types = ["feature_abundances", "pathway_abundances"] #  "gene_abundances",
        prevalence_data_types = ["feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio"]
        metrics = ["number_of_reads", "tpm", "coverage"]
        
        argument_combinations = chain(
            product(levels, abundance_data_types, metrics),
            product(levels, prevalence_data_types, ["number_of_reads"]), # Expects an argument but it's not actually used
        )
        
        # Specify group file mode
        group_to_filemode = dict()
        group_to_dataset = defaultdict(xr.Dataset)
        for level, data_type, metric in argument_combinations:
            illegal_conditions = [
                # (level == "genome_cluster") and (data_type == "gene_abundances"),
                (level == "genomes") and (data_type == "feature_prevalence-ratio"),
                (data_type != "pathway_abundances") and (metric == "coverage"),
            ]
            if not any(illegal_conditions):
                try:
                    # Group
                    group = (
                        data_type.split("_")[0], 
                        level,
                    )
                    
                    # Mode
                    if group not in group_to_filemode:
                        group_to_filemode[group] = "w"
                    else:
                        group_to_filemode[group] = "a"
                    mode = group_to_filemode[group]
                    
                    # Filepath
                    filepath = os.path.join(pathway_profiling_output_directory, f"{group[0]}.{group[1]}.nc")

                    # Variable name
                    name = metric if "abundances" in data_type else data_type.split("_")[-1]
                    
                    # Merge pathway profiling
                    X = merge_pathway_profiling_tables_as_xarray(
                        profiling_directory=opts.pathway_profiling_directory, 
                        data_type=data_type, 
                        level=level, 
                        metric=metric, 
                        fillna_with_zeros=bool(opts.fillna_with_zeros), 
                        )

                    if data_type in prevalence_data_types:
                        error_msg = f"Merging pathway profiles for level={level}, data_type={data_type} in {opts.pathway_profiling_directory} resulted in empty xr.DataArray"
                        info_msg = f"Pathway profiles for level={level}, data_type={data_type} have {X.shape[0]} samples, {X.shape[1]} {level}, and {X.shape[2]} features"

                    else:
                        error_msg = f"Merging pathway profiles for level={level}, data_type={data_type}, metric={metric} in {opts.pathway_profiling_directory} resulted in empty xr.DataArray"
                        info_msg = f"Pathway profiles for level={level}, data_type={data_type}, metric={metric} have {X.shape[0]} samples, {X.shape[1]} {level}, and {X.shape[2]} features"

                    if len(X) == 0:
                        raise EmptyDataError(error_msg)
                    
                    logger.info(info_msg)
                    if opts.xarray_compression_level:
                        logger.info(f"Setting gzip compression: {opts.xarray_compression_level}")
                        X.encoding.update({"compression": "gzip", "compression_opts": opts.xarray_compression_level})
                    
                    logger.info(f"Adding DataArray ({name}) to DataSet group {group}")
                    group_to_dataset[group][name] = X
                    logger.info(f"Writing output: {filepath} [mode={mode}]")
                    group_to_dataset[group].to_netcdf(filepath, engine=opts.xarray_engine, mode=mode)
                    del X

                except Exception as e:
                    if data_type in prevalence_data_types:
                        logger.warning(f"Not able to merge {data_type}.{level} files from {opts.pathway_profiling_directory}: {e}")
                    else:
                        logger.warning(f"Not able to merge {data_type}.{level}.{metric} files from {opts.pathway_profiling_directory}: {e}")
                    
        logger.info(f"Completed merging pathway profiling tables: {pathway_profiling_output_directory}")
    logger.info(f"Completed running leviathan-merge: {opts.output_directory}")


if __name__ == "__main__":
    main()


    
