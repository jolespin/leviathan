#!/usr/bin/env python
import sys,os, argparse, warnings, subprocess
from collections import defaultdict
from pandas.errors import EmptyDataError
import pyfastx
from tqdm import tqdm
# from memory_profiler import profile

__program__ = os.path.split(sys.argv[0])[-1]

from .utils import (
    open_file_reader,
    # open_file_writer,
    read_pickle, 
    # write_pickle,
    read_json,
    # write_json,
    # build_logger,
    # reset_logger,
    get_timestamp,
    # format_duration,
    # format_header,
    format_bytes,
    get_file_size,
    profile_peak_memory,
    RunShellCommand,
)

@profile_peak_memory
def process_genomic_databases_and_check_inputs(fasta, feature_mapping, genomes, logger, config):  
   # Fasta
    genes_from_fasta = set()
    for id, seq in tqdm(pyfastx.Fasta(fasta, build_index=False), f"Loading fasta: {fasta}"):
        genes_from_fasta.add(id)
    
    # Feature mapping
    # ===============
    gene_to_data = defaultdict(dict)
    genome_to_data = defaultdict(dict)
    features_from_data = set()
    with open_file_reader(feature_mapping) as f:
        first_line = f.readline().strip()
        assert "\t" in first_line
        fields = first_line.split("\t")
        assert len(fields) in {3,4}, "Expecting the following fields (No header): [id_gene, features, id_genome, (Optional: id_genome_cluster)]"
        if len(fields) == 3:
            id_gene, features, id_genome  = fields
            gene_to_data[id_gene]["features"] = eval(features)
            gene_to_data[id_gene]["id_genome"] = id_genome
            gene_to_data[id_gene]["id_genome_cluster"] = None
            genomes_from_feature_mapping.add(id_genome)
            
            for line in tqdm(f, f"Loading feature mapping: {feature_mapping}"):
                line = line.strip()
                if line:
                    id_gene, features, id_genome = line.split("\t")
                    gene_to_data[id_gene]["features"] = eval(features)
                    gene_to_data[id_gene]["id_genome"] = id_genome
                    gene_to_data[id_gene]["id_genome_cluster"] = None
                    genome_to_data[id_genome][["id_genome_cluster"]] = None
                    
        elif len(fields) == 4:
            id_gene, features, id_genome, id_genome_cluster  = fields
            gene_to_data[id_gene]["features"] = eval(features)
            gene_to_data[id_gene]["id_genome"] = id_genome
            gene_to_data[id_gene]["id_genome_cluster"] = id_genome_cluster
            genome_to_data[id_genome]["id_genome_cluster"] = id_genome_cluster

            for line in tqdm(f, f"Loading feature mapping with genome clusters: {feature_mapping}"):
                line = line.strip()
                if line:
                    id_gene, features, id_genome, id_genome_cluster = line.split("\t")
                    gene_to_data[id_gene]["features"] = eval(features)
                    gene_to_data[id_gene]["id_genome"] = id_genome
                    gene_to_data[id_gene]["id_genome_cluster"] = id_genome_cluster
                    genome_to_data[id_genome]["id_genome_cluster"] = id_genome_cluster
                    
        config["contains_genome_cluster_mapping"] = True
        
    for id_gene, data in gene_to_data.items():
        features_from_data.update(data["features"])

    # Check overlap of genes between --fasta and --feature_mapping
    genes_from_feature_mapping = set(gene_to_data.keys())
    genomes_from_feature_mapping = set(genome_to_data.keys())
    if genes_from_fasta != genes_from_feature_mapping:
        A_exclusive = genes_from_fasta - genomes_from_feature_mapping
        B_exclusive = genomes_from_feature_mapping - genes_from_fasta
        msg = "--fasta must contain same genes in --feature_mapping"
        if A_exclusive:
            msg += f"\nN={len(A_exclusive)} genes in --fasta that are not in --feature_mapping"
        if B_exclusive:
            msg += f"\nN={len(B_exclusive)} genes in --feature_mapping that are not in --fasta"
        logger.critical(msg)
        raise IndexError(msg)
    config["number_of_genes"] = len(genes_from_feature_mapping)
    config["number_of_features"] = len(features_from_data)
    
    # Check if features as KEGG orthologs
    config["feature_type_is_kegg_ortholog"] = True
    for id_feature in features_from_data:
        conditions = [
            id_feature.startswith("K"),
            len(id_feature) == 6,
            id_feature[1:].isnumeric(),
        ]
        if not all(conditions):
            config["feature_type_is_kegg_ortholog"] = False
    
    # Genomes
    # =======
    genomes_with_filepaths = set()
    if genomes is not None:
        with open_file_reader(genomes) as f:
            for line in tqdm(f, f"Loading genomes: {genomes}"):
                line = line.strip()
                if line:
                    id_genome, filepath = line.split("\t")
                    genome_to_data[id_genome]["filepath"] = filepath
                    genomes_with_filepaths.add(id_genome)
                    
        if genomes_from_feature_mapping != genomes_with_filepaths:
            A_exclusive = genomes_from_feature_mapping - genomes_with_filepaths
            B_exclusive = genomes_with_filepaths - genomes_from_feature_mapping
            msg = "--feature_mapping and --genomes genome sets are different"
            if A_exclusive:
                msg += f"\nN={len(A_exclusive)} genomes in --feature_mapping that are not in --genomes"
            if B_exclusive:
                msg += f"\nN={len(B_exclusive)} genomes in --genomes that are not in --feature_mapping"
            logger.warn(msg)
            # raise IndexError(msg)
        
        config["contains_genome_filepaths"] = True
        
    config["number_of_genomes"] = len(genomes_with_filepaths)
    config["timestamp"] = get_timestamp()

    return config, gene_to_data, genome_to_data

# Load genome database and check inputs
def update_genome_database_with_fasta_filepaths_and_check_inputs(index_directory, genomes, logger, config):
    # Read database files
    gene_to_data = read_pickle(os.path.join(index_directory, "database", "gene_to_data.pkl.gz"))
    genome_to_data = read_pickle(os.path.join(index_directory, "database", "genome_to_data.pkl.gz"))
    genomes_from_feature_mapping = set(genome_to_data.keys())

    # Genomes
    genomes_with_filepaths = set()
    with open_file_reader(genomes) as f:
        for line in tqdm(f, f"Loading genomes: {genomes}"):
            line = line.strip()
            if line:
                id_genome, filepath = line.split("\t")
                genome_to_data[id_genome]["filepath"] = filepath
                genomes_with_filepaths.add(id_genome)
                
    if genomes_from_feature_mapping != genomes_with_filepaths:
        A_exclusive = genomes_from_feature_mapping - genomes_with_filepaths
        B_exclusive = genomes_with_filepaths - genomes_from_feature_mapping
        msg = "--feature_mapping and --genomes genome sets are different"
        if A_exclusive:
            msg += f"\nN={len(A_exclusive)} genomes in --feature_mapping that are not in --genomes"
        if B_exclusive:
            msg += f"\nN={len(B_exclusive)} genomes in --genomes that are not in --feature_mapping"
        logger.warn(msg)
        # raise IndexError(msg)
    
    config["contains_genome_filepaths"] = True
    config["timestamp"] = get_timestamp()

    return config, gene_to_data, genome_to_data

# Check pathway database
def load_pathway_database_and_check_inputs(index_directory, gene_to_data, logger, config):
    # Read database files
    pathway_to_data = read_pickle(os.path.join(index_directory, "database", "pathway_to_data.pkl.gz"))

    # Features from gene identifier mapping
    features_from_data = set()
    for id_gene, data in gene_to_data.items():
        features_from_data.update(data["features"])
        
    # Features from pathways
    features_from_pathways = set()
    for id_pathway, data in pathway_to_data.items():
        features_from_pathways.update(set(data["ko_to_nodes"].keys()))
        
    # Overlapping features
    overlapping_features = features_from_data & features_from_pathways
    number_of_overlapping_features = len(overlapping_features)
                
    if number_of_overlapping_features > 0:
        A_exclusive = features_from_data - features_from_pathways
        B_exclusive = features_from_pathways - features_from_data
        logger.info(f"Number of features from data: {len(features_from_data)} [Exclusive: {len(A_exclusive)}]")
        logger.info(f"Number of features from pathways: {len(features_from_pathways)} [Exclusive: {len(B_exclusive)}]")
        logger.info(f"Number of features overlapping between data and pathways: {number_of_overlapping_features}")
        config["number_of_features_in_pathways"] = len(features_from_pathways)
        config["number_of_features_overlapping_in_pathways"] = number_of_overlapping_features

    else:
        msg = f"No features {len(features_from_data)} from gene_to_data.pkl.gz overlap with the pathway_to_data.pkl.gz database.\nTo address this, either 1) remove pathway database, 2) confirm pathway database features match gene feature types, or 3) use KEGG orthologs for gene feature types"
        msg += "\n\nHere are a few of the features from gene_to_data.pkl.gz: {}".format("\n\t".join(list(features_from_data)[:min(5, len(features_from_data))]))
        msg += "\n\nHere are a few of the features from pathway_to_data.pkl.gz: {}".format("\n\t".join(list(features_from_data)[:min(5, len(features_from_pathways))]))
        logger.critical(msg)
        raise IndexError(msg)
    
    config["timestamp"] = get_timestamp()

    
    return config, pathway_to_data

# Check salmon index files
def check_salmon_index(salmon_index_directory, logger):
    expected_files = [
        'seq.bin', 'info.json', 'pre_indexing.log', 'ref_indexing.log', 'ctable.bin', 'refAccumLengths.bin', 
        'mphf.bin', 'versionInfo.json', 'duplicate_clusters.tsv', 'ctg_offsets.bin', 'reflengths.bin', 
        'pos.bin', 'refseq.bin', 'complete_ref_lens.bin', 'rank.bin',
        ]
    
    missing_files = list()
    empty_files = list()
    if os.path.exists(salmon_index_directory):
        for filename in expected_files:
            filepath = os.path.join(salmon_index_directory, filename)
            if not os.path.exists(filepath):
                missing_files.append(filepath)
                
            filesize = get_file_size(filepath)
            logger.info(f"[salmon_index] {filepath} ({format_bytes(filesize)})")
            if filesize < 1:
                empty_files.append(filepath)
        if any(missing_files):
            msg = f"Salmon index directory is corrupted.  The following files are missing: {missing_files}]"
            logger.critical(msg)
            raise FileNotFoundError(msg)
        if any(empty_files):
            msg = f"Salmon index directory is corrupted.  The following files are empty: {empty_files}]"
            logger.critical(msg)
            raise EmptyDataError(msg)
    else:
        msg = f"Salmon index directory does not exist: {salmon_index_directory} therefore updates are not applicable.  Please rerun with --fasta, --feature_mapping, and --genomes arguments"
        logger.critical(msg)
        raise FileNotFoundError(msg)

# Run Salmon (salmon index --keepDuplicates --threads ${N_JOBS} --transcripts ${FASTA} --index ${INDEX})
def run_salmon_indexer(logger, log_directory, salmon_executable, n_jobs, fasta, index_directory, index_options):    
    cmd = RunShellCommand(
        command=[
            salmon_executable,
            "index",
            "--keepDuplicates",
            "--threads",
            n_jobs,
            "--transcripts",
            fasta,
            "--index",
            os.path.join(index_directory, "salmon_index"),
            index_options,   
            ], 
        name="salmon_indexer",
    )
    
    # Run
    logger.info(f"[{cmd.name}] running command: {cmd.command}")
    cmd.run()
    logger.info(f"[{cmd.name}] duration: {cmd.duration_}")
    logger.info(f"[{cmd.name}] peak memory: {format_bytes(cmd.peak_memory_)}")

    # Dump
    logger.info(f"[{cmd.name}] dumping stdout, stderr, and return code: {log_directory}")
    cmd.dump(log_directory)
    
    # Validate
    logger.info(f"[{cmd.name}] checking return code status: {cmd.returncode_}")
    cmd.check_status()
    return cmd

# Run Sylph (sylph sketch -t ${N_JOBS} --gl ${GENOMES} -o ${INDEX} -k ${K} --min-spacing ${MIN_SPACING})
def run_sylph_genomes_sketcher(logger, log_directory, sylph_executable, n_jobs, genome_filepaths, index_directory, k, minimum_spacing, subsampling_rate, sylph_sketch_options):
    cmd = RunShellCommand(
        command=[
            sylph_executable,
            "sketch",
            "-t",
            n_jobs,
            "--gl",
            genome_filepaths,
            "-o",
            os.path.join(index_directory, "database", "genomes"),
            "-k",
            k,
            "--min-spacing",
            minimum_spacing,
            "-c",
            subsampling_rate,
            sylph_sketch_options,
        ],
        name="sylph_genomes_sketcher",
    )
    
    # Run
    logger.info(f"[{cmd.name}] running command: {cmd.command}")
    cmd.run()
    logger.info(f"[{cmd.name}] duration: {cmd.duration_}")
    logger.info(f"[{cmd.name}] peak memory: {format_bytes(cmd.peak_memory_)}")

    # Dump
    logger.info(f"[{cmd.name}] dumping stdout, stderr, and return code: {log_directory}")
    cmd.dump(log_directory)
    
    # Validate
    logger.info(f"[{cmd.name}] checking return code status: {cmd.returncode_}")
    cmd.check_status()
    return cmd

    
# Download KEGG Pathway Database
def run_kegg_pathway_downloader(logger, log_directory, pathway_database_downloader_executable,  index_directory, no_intermediate_files):
    cmd = RunShellCommand(
        command=[
            pathway_database_downloader_executable,
            "--download",
            "--force",
            "--no_intermediate_files" if no_intermediate_files else "",
            "--database",
            os.path.join(index_directory, "database", "pathway_to_data.pkl.gz"),
    
        ],
        name="kegg_pathway_downloader",
    )
    
    # Run
    logger.info(f"[{cmd.name}] running command: {cmd.command}")
    cmd.run()
    logger.info(f"[{cmd.name}] duration: {cmd.duration_}")
    logger.info(f"[{cmd.name}] peak memory: {format_bytes(cmd.peak_memory_)}")

    # Dump
    logger.info(f"[{cmd.name}] dumping stdout, stderr, and return code: {log_directory}")
    cmd.dump(log_directory)
    
    # Validate
    logger.info(f"[{cmd.name}] checking return code status: {cmd.returncode_}")
    cmd.check_status()
    return cmd