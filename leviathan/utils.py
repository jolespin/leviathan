#!/usr/bin/env python
import sys, os, glob
from tqdm import tqdm
from collections import defaultdict
import pandas as pd
from pyexeggutor import (
    open_file_reader,
    check_argument_choice,
)

# Annotations
def read_annotations(path:str, format="pykofamsearch"):
    
    """
    Reads feature annotations from a given file and returns a dictionary mapping each gene to its associated features.

    Parameters
    ----------
    path : str
        Path to the annotation file
    format : str
        Format of the annotation file. Options: pykofamsearch, pykofamsearch-reformatted, pyhmmsearch, pyhmmsearch-reformatted, veba-pfam, veba-kofam, veba-cazy, veba-uniref, veba-mibig, veba-vfdb, veba-amr, custom

    Returns
    -------
    gene_to_features : dict
        Mapping of gene identifiers to their associated features
    """
    check_argument_choice(
        query=format, 
        choices={"pykofamsearch", "pykofamsearch-reformatted", "pyhmmsearch","pyhmmsearch-reformatted", "veba-pfam","veba-kofam","veba-cazy","veba-uniref", "veba-mibig", "veba-vfdb","veba-amr", "custom"},
        )
    
    if format in {"pykofamsearch", "pyhmmsearch", "custom", "pykofamsearch-reformatted", "pyhmmsearch-reformatted"}:
        f_annotations = open_file_reader(path)

        gene_to_features = defaultdict(set)    
        if format != "custom":
            next(f_annotations)
            
        if format in {"pykofamsearch-reformatted", "pyhmmsearch-reformatted"}:
            for line in tqdm(f_annotations, desc="Extracting feature annotations"):
                line = line.strip()
                if line:
                    id_gene, number_of_hits, features, *extra = line.split("\t")
                    gene_to_features[id_gene] = set(eval(features))

        for line in tqdm(f_annotations, desc="Extracting feature annotations"):
            line = line.strip()
            if line:
                id_gene, id_feature, *extra = line.split("\t")
                gene_to_features[id_gene].add(id_feature)
        f_annotations.close()



    else:
        df_annotations = pd.read_csv(path, sep="\t", index_col=0, header=[0,1])
        
        # HMM-based annotations
        if format in {"veba-pfam", "veba-kofam", "veba-amr"}:
            column = {
                "veba-pfam":("Pfam", "ids"),
                "veba-kofam":("KOfam", "ids"),
                "veba-amr":("NCBIfam-AMR", "ids"),
            }[format]
            gene_to_features = df_annotations[column].map(lambda x: set(eval(x)))
        
        # Diamond-based annotations
        else:
            column = {
                "veba-cazy":("CAZy", "sseqid"),
                "veba-uniref":("UniRef", "sseqid"),
                "veba-mibig":("MIBiG", "sseqid"),
                "veba-vfdb":("VFDB", "sseqid"),
            }[format]
            
            gene_to_features = defaultdict(set)
            for id_gene, id_feature in df_annotations[column].items():
                gene_to_features[id_gene].add(id_feature)
    return gene_to_features

def merge_taxonomic_profiling_tables(profiling_directory:str, level="genome", fillna_with_zeros:bool=False, sparse:bool=False):
    
    """
    Merge taxonomic profiling at the genome or genome cluster level.

    Parameters
    ----------
    profiling_directory : str
        Directory containing the profiling output.
    level : str, optional
        Level at which to merge the taxonomic profiling. Options are
        "genome" or "genome_cluster". Default is "genome".
    fillna_with_zeros : bool, optional
        Whether to fill missing values with zeros. Default is False.
    sparse : bool, optional
        Whether to return a pd.Sparse type. Default is False.
        
    Returns
    -------
    pd.DataFrame
        Merged taxonomic profiling at the specified level.

    Raises
    ------
    KeyError
        If `level` is not in {"genome", "genome_cluster"}.
    FileNotFoundError
        If no files are found in the specified directory.

    Files:
    * taxonomic_abundance.genome_clusters.tsv.gz
    * taxonomic_abundance.genomes.tsv.gz
    """
    choices = {"genomes", "genome_clusters"}
    if level not in choices:
        raise KeyError(f"level must be in {choices}")
    
    output = dict()

    # Genomes
    if level == "genomes":
        filepaths = glob.glob(f"{profiling_directory}/*/output/taxonomic_abundance.genomes.tsv.gz")
        if filepaths:
            for filepath in tqdm(filepaths, f"Merging {level}-level taxonomic abundances"):
                id_sample = filepath.split("/")[-3]
                output[id_sample] = pd.read_csv(filepath, sep="\t", index_col=0).squeeze("columns")
        else:
            raise FileNotFoundError(f"Could not find any taxonomic_abundance.genomes.tsv.gz files in {profiling_directory}")
     
    # Genome clusters
    elif level == "genome_clusters":
        filepaths = glob.glob(f"{profiling_directory}/*/output/taxonomic_abundance.genome_clusters.tsv.gz")
        output = dict()
        if filepaths:
            for filepath in tqdm(filepaths, f"Merging {level}-level taxonomic abundances"):
                id_sample = filepath.split("/")[-3]
                output[id_sample] = pd.read_csv(filepath, sep="\t", index_col=0).squeeze("columns")
        else:
            raise FileNotFoundError(f"Could not find any taxonomic_abundance.genome_clusters.tsv.gz files in {profiling_directory}")
        
    X = pd.DataFrame(output).T
    missing_value_fill=pd.NA
    if fillna_with_zeros:
        X = X.fillna(0.0)
        missing_value_fill = 0.0
    if sparse:
        X = X.astype(pd.SparseDtype("float", missing_value_fill))
    return X

def merge_pathway_profiling_tables(profiling_directory:str, data_type:str, level="genomes", metric="number_of_reads", fillna_with_zeros:bool=False, sparse:bool=False):
    
    """
    merges sample-level {data_type} values from multiple samples into a single DataFrame.

    Parameters
    ----------
    profiling_directory : str
        Path to directory containing sample-level directories with output files.
    data_type : str
        Type of {level}-level data to merge. One of: {"feature_abundances", "feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio", "gene_abundances", "pathway_abundances"}
    level : str, optional
        Level of organization for {data_type}. One of {"genomes", "genome_cluster"}.
    metric : str, optional
        Metric to use for {data_type}. One of {"number_of_reads", "tpm", "coverage"}.
    fillna_with_zeros : bool, optional
        Whether to fill missing values with zeros. Default is False.
    sparse : bool, optional
        Whether to return a pd.Sparse type. Default is False. 
    Returns
    -------
    pd.DataFrame
        merged DataFrame with {data_type} values for each sample.

    Notes
    -----
    Will raise a ValueError if an invalid combination of arguments is provided, such as level="genome_cluster" and data_type="gene_abundances".
    
    Files:
    * feature_abundances.genome_clusters.tsv.gz
    * feature_abundances.genomes.tsv.gz
    * feature_prevalence-binary.genome_clusters.tsv.gz
    * feature_prevalence-binary.genomes.tsv.gz
    * feature_prevalence.genome_clusters.tsv.gz
    * feature_prevalence.genomes.tsv.gz
    * feature_prevalence-ratio.genome_clusters.tsv.gz
    * gene_abundances.genomes.tsv.gz
    * pathway_abundances.genome_clusters.tsv.gz
    * pathway_abundances.genomes.tsv.gz
    """

    check_argument_choice(
        query=data_type, 
        choices={"feature_abundances", "feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio", "gene_abundances", "pathway_abundances"},
        )
    check_argument_choice(
        query=level, 
        choices={"genomes", "genome_clusters"},
        )
    check_argument_choice(
        query=metric, 
        choices={"number_of_reads", "tpm", "coverage"},
        )

    illegal_conditions = [
        (level == "genome_cluster") and (data_type == "gene_abundances"),
        (level == "genomes") and (data_type == "feature_prevalence-ratio"),
        (data_type != "pathway_abundances") and (metric == "coverage"),
    ]
    
    if any(illegal_conditions):
        raise ValueError(f"Invalid combination of arguments: level={level}, data_type={data_type}, metric={metric}")
    
    # Merge tables to produce output
    filepaths = glob.glob(f"{profiling_directory}/*/output/{data_type}.{level}.tsv.gz")
    if filepaths:
        output = dict()
        # Abundance/Coverage
        if data_type in {"feature_abundances", "gene_abundances", "pathway_abundances"}:
            
            # Determine column name
            column = str(metric)
            if data_type in {"feature_abundances", "pathway_abundances"}:
                if metric != "coverage":
                    column = f"{metric}(scaled)"
            
            description = "Merging {}-level {} {} values".format(level, data_type.replace("_", " "), metric)
            for filepath in tqdm(filepaths, description):
                id_sample = filepath.split("/")[-3]
                df = pd.read_csv(filepath, sep="\t", index_col=[0,1])
                output[id_sample] = df[column]
                
        # Prevalence
        elif data_type in {"feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio"}:
            description = "Merging {}-level {} prevalence values".format(level, data_type.replace("_", " "))
            for filepath in tqdm(filepaths, description):
                id_sample = filepath.split("/")[-3]
                df = pd.read_csv(filepath, sep="\t", index_col=0)
                output[id_sample] = df.stack()
        X = pd.DataFrame(output).T
        
        sparse_dtype = "float"
        missing_value_fill = pd.NA
        if data_type == "feature_prevalence-binary":
            if fillna_with_zeros:
                X = X.fillna(0)
                sparse_dtype = "int"
                missing_value_fill = 0
        else:
            if fillna_with_zeros:
                X = X.fillna(0.0)
                missing_value_fill = 0.0
        if sparse:
            X = X.astype(pd.SparseDtype(sparse_dtype, missing_value_fill))
        return X
                
    else:
        raise FileNotFoundError(f"Could not find any {data_type}.{level}.tsv.gz files in {profiling_directory}")

                

