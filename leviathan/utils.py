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


                

