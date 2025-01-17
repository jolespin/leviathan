#!/usr/bin/env python
import sys, os, argparse, glob
from collections import defaultdict
from tqdm import tqdm

__program__ = os.path.split(sys.argv[0])[-1]

from pyexeggutor import (
    open_file_reader,
    open_file_writer,
    build_logger,
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
    usage = f"{__program__} -i path/to/veba_output/ -t prokaryotic,eukaryotic -o path/to/output.tsv"
    epilog = "Copyright 2024 New Atlantis Labs (jolespin@newatlantis.io)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # Pipeline
    parser_io = parser.add_argument_group('I/O arguments')
    parser_io.add_argument("-i","--veba_directory", type=str, required=True, help = "path/to/veba_directory/ (e.g., veba_output/)")
    parser_io.add_argument("-t","--organism_types", type=str, default = "prokaryotic,eukaryotic", help="Comma-separated list of organism types.  Choose between {prokaryotic, eukaryotic, viral}(e.g., prokaryotic,eukaryotic).  viral is not recommended.")
    parser_io.add_argument("-o", "--output", type=str,  default="stdout", help = "path/to/output.tsv[.gz] [Default: stdout]")

    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan compile-manifest-from-veba")

    # Commands
    logger.info(f"Command: {sys.argv}")
     
    # Inputs
    logger.info(f"Checking input directory: {opts.veba_directory}")

    if not os.path.exists(opts.veba_directory):
        logger.error(f"Error: {opts.veba_directory} does not exist.")
        sys.exit(1)
    if not os.path.isdir(opts.veba_directory):
        logger.error(f"Error: {opts.veba_directory} is not a directory.")
        sys.exit(1)
    # Output
    if opts.output == "stdout":
        f_out = sys.stdout
    else:
        f_out = open_file_writer(opts.output)
        
    logger.info(f"Creating output: {f_out}")
    
    # Organism types
    opts.organism_types = opts.organism_types.split(",")
    logger.info(f"Parsing organism types: {opts.organism_types}")

    for organism_type in opts.organism_types:
        if organism_type.lower() == "viral":
            logger.warning(f"'viral' is not recommended for organism types because small genomes require different parameters than medium-to-large genomes with Sylph.")

    # Create manifest
    manifest = defaultdict(dict)
    for organism_type in opts.organism_types:
        organism_type_directory = os.path.join(opts.veba_directory, "binning", organism_type)
        logger.info(f"Creating manifest from {organism_type_directory}")
        if not os.path.exists(organism_type_directory):
            logger.critical(f"{organism_type_directory} does not exist.")
            sys.exit(1)
        if not os.path.isdir(organism_type_directory):
            logger.error(f"{organism_type_directory}  is not a directory.")
            sys.exit(1)
        for filepath in tqdm(glob.glob(os.path.join(organism_type_directory, "*", "output", "genomes", "*.fa")), f"Identifying genomes assemblies for {organism_type}", unit=" genomes"):
            id_genome = os.path.split(filepath)[1][:-3]
            manifest[id_genome]["assembly"] = filepath
        for filepath in tqdm(glob.glob(os.path.join(organism_type_directory, "*", "output", "genomes", "*.ffn")), f"Identifying CDS sequences for {organism_type}", unit=" genomes"):
            id_genome = os.path.split(filepath)[1][:-4]
            manifest[id_genome]["cds"] = filepath
        
    # Genome clusters
    contains_genome_clusters = False
    genome_cluster_filepath = os.path.join(opts.veba_directory, "cluster", "output", "global", "mags_to_slcs.tsv")
    
    if os.path.exists(genome_cluster_filepath):
        logger.info(f"Adding genome clusters from {genome_cluster_filepath}")
        with open_file_reader(genome_cluster_filepath) as f_in:
            for line in f_in:
                line = line.strip()
                if line:
                    id_genome, id_cluster = line.strip().split("\t")
                    if id_genome in manifest:
                        manifest[id_genome]["id_genome_cluster"] = id_cluster
        contains_genome_clusters = True
    else:
        logger.warning(f"No genome clusters found at {genome_cluster_filepath}")

    

    # Check files
    logger.info(f"Checking assembly and CDS files for manifest")
    for id_genome, data in tqdm(manifest.items(), unit=" genomes"):
        try:
            filepath = data["assembly"]
            if not os.path.exists(filepath):
                logger.critical(f"{filepath} does not exist.")
                sys.exit(1)
        except KeyError:
            logger.critical(f"{id_genome} does not have an assembly fasta file.")
            sys.exit(1)
        try:
            filepath = data["cds"]
            if not os.path.exists(filepath):
                logger.critical(f"{filepath} does not exist.")
                sys.exit(1)
        except KeyError:
            logger.critical(f"{id_genome} does not have a CDS fasta file.")
            sys.exit(1)
    if contains_genome_clusters:
        logger.info(f"Checking clustering for genomes in manifest",)
        genomes_missing_clusters = set()
        for id_genome, data in tqdm(manifest.items(), unit=" genomes"):
            try:
                id_cluster = data["id_genome_cluster"]
            except KeyError:
                genomes_missing_clusters.add(id_genome)
                sys.exit(1)
        if genomes_missing_clusters:
            logger.critical("The following genomes do not have genome clusters:{}".format("\n".join(sorted(genomes_missing_clusters))))
            sys.exit(1)
            
    # Write manifest
    logger.info(f"Writing manifest: {f_out}")
    if contains_genome_clusters:
        for id_genome, data in manifest.items():
            print(id_genome, data["assembly"], data["cds"], data["id_genome_cluster"],sep="\t", file=f_out)
    else:
        for id_genome, data in manifest.items():
            print(id_genome, data["assembly"], data["cds"], sep="\t", file=f_out)
    if f_out != sys.stdout:
        f_out.close()
        
    # ========
    # Complete
    # ========    
    logger.info(f"Completed generating manifest: {f_out}")
            
if __name__ == "__main__":
    main()
    
    

    
