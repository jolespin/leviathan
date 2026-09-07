# Walkthrough: End-to-End

**Working Directory:** `test/commands/`

Please see [docs](../docs/OUTPUTS.md) for descriptions of outputs.

The test scripts use a shared `config.sh` to toggle between pangenome modes (`with_pangenomes` or `no_pangenomes`). You can also override via environment variable: `MANIFEST_TYPE=no_pangenomes bash run_workflow.sh`.

## 1. Download CAMI-II_Marine_n-100
The dataset provided here is a subset of the `CAMI-II` dataset called `CAMI-II_Marine_n-100` used in the benchmarking for `Leviathan`.  Currently, the full database is too large to host for free on `Zenodo` or `FigShare` so I'm providing a small toy dataset for testing. 

```bash
# Download and extract the CAMI-II Marine toy dataset
url="https://zenodo.org/records/17783338/files/CAMI-II_Marine_n-100.tar.gz?download=1"
dataset_directory="../datasets/"
curl -L "${url}" | tar -xz -C ${dataset_directory}
```

## 2. Build a manifest file from the genomics assets

If you ran [VEBA](https://github.com/jolespin/veba) you can just use `compile-manifest-from-veba.py`.

```bash
#!/usr/bin/env bash
job_name="leviathan-manifest"

# Manifest type: "with_pangenomes" or "no_pangenomes"
manifest_type="with_pangenomes"

# Directories
input_directory="../inputs/${manifest_type}"
reference_directory="${input_directory}/references"
veba_directory="../../Analysis/veba_output/"

# Output manifest
manifest="manifest.${manifest_type}.tsv.gz"

compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest} --veba_major_version 2
```

If not, you can easily use `Leviathan` by building your own manifest table. 

For the data you just downloaded, you can use the pre-built manifest files `manifest.with_pangenomes.tsv.gz` (recommended) or `manifest.no_pangenomes.tsv.gz` which is the same table just missing column 4.

```python
import os
import pandas as pd
import glob

manifest = dict()
cami_directory="../datasets/CAMI-II_Marine_n-100"
for sample_directory in glob.glob(f"{cami_directory}/sample_*"):
    id_sample = sample_directory.split("/")[-1]
    genome_to_pangenome = pd.read_csv(f"{sample_directory}/genome_to_pangenome.tsv.gz", sep="\t", index_col=0, header=None).iloc[:,0]
    for id_genome, id_pangenome in genome_to_pangenome.items():
        manifest[id_genome] = {
            "assembly":f"{cami_directory}/{id_sample}/genomes/{id_genome}.fa.gz",
            "cds":f"{cami_directory}/{id_sample}/genomes/{id_genome}.ffn.gz",
            "id_pangenome":id_pangenome,
        }
df_manifest = pd.DataFrame(manifest).T
df_manifest.to_csv("manifest.with_pangenomes.tsv.gz", sep="\t", header=None)
```

## 3. Preprocess the files for building an index
This step is light-weight and produces the following files: 
* `cds.fasta.gz` - All CDS sequences for all genomes (cannot have duplicate ids)
* `feature_mapping.tsv.gz` - Feature mapping table `[id_gene, set(features), id_genome] [Optional:id_pangenome]`
* `genomes.tsv.gz` - Filepath of all the genomes
* `md5hashes.json` - md5 hash for all files for reproducibility

For genome clustering into pangenomes, I recommend using the [cluster module of VEBA](https://github.com/jolespin/veba/blob/main/walkthroughs/docs/end-to-end_metagenomics.md#9-cluster-genomes-and-proteins) which will soon be a standalone method. 

```bash
#!/usr/bin/env bash
job_name="leviathan-preprocess"

# Manifest type: "with_pangenomes" or "no_pangenomes"
manifest_type="with_pangenomes"

# Directories
input_directory="../inputs/${manifest_type}"
reference_directory="${input_directory}/references"
dataset_directory="../datasets/CAMI-II_Marine_n-100/"

# Inputs
manifest="manifest.${manifest_type}.tsv.gz"
annotations="${dataset_directory}/analysis/pykofamsearch_output.pathways.tsv.gz"

# Run
leviathan-preprocess.py -i ${manifest} -a ${annotations} -o ${reference_directory} --annotation_format pykofamsearch 2> logs/${job_name}.err 1> logs/${job_name}.out
```

## 4. Build the index 
This step is essential and does the following: 
* Builds `Sylph` database needed for taxonomic profiling
* Builds `Salmon` database needed for pathway profiling
* Checks all proteins, genomes, and pangenomes
* Builds mapping objects that are used for compiling the results

The index module produces the following files/directories: 
* `config.json` - All the necessary run information
* `database/` - Gzipped Python pickle objects and the `Sylph` database
* `logs/` - All the logs for building the database
* `md5hashes.json` - md5 hash for all files for reproducibility
* `salmon_index/` - The index used for pathway profiling

```bash
#!/usr/bin/env bash
job_name="leviathan-index"

# Manifest type: "with_pangenomes" or "no_pangenomes"
manifest_type="with_pangenomes"

# Datasets
dataset_directory="../datasets/CAMI-II_Marine_n-100/"

# Databases
mkdir -p ../databases/
pathway_database="../databases/KEGG-Pathway-Profiler/database.pkl.gz"

# Directories
input_directory="../inputs/${manifest_type}"
reference_directory="${input_directory}/references"
index_directory="${reference_directory}/index/"

# Inputs
fasta="${reference_directory}/cds.fasta.gz"
feature_mapping="${reference_directory}/feature_mapping.tsv.gz"
genomes="${reference_directory}/genomes.tsv.gz"

# Fetch KEGG Pathway database
build-pathway-database.py --ebi latest -d ${pathway_database}

# Run
leviathan-index.py -f ${fasta} -m ${feature_mapping} -g ${genomes} -d ${index_directory} -p=-1 --pathway_database ${pathway_database} 2> logs/${job_name}.err > logs/${job_name}.out
```

The `config.json` should look like this: 
```json
{
    "fasta_filepath": "../inputs/with_pangenomes/references/cds.fasta.gz",
    "feature_mapping_filepath": "../inputs/with_pangenomes/references/feature_mapping.tsv.gz",
    "contains_genome_cluster_mapping": true,
    "contains_genome_filepaths": true,
    "timestamp": "the time you ran this",
    "number_of_genes": 38726,
    "number_of_features": 1390,
    "feature_type_is_kegg_ortholog": true,
    "number_of_genomes": 93,
    "contains_pathways": true,
    "number_of_features_in_pathways": 2791,
    "number_of_features_overlapping_in_pathways": 1390
}
```

> [!Note:] 
> Ths reason why there are 93 genomes and not 100 genomes is because some of the genomes did not contain any features we were using here (in this case, KOfam).

## 5. Run taxonomic profiling
Now that the database is built and configured, we can start pouring water through the system.  First let's do taxonomic profiling which is essentially a wrapper around `Sylph` that reformats the output data and aggregates with respect to genome clusters.

Since `Leviathan` is designed to run each sample separately, let's create a file of commands that we can pipe into `GNU Parallel`

```bash
#!/usr/bin/env bash

# Manifest type: "with_pangenomes" or "no_pangenomes"
manifest_type="with_pangenomes"

rm -f commands.leviathan-profile-taxonomy.list

# Directories
input_directory="../inputs/${manifest_type}"
dataset_directory="../datasets/CAMI-II_Marine_n-100"
output_directory="../outputs/${manifest_type}"

# Input/output paths
index_directory="${input_directory}/references/index/"
profiling_directory="${output_directory}/profiling"
mkdir -p ${profiling_directory}

# Output format
table_format="parquet"

# Generate one command per sample
for id in $(cat identifiers.list);
do
	job_name="leviathan-profile-taxonomy__${id}"
	echo $job_name
	r1="${dataset_directory}/${id}/reads/reads_1.fastq.gz"
	r2="${dataset_directory}/${id}/reads/reads_2.fastq.gz"
	cmd="leviathan-profile-taxonomy.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=2 -o ${profiling_directory}/taxonomy/ -f ${table_format}"
	echo $cmd >> commands.leviathan-profile-taxonomy.list
done
```

Now we have the commands in `commands.leviathan-profile-taxonomy.list` we can use `GNU Parallel` assuming you have it installed (e.g., `brew install parallel`, `sudo apt-get install parallel`, `mamba install -c conda-forge parallel`)

You may need to adjust `n_concurrent_tasks` depending on your available CPU cores.

```
n_concurrent_tasks=4
cat commands.leviathan-profile-taxonomy.list | parallel -j ${n_concurrent_tasks}
```

This will produce a directory of files for each sample similar to the output structure of [VEBA](https://github.com/jolespin/veba) and most of my other pipelines.

The files you need are in `../outputs/${manifest_type}/profiling/taxonomy/*/output` where `*` will be the samples (e.g., `sample_0`, `sample_1`, `...`, `sample_8`).  

The file names are self-explanatory:

* sequence_abundance.genome_clusters.parquet
* sequence_abundance.genomes.parquet
* sylph_profile.tsv.gz
* taxonomic_abundance.genome_clusters.parquet
* taxonomic_abundance.genomes.parquet

## 6. Run pathway profiling
Now let's move on to the actual purpose of the tool which is pathway profiling.  You can use any feature type (e.g., KEGG, Pfam, PGAP, MetaCyc) but currently only KEGG is supported for full pathway analysis because of [KEGG-Pathway-Profiler](https://github.com/jolespin/kegg_pathway_profiler).

We are going to build the commands file in the same way as we did for the taxonomy: 

```bash
#!/usr/bin/env bash

# Manifest type: "with_pangenomes" or "no_pangenomes"
manifest_type="with_pangenomes"

rm -f commands.leviathan-profile-pathway.list

# Directories
input_directory="../inputs/${manifest_type}"
dataset_directory="../datasets/CAMI-II_Marine_n-100"
output_directory="../outputs/${manifest_type}"

# Input/output paths
index_directory="${input_directory}/references/index/"
profiling_directory="${output_directory}/profiling"
mkdir -p ${profiling_directory}

# Output format
table_format="parquet"

# Generate one command per sample
for id in $(cat identifiers.list);
do
	job_name="leviathan-profile-pathway__${id}"
	echo $job_name
	r1="${dataset_directory}/${id}/reads/reads_1.fastq.gz"
	r2="${dataset_directory}/${id}/reads/reads_2.fastq.gz"
	cmd="leviathan-profile-pathway.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=2 -o ${profiling_directory}/pathway/ -f ${table_format}"
	echo $cmd >> commands.leviathan-profile-pathway.list
done
```

Run jobs in parallel: 

```
n_concurrent_tasks=4
cat commands.leviathan-profile-pathway.list | parallel -j ${n_concurrent_tasks}
```

The files you need are in `../outputs/${manifest_type}/profiling/pathway/*/output`.

Here are the output files:

* feature_abundances.genome_clusters.parquet
* feature_abundances.genomes.parquet
* feature_prevalence-binary.genome_clusters.parquet
* feature_prevalence-binary.genomes.parquet
* feature_prevalence-ratio.genome_clusters.parquet
* feature_prevalence.genome_clusters.parquet
* feature_prevalence.genomes.parquet
* gene_abundances.genomes.parquet
* pathway_abundances.genome_clusters.parquet
* pathway_abundances.genomes.parquet


## 7. Merge sample-specific results into a single dataset

You can analyze the `.parquet` files individually but it's often more efficient to index and perform analysis using the `NetCDF` objects through `Xarray` since they are designed for high-dimensional data unlike `Pandas` which is for 1D and 2D primarily. 

```bash
#!/usr/bin/env bash

# Manifest type: "with_pangenomes" or "no_pangenomes"
manifest_type="with_pangenomes"

# Directories
output_directory="../outputs/${manifest_type}"
profiling_directory="${output_directory}/profiling"
artifact_directory="${output_directory}/artifacts"

# Output format
job_name="leviathan-merge"
table_format="parquet"
taxonomy_directory="${profiling_directory}/taxonomy/"
pathway_directory="${profiling_directory}/pathway/"

# Run
leviathan-merge.py -t ${taxonomy_directory} -p ${pathway_directory} -o ${artifact_directory} -f ${table_format} 2> logs/${job_name}.err 1> logs/${job_name}.out
```

Here are the output files:
* feature.genome_clusters.nc
* feature.genomes.nc
* pathway.genome_clusters.nc
* pathway.genomes.nc
* taxonomic_abundances.genome_clusters.nc
* taxonomic_abundances.genomes.nc

## 8. Analyze results
Please refer to the [docs](../docs/MODULES.md) for how to read and analyze outputs.
