#!/usr/bin/env python
import sys
import os
import argparse

from pyexeggutor import (
    read_json,
    build_logger,
    format_bytes,
    get_directory_size,
    get_md5hash_from_file,
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
    usage = f"{__program__} --fasta path/to/cds.fasta --feature_mapping path/to/features.tsv --genomes path/to/genomes.tsv  --index_directory path/to/leviathan_index/"
    epilog = "Copyright 2024 New Atlantis Labs (jolespin@newatlantis.io)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", "--number_of_rows", type=int, default=10, help="Number of rows to show for parquet [Default: 10]")
    parser.add_argument("-e", "--xarray_engine", type=str, choices={"h5netcdf", "netcdf4"}, default="h5netcdf", help = "Xarray backend engine [Default: h5netcdf]")
    group = parser.add_argument_group('Input Options (choose one)')
    mutex_group = group.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument("-d", "--index_directory", type=str, help="path/to/index_directory/")
    mutex_group.add_argument("-p", "--parquet", type=str, help="path/to/table.parquet")
    mutex_group.add_argument("-x", "--netcdf", type=str, help="path/to/dataset.nc")
    
    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan info")

    # Commands
    logger.info(f"Command: {sys.argv}")
     
    if opts.index_directory:
        logger.info(f"Providing info for index: {opts.index_directory}")
        print()
        # Size
        size_in_bytes = get_directory_size(opts.index_directory)
        logger.info(f"Database size: {format_bytes(size_in_bytes)} ({size_in_bytes} bytes)")

        # Config
        path_config = os.path.join(opts.index_directory, "config.json")
        config = read_json(path_config)
        logger.info(f"Config: {path_config}")
        for k, v in config.items():
            logger.info(f"  |--- {k}: {v}")

        # Hash
        path_md5 = os.path.join(opts.index_directory, "md5hashes.json")
        hashes = read_json(path_md5)
        logger.info(f"MD5 hashes: {path_md5}")
        for k, v in hashes.items():
            logger.info(f"  |--- {k}: {v}")
        
    elif opts.parquet:
        import fastparquet as fp
        logger.info(f"Providing preview of parquet: {opts.parquet}")
        pf = fp.ParquetFile(opts.parquet)
        df = pf.head(opts.number_of_rows)
        print()
        df.to_csv(sys.stdout, sep="\t")
        
    elif opts.netcdf:
        import xarray as xr
        logger.info(f"Providing preview of Xarray NetCDF: {opts.netcdf}")
        ds = xr.open_dataset(opts.netcdf, engine=opts.xarray_engine)
        print()
        print(ds)

    logger.info(f"Finished running leviathan-info: {opts.index_directory}")

        
if __name__ == "__main__":
    main()
    
    

    
