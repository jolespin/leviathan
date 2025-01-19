#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess, shutil
from collections import defaultdict
# from importlib.resources import files as resource_files
# from pandas.errors import EmptyDataError
import pandas as pd
from tqdm import tqdm
import pyfastx
# from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from pyexeggutor import (
    open_file_reader,
    open_file_writer,
    # read_pickle, 
    # write_pickle,
    # read_json,
    write_json,
    build_logger,
    # reset_logger,
    format_duration,
    # format_header,
    format_bytes,
    # get_timestamp,
    get_directory_tree,
    get_directory_size,
    get_md5hash_from_directory,
    # RunShellCommand,
)
from leviathan.utils import (
    read_annotations,
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
    usage = f"{__program__} -i/--input path/to/input.tsv -a path/to/annotations.tsv -o/--output_directory path/to/output_directory/"
    epilog = "Copyright 2024 New Atlantis Labs (jolespin@newatlantis.io)"

    # Parser
    parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # Pipeline
    parser.add_argument("-i","--input", type=str, default="stdin", help = "path/to/input.tsv[.gz] [id_genome, path/to/assembly.fasta, path/to/cds.fasta. [Optional: id_genome_cluster]] (No header, Tab delimited)")
    parser.add_argument("-a","--annotations", type=str, help = "path/to/annotations.tsv[.gz] from either PyKOfamSearch or PyHMMSearch (with header). Note: Assumes protein-level annotations have same protein identifiers as CDS sequences")
    parser.add_argument("-f","--annotation_format", type=str, default="pykofamsearch", 
                           choices={"pykofamsearch", "pyhmmsearch", "pykofamsearch-reformatted", "pyhmmsearch-reformatted", "veba-pfam","veba-kofam","veba-cazy","veba-uniref", "veba-mibig", "veba-vfdb","veba-amr", "custom"}, 
                           help = "Annotation format. If 'custom', then annotation table must be 2 columns [id_gene, id_feature] (No header, Tab delimited)"
                                   "and can contain multiple lines per gene. [Default: pykofamsearch]",
                                   )
    parser.add_argument("-o","--output_directory", type=str, help = "path/to/output_directory/ output directory that includes feature_mapping.tsv, genomes.tsv, and cds.fasta")
    # parser.add_argument("-f", "--force", action="store_true", help = "If --output_directory exists, then overwrite contents")

    # Options
    opts = parser.parse_args()
    opts.script_directory  = script_directory
    opts.script_filename = script_filename

    # logger
    logger = build_logger("leviathan preprocess")
    
    # Command
    logger.info(f"Command: {sys.argv}")

    # Output
    logger.info(f"Creating output directory: {opts.output_directory}")
    os.makedirs(opts.output_directory, exist_ok=True)

    # try:
        # os.makedirs(opts.output_directory, exist_ok=bool(opts.force))
    # except FileExistsError:
        # raise FileExistsError(f"--output_directory {opts.output_directory} already exists.  Either remove {opts.output_directory}, change --output_directory, or use --force to overwrite")

    # Input
    logger.info(f"Reading input: {opts.input}")
    if opts.input == "stdin":
        opts.input = sys.stdin

    df_input = pd.read_csv(opts.input, sep="\t", header=None)
    number_of_genomes, m = df_input.shape
    if m not in {3,4}:
        raise IndexError(f"--input has {m} columns but must be either 3 or 4 columns: [id_genome, path/to/assembly.fasta, path/to/cds.fasta. [Optional: id_genome_cluster]] (No header, Tab delimited)")
    df_input.columns = ["id_genome", "assembly", "cds", "id_genome_cluster"][:m]
    df_input = df_input.set_index("id_genome")
    
    genome_to_genomecluster = None
    if "id_genome_cluster" in df_input.columns:
        genome_to_genomecluster = df_input["id_genome_cluster"].to_dict()
        
    # Genomes
    genomes_filepath = os.path.join(opts.output_directory, "genomes.tsv.gz")
    logger.info(f"Writing genome filepaths: {genomes_filepath}")
    df_input["assembly"].to_csv(genomes_filepath, sep="\t", header=None)

    # Annotations
    logger.info(f"Reading annotations: {opts.input} [Format: {opts.annotation_format}]")
    gene_to_features = read_annotations(opts.annotations, format=opts.annotation_format)    
     
    # Build CDS fasta
    cds_identifiers = set()
    gene_to_genome = dict()
    with open_file_writer(os.path.join(opts.output_directory, "cds.fasta.gz")) as f:
        for id_genome, cds_filepath in tqdm(df_input["cds"].items(), total=number_of_genomes, desc="Extract feature sequences from CDS fasta"):
            for id_gene, seq in pyfastx.Fasta(cds_filepath, build_index=False):
                if id_gene in gene_to_features:
                    feature_set = gene_to_features[id_gene]
                    print(">{} [id_genome={}][features={}]\n{}".format(id_gene, id_genome, feature_set, seq), file=f)
                    cds_identifiers.add(id_gene)
                    gene_to_genome[id_gene] = id_genome
                    
    genes_missing_cds_sequences = set(gene_to_features.keys()) - cds_identifiers
    if genes_missing_cds_sequences:
        logger.warning(f"Number of genes in --annotations that do not have sequences from --input: {len(genes_missing_cds_sequences)}")
        with open_file_writer(os.path.join(opts.output_directory, "genes_missing_cds_sequences.list")) as f:
            for id_gene in genes_missing_cds_sequences:
                print(id_gene, file=f)
                
    if not cds_identifiers:
        raise IndexError("None of the CDS identifiers had protein representatives in --annotations")
    
    logger.info(f"Number of CDS sequences with features: {len(cds_identifiers)}")

    # Feature mapping
    feature_mapping_filepath = os.path.join(opts.output_directory, "feature_mapping.tsv.gz")
    logger.info(f"Building feature mappings: {feature_mapping_filepath}")

    f_feature_mapping = open_file_writer(feature_mapping_filepath)
    if genome_to_genomecluster:
        for id_gene, feature_set in tqdm(gene_to_features.items(), desc=f"Writing feature mapping table [Genome_Clusters = True]"): # [id_gene, feature_set, id_genome, (Optional: id_genome_cluster)] 
            if id_gene in cds_identifiers:
                id_genome = gene_to_genome[id_gene]
                id_genome_cluster = genome_to_genomecluster[id_genome]
                fields = [
                    id_gene, 
                    feature_set,
                    id_genome,
                    id_genome_cluster,
                ]
                print(*fields, sep="\t", file=f_feature_mapping)    
    else:
        for id_gene, feature_set in tqdm(gene_to_features.items(), desc=f"Writing feature mapping table [Genome_Clusters = False]"): # [id_gene, feature_set, id_genome, (Optional: id_genome_cluster)] 
            if id_gene in cds_identifiers:
                id_genome = gene_to_genome[id_gene]
                fields = [
                    id_gene, 
                    feature_set,
                    id_genome,
                ]
                print(*fields, sep="\t", file=f_feature_mapping)    
    f_feature_mapping.close()
    
    # ========
    # Hash
    # ========   
    md5hash_filepath = os.path.join(opts.output_directory, "md5hashes.json")
    logger.info(f"Calculating md5 hashes: {md5hash_filepath}")
    file_to_hash = get_md5hash_from_directory(opts.output_directory)
    write_json(file_to_hash, md5hash_filepath)

    # ========
    # Complete
    # ========    
    logger.info(f"Completed preprocessing input data for leviathan index: {opts.output_directory}")
    logger.info(f"Directory size of leviathan preprocessing: {format_bytes(get_directory_size(opts.output_directory))}")
    logger.info(f"Directory structure of leviathan preprocessing:\n{get_directory_tree(opts.output_directory, ascii=True)}")

if __name__ == "__main__":
    main()
    
    

    
