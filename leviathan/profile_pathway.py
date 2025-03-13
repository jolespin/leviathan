#!/usr/bin/env python
import sys
import os
import glob
from collections import defaultdict
from tqdm import tqdm
import pandas as pd
import numpy as np
import xarray as xr
# from memory_profiler import profile

from kegg_pathway_profiler.pathways import (
    pathway_coverage_wrapper,
)

from pyexeggutor import (
    format_bytes,
    RunShellCommand,
    check_argument_choice,
)
    
        
        
__program__ = os.path.split(sys.argv[0])[-1]


# Run Salmon quant (salmon quant --meta --libType A --index ${INDEX} -1 ${R1} -2 ${R2} --threads ${N_JOBS}  --minScoreFraction=0.87 --writeUnmappedNames)
def run_salmon_quant(logger, log_directory, salmon_executable, n_jobs, output_directory, index_directory, forward_reads, reverse_reads, minimum_score_fraction, salmon_quant_options):
    cmd = RunShellCommand(
        command=[
            salmon_executable,
            "quant",
            "--meta",
            "--libType",
            "A",
            "--threads",
            n_jobs,
            "--minScoreFraction",
            minimum_score_fraction,
            "--index",
            os.path.join(index_directory, "salmon_index"),
            "-1",
            forward_reads,
            "-2",
            reverse_reads,
            "--writeUnmappedNames",
            salmon_quant_options,
            "--output",
            output_directory,
            
        ],
        name="salmon_quant",
        validate_input_filepaths=[
            forward_reads,
            reverse_reads,
        ],
        validate_output_filepaths=[
            os.path.join(output_directory, "quant.sf"),
        ],
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

def reformat_gene_abundance(df_quant:pd.DataFrame, gene_to_data:dict):
    # Name    Length  EffectiveLength TPM     NumReads
    index = list()
    values = list()
    for id_gene, row in tqdm(df_quant.iterrows(), "Removing zero-abundance features"):
        abundance = row["NumReads"]
        if abundance > 0:
            id_genome = gene_to_data[id_gene]["id_genome"]
            tpm = row["TPM"]
            values.append([abundance, tpm])
            index.append((id_genome, id_gene))
    return pd.DataFrame(
        data=values,
        index=pd.MultiIndex.from_tuples(index, names=["id_genome", "id_gene"]),
        columns=[ "number_of_reads", "tpm"],
    )
    
def reformat_feature_abundance(df_gene_abundances:pd.DataFrame, gene_to_data:dict, split_feature_abundances:bool):
    feature_to_values = defaultdict(lambda: np.zeros(2, dtype=float))
    if split_feature_abundances:
        columns = ["number_of_reads(scaled)", "tpm(scaled)"]
        for (id_genome, id_gene), row in tqdm(df_gene_abundances.iterrows(), "Aggregating feature counts (Splitting abundances across features)"):
            abundance, tpm = row
            features = gene_to_data[id_gene]["features"]
            if features:
                number_of_features = len(features)
                tpm_scaled = tpm/number_of_features
                abundance_scaled = abundance/number_of_features
                for id_feature in features:
                    feature_to_values[(id_genome, id_feature)] += [abundance_scaled, tpm_scaled]
    else:
        columns = ["number_of_reads", "tpm"]
        for (id_genome, id_gene), row in tqdm(df_gene_abundances.iterrows(), "Aggregating feature counts"):
            tpm, abundance = row
            features = gene_to_data[id_gene]["features"]
            if features:
                number_of_features = len(features)
                for id_feature in features:
                    feature_to_values[(id_genome, id_feature)] += [abundance_scaled, tpm_scaled]

                    
    df_output = pd.DataFrame(
        data=feature_to_values,
        index=columns,
    ).T
    df_output.index.names = ["id_genome", "id_feature"]
    return df_output
    
def build_wide_feature_prevalence_matrix(df_feature_abundance:pd.DataFrame, threshold:float=0.0):
    # Index
    genomes = sorted(df_feature_abundance.index.get_level_values(0).unique())
    features = sorted(df_feature_abundance.index.get_level_values(1).unique())
    # Shape
    number_of_genomes = len(genomes)
    number_of_features = len(features)
    # Lookup
    genome_index_lookup = dict(zip(genomes, range(number_of_genomes)))
    feature_index_lookup = dict(zip(features, range(number_of_features)))
    # Zero-matrix
    prevalence_matrix = np.zeros((number_of_genomes, number_of_features), dtype=int)
    # Populate zero-matrix
    for (id_genome, id_feature), value in tqdm(df_feature_abundance.iloc[:,0].items(), total=df_feature_abundance.shape[0]):
        if value > threshold:
            i = genome_index_lookup[id_genome]
            j = feature_index_lookup[id_feature]
            prevalence_matrix[i,j] += 1
      
    return pd.DataFrame(
        data=prevalence_matrix,
        index=pd.Index(genomes, name="id_genome"),
        columns=pd.Index(features, name="id_feature"),
    )
                    
def build_feature_prevalence_dictionary(df_feature_prevalence_binary:pd.DataFrame):
    genome_to_features = dict()
    for id_genome, prevalence in df_feature_prevalence_binary.iterrows():
        genome_to_features[id_genome] = set(prevalence[lambda x: x > 0].index)
    return genome_to_features

def build_feature_pathway_dictionary(pathway_to_data:dict):
    feature_to_pathways = defaultdict(set)
    for id_pathway, data in pathway_to_data.items():
        for id_feature in data["ko_to_nodes"]:
            feature_to_pathways[id_feature].add(id_pathway)
    return feature_to_pathways
            
        
def calculate_pathway_coverage(genome_to_features:dict, pathway_to_data:dict):
    # Coverage
    coverages = dict()
    # Calculate pathway coverage for all genomes
    for id_genome, evaluation_features in genome_to_features.items():
        # Calculate pathway coverage for all pathways based on evaluation feature set
        pathway_to_results = pathway_coverage_wrapper(
            evaluation_kos=evaluation_features,
            database=pathway_to_data,
            progressbar_description=f"Calculating pathway coverage: {id_genome}",
        )

        # Coverage
        for id_pathway, results in pathway_to_results.items():
            coverages[(id_genome, id_pathway)] = results["coverage"]
    
    return coverages

def aggregate_pathway_abundance_and_append_coverage(df_feature_abundance:pd.DataFrame, feature_to_pathways:dict, coverages:dict, index_names = ["id_genome", "id_pathway"]):
    abundance_matrix = defaultdict(lambda: np.zeros(3, dtype=float))
    for (id_genome, id_feature), values in df_feature_abundance.iterrows():
        for id_pathway in feature_to_pathways[id_feature]:
            abundance_matrix[(id_genome, id_pathway)][:-1] += values
    for (id_genome, id_pathway) in abundance_matrix:
        coverage = coverages.get((id_genome, id_pathway), 0.0)
        abundance_matrix[(id_genome, id_pathway)] += [0.0, 0.0, coverage]
            
    df_output = pd.DataFrame(abundance_matrix, index=df_feature_abundance.columns.tolist() + ["coverage"]).T
    df_output.index.names = index_names
    return df_output

def aggregate_feature_abundance_for_clusters(df_feature_abundance:pd.DataFrame, genome_to_data:dict):
    def f(x):
        id_genome, id_feature = x
        return (genome_to_data[id_genome]["id_genome_cluster"], id_feature)
    df_output = df_feature_abundance.groupby(f).sum()
    df_output.index = pd.MultiIndex.from_tuples(df_output.index, names=["id_genome_cluster", "id_feature"])
    return df_output

def merge_pathway_profiling_tables_as_pandas(profiling_directory:str, data_type:str, level="genomes", metric="number_of_reads", fillna_with_zeros:bool=False, sparse:bool=False):
    
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
            description = "Merging {}-level {} values".format(level, data_type.replace("_", " "))
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

def merge_pathway_profiling_tables_as_xarray(profiling_directory:str, data_type:str, level="genomes", metric="number_of_reads", fillna_with_zeros:bool=False):
    
    """
    merges sample-level {data_type} values from multiple samples into a single DataFrame.

    Parameters
    ----------
    profiling_directory : str
        Path to directory containing sample-level directories with output files.
    data_type : str
        Type of {level}-level data to merge. One of: {"feature_abundances", "feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio", "pathway_abundances"}
    level : str, optional
        Level of organization for {data_type}. One of {"genomes", "genome_cluster"}.
    metric : str, optional
        Metric to use for {data_type}. One of {"number_of_reads", "tpm", "coverage"}.
    fillna_with_zeros : bool, optional
        Whether to fill missing values with zeros. Default is False.

    Returns
    -------
    xr.DataArray
        Merged xr.DataArray with dims: (samples, {level}, features)

    Notes
    -----
    Will raise a ValueError if an invalid combination of arguments is provided, such as level="genomes" and data_type="feature_prevalence-ratio".
    
    Files:
    * feature_abundances.genome_clusters.tsv.gz
    * feature_abundances.genomes.tsv.gz
    * feature_prevalence-binary.genome_clusters.tsv.gz
    * feature_prevalence-binary.genomes.tsv.gz
    * feature_prevalence.genome_clusters.tsv.gz
    * feature_prevalence.genomes.tsv.gz
    * feature_prevalence-ratio.genome_clusters.tsv.gz
    * pathway_abundances.genome_clusters.tsv.gz
    * pathway_abundances.genomes.tsv.gz
    
    # Not supported: 
    * gene_abundances.genomes.tsv.gz

    """

    check_argument_choice(
        query=data_type, 
        choices={"feature_abundances", "feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio",  "pathway_abundances"}, # "gene_abundances",
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
        # (level == "genome_cluster") and (data_type == "gene_abundances"),
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
        if data_type in {"feature_abundances",  "pathway_abundances"}:
            name = (data_type, level, metric)
            variable_label = data_type.split("_")[0] + "s"

            # Determine column name
            column = str(metric)
            if data_type in {"feature_abundances", "pathway_abundances"}:
                if metric != "coverage":
                    column = f"{metric}(scaled)"
            
            description = "Merging {}-level {} {} values".format(level, data_type.replace("_", " "), metric)
            for filepath in tqdm(filepaths, description):
                id_sample = filepath.split("/")[-3]
                df = pd.read_csv(filepath, sep="\t", index_col=[0,1])
                df = df[column].unstack()

                output[id_sample] = xr.DataArray(data = df.values, coords = [(level, df.index), (variable_label, df.columns)])
                del df
                
        # Prevalence
        elif data_type in {"feature_prevalence", "feature_prevalence-binary", "feature_prevalence-ratio"}:
            name = (data_type, level)
            description = "Merging {}-level {} values".format(level, data_type.replace("_", " "))
            for filepath in tqdm(filepaths, description):
                id_sample = filepath.split("/")[-3]
                df = pd.read_csv(filepath, sep="\t", index_col=0)
                variable_label = data_type.split("_")[0] + "s"
                output[id_sample] = xr.DataArray(data = df.values, coords = [(level, df.index), (variable_label, df.columns)])
        X = xr.concat(output.values(), dim="samples")
        X["samples"] = list(output.keys())
        
        
        if data_type in {"feature_prevalence-binary", "feature_prevalence"}:
            X = X.astype(np.int8)
            if fillna_with_zeros:
                X = X.fillna(0)
        else:
            X = X.astype(np.float32)
            if fillna_with_zeros:
                X = X.fillna(0.0)
        return X
                
    else:
        raise FileNotFoundError(f"Could not find any {data_type}.{level}.tsv.gz files in {profiling_directory}")

