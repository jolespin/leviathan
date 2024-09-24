#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess
from collections import defaultdict
from pandas.errors import EmptyDataError
from tqdm import tqdm
from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from leviathan.utils import (
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
    parser.add_argument("-d","--index_directory", type=str, required=True, help = "path/to/index_directory/")


    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan info")

    # Commands
    logger.info(f"Command: {sys.argv}")
     
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
        

if __name__ == "__main__":
    main()
    
    

    
