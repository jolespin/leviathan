#!/usr/bin/env python
import sys, os
from tqdm import tqdm
from collections import defaultdict    
from pyexeggutor import (
    open_file_reader,
)

# Annotations
def read_annotations(path:str, format="pykofamsearch"):
    choices = {"pykofamsearch", "pyhmmsearch", "veba-pfam","veba-kofam","veba-cazy","veba-uniref", "veba-mibig", "veba-vfdb","veba-amr", "custom"}
    if format not in choices:
        raise KeyError(f"format must be in {choices}")
    
    if format in {"pykofamsearch", "pyhmmsearch", "custom"}:
        f_annotations = open_file_reader(path)

        gene_to_features = defaultdict(set)    
        if format != "custom":
            next(f_annotations)
        for line in tqdm(f_annotations, desc="Extracting feature annotations"):
            line = line.strip()
            if line:
                id_gene, id_feature, *extra = line.split("\t")
                gene_to_features[id_gene].add(id_feature)
        f_annotations.close()
    else:
        from pandas import read_csv
        df_annotations = read_csv(path, sep="\t", index_col=0, header=[0,1])
        
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