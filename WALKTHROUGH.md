# Walkthrough

**Working Directory:** `test/commands/`

Please see main [README.md](../README.md) for descriptions of outputs.

## 1. Download CAMI-II_Marine_n-100
The dataset provided here is a subset of the `CAMI-II` dataset called `CAMI-II_Marine_n-100` used in the benchmarking for `Leviathan`.  Currently, the full database is too large to host for free on `Zenodo` or `FigShare` so I'm providing a small toy dataset for testing. 

```
url="https://zenodo.org/records/17783338/files/CAMI-II_Marine_n-100.tar.gz?download=1"
database_directory="../databases/"
curl -L "${url}" | tar -xz -C ${database_directory}
```

## 2. Build a manifest file from the genomics assets

If you ran [VEBA](https://github.com/jolespin/veba) you can just use `compile-manifest-from-veba.py`.

```bash
#!/usr/bin/env bash
job_name="leviathan-manifest"
working_directory="../working"
reference_directory="${working_directory}/references"
veba_directory="../../Analysis/veba_output/"
manifest="${reference_directory}/manifest.tsv"
compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest} 2> logs/${job_name}.err 1> logs/${job_name}.out
```

If not you can easily use `Leviathan` by building your own manifest table. 

For the data you just downloaded, you can the pre-built manifest files `manifest.with_pangenomes.tsv.gz` (recommended) or `manifest.no_pangenomes.tsv.gz` which is the same table just missing column 4.

```python
import os
import pandas as pd
import glob

manifest = dict()
cami_directory="../databases/CAMI-II_Marine_n-100"
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
df_manifest.to_csv("manifest.tsv.gz", sep="\t", header=None)
```

## 3. Preprocess the files for building an index
This step is light-weight and produces the following files: 
* cds.fasta.gz - All CDS sequences for all genomes (cannot have duplicate ids)
* feature_mapping.tsv.gz - Feature mapping table `[id_gene, set(features), id_genome] [Optional:id_pangenome]`
* genomes.tsv.gz - Filepath of all the genomes
* md5hashes.json - md5 hash for all files for reproducibility

For genome clustering into pangenomes, I recommend using the [cluster module of VEBA](https://github.com/jolespin/veba/blob/main/walkthroughs/docs/end-to-end_metagenomics.md#9-cluster-genomes-and-proteins) which will soon be a standalone method. 

```bash
#!/usr/bin/env bash
job_name="leviathan-preprocess"
working_directory="../working/"
reference_directory="${working_directory}/references"
manifest="manifest.tsv.gz"
annotations="../databases/CAMI-II_Marine_n-100/analysis/pykofamsearch_output.pathways.tsv.gz"
leviathan-preprocess.py -i ${manifest} -a ${annotations} -o ${reference_directory} --annotation_format pykofamsearch 2> logs/${job_name}.err 1> logs/${job_name}.out
```

## 4. Build the index 
This step is essential and does the following: 
* Builds `Sylph` database needed for taxonomic profiling
* Builds `Salmon` database needed for pathway profiling
* Checks all proteins, genomes, and pangenomes
* Builds mapping objects that are used for compiling the results

The index module produces the following files/directories: 
* config.json - All the necessary run information
* database - Gzipped Python pickle objects and the `Sylph` database
* logs - All the logs for building the database
* salmon_index - The index used for pathway profiling

logs
md5hashes.json
salmon_index
```bash
#!/usr/bin/env bash
job_name="leviathan-index"

# Databases
database_directory="../databases/CAMI-II_Marine_n-100"
pathway_database="${HOME}/Databases/KEGG-Pathway-Profiler/database.pkl.gz"

# Output Directories
working_directory="../working"
reference_directory="${working_directory}/references"
index_directory="${reference_directory}/index/"

# Inputs
reference_directory="${working_directory}/references"
fasta="${reference_directory}/cds.fasta.gz"
feature_mapping="${reference_directory}/feature_mapping.tsv.gz"
genomes="${reference_directory}/genomes.tsv.gz"

# Run
leviathan-index.py -f ${fasta} -m ${feature_mapping} -g ${genomes} -d ${index_directory} -p=-1 --pathway_database ${pathway_database} 2> logs/${job_name}.err > logs/${job_name}.out
```

The `config.json` should look like this: 
```json
{
    "fasta_filepath": "../working/references/cds.fasta.gz",
    "feature_mapping_filepath": "../working/references/feature_mapping.tsv.gz",
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
rm -f commands.leviathan-profile-taxonomy.list
working_directory="../working"
database_directory="../databases/CAMI-II_Marine_n-100"

index_directory="${working_directory}/references/index/"
profiling_directory="${working_directory}/leviathan_output/profiling"
mkdir -p ${profiling_directory}

for id in $(cat identifiers.list);
do
	job_name="leviathan-profile-taxonomy__${id}"
	echo $job_name
	r1="${database_directory}/${id}/reads/reads_1.fastq.gz"
	r2="${database_directory}/${id}/reads/reads_2.fastq.gz"
	cmd="leviathan-profile-taxonomy.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=2 -o ${profiling_directory}/taxonomy/  2> logs/${job_name}.err > logs/${job_name}.out"
	echo $cmd >> commands.leviathan-profile-taxonomy.list
done
```

Now we have the commands in `commands.leviathan-profile-taxonomy.list` we can use `GNU Parallel` assuming you have it installed (e.g., `brew install parallel`, `sudo apt-get install parallel`, `mamba install -c conda-forge parallel`)

I have more than 9 CPU cores so I will run all 9 jobs at once but you may need to drop this to `4` or so. 

```
n_concurrent_jobs=9
cat commands.leviathan-profile-taxonomy.list | parallel -j ${n_concurrent_jobs}
```

This will produce a directory of files for each sample similar to the output structure of [VEBA](https://github.com/jolespin/veba) and most of my other pipelines.

The files you need are in `../working/leviathan_output/profiling/taxonomy/*/output` where `*` will be the samples (e.g., `sample_0`, `sample_1`, `...`, `sample_8`).  

The file names are self-explanatory:

* sequence_abundance.genome_clusters.parquet
* sequence_abundance.genomes.parquet
* sylph_profile.tsv.gz
* taxonomic_abundance.genome_clusters.parquet
* taxonomic_abundance.genomes.parquet

## 5. Run pathway profiling
Now let's move on to the actual purpose of the tool which is pathway profiling.  You can use any feature type (e.g., KEGG, Pfam, PGAP, MetaCyc) but currently only KEGG is supported for full pathway analysis because of [KEGG-Pathway-Profiler](https://github.com/jolespin/kegg_pathway_profiler).

We are going to build the commands file in the same way as we did for the taxonomy: 

```bash
#!/usr/bin/env bash
rm -f commands.leviathan-profile-pathway.list
working_directory="../working"
database_directory="../databases/CAMI-II_Marine_n-100"

index_directory="${working_directory}/references/index/"
profiling_directory="${working_directory}/leviathan_output/profiling"
mkdir -p ${profiling_directory}

for id in $(cat identifiers.list);
do
	job_name="leviathan-profile-pathway__${id}"
	echo $job_name
	r1="${database_directory}/${id}/reads/reads_1.fastq.gz"
	r2="${database_directory}/${id}/reads/reads_2.fastq.gz"
	cmd="leviathan-profile-pathway.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=2 -o ${profiling_directory}/pathway/  2> logs/${job_name}.err > logs/${job_name}.out"
	echo $cmd >> commands.leviathan-profile-pathway.list
done
```

Run jobs in parallel: 

```
n_concurrent_jobs=9
cat commands.leviathan-profile-pathway.list | parallel -j ${n_concurrent_jobs}
```

The files you need are in `../working/leviathan_output/profiling/pathway/*/output`.


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


## 6. Merge sample-specific results into a single dataset

You can analyze the `.parquet` files individually but it's often more efficient to index and perform analysis using the `NetCDF` objects through `Xarray` since they are designed for high-dimensional data unlike `Pandas` which is for 1D and 2D primarily. 

```bash
#!/usr/bin/env bash
working_directory="../working"
profiling_directory="${working_directory}/leviathan_output/profiling"
artifact_directory="${working_directory}/leviathan_output/artifacts"
job_name="leviathan-merge"
leviathan-merge.py -t ${profiling_directory}/taxonomy/ -p ${profiling_directory}/pathway/ -o ${artifact_directory} 2> logs/${job_name}.err 1> logs/${job_name}.out
```

Here are the output files:
* feature.genome_clusters.nc
* feature.genomes.nc
* pathway.genome_clusters.nc
* pathway.genomes.nc
* taxonomic_abundances.genome_clusters.nc
* taxonomic_abundances.genomes.nc

## 7. Reading output files
### 7a. Reading Parquet files with Pandas
```python
!pip install pyarrow
df = pd.read_parquet("path/to/file.parquet")
```

### 7b. Reading NetCDF files with Xarray
> [!NOTE]
> To load `.nc` files you must have `h5netcdf` installed before `xarray` is loaded
```python
!pip install xarray h5netcdf
import xarray as xr

# Taxonomic abundances for genomes
ds_taxonomic = xr.open_dataset("leviathan_output/artifacts/taxonomic_abundances.genomes.nc")
ds_taxonomic

<xarray.Dataset> Size: 3kB
Dimensions:               (samples: 4, genomes: 23)
Coordinates:
  * samples               (samples) <U2 32B 'S3' 'S4' 'S1' 'S2'
  * genomes               (genomes) <U26 2kB 'S1__BINETTE__P.1__bin_210' ... ...
Data variables:
    taxonomic_abundances  (samples, genomes) float32 368B ...
    sequence_abundances   (samples, genomes) float32 368B ...

# Pathway abundances and coverage for genome clusters
ds_pathway = xr.open_dataset("leviathan_output/artifacts/pathway.genome_clusters.nc")
ds_pathway
<xarray.Dataset> Size: 276kB
Dimensions:          (genome_clusters: 19, pathways: 292, samples: 4)
Coordinates:
  * genome_clusters  (genome_clusters) <U37 3kB 'ESLC-a2a3ed2541a4e0cbd4acd3a...
  * pathways         (pathways) <U6 7kB 'M00001' 'M00002' ... 'M00982' 'M00983'
  * samples          (samples) <U2 32B 'S3' 'S4' 'S1' 'S2'
Data variables:
    number_of_reads  (samples, genome_clusters, pathways) float32 89kB ...
    tpm              (samples, genome_clusters, pathways) float32 89kB ...
    coverage         (samples, genome_clusters, pathways) float32 89kB ...

```
### 7c. Filtering functional profiling results with taxonomy gate
```python
# Load taxonomic profiling
ds_taxonomic = xr.open_dataset("leviathan_output/artifacts/taxonomic_abundances.genome_clusters.nc")

# Load functional profiling
ds_pathway = xr.open_dataset("leviathan_output/artifacts/pathway.genome_clusters.nc")

# Get (pan)genomes to retain from taxonomic abundances
minimum_samples_detected = 2
retained_organisms = (ds_taxonomic["taxonomic_abundances"].to_pandas() > 0).sum(axis=0)[lambda x: x >= minimum_samples_detected].index

# Filter functional profiling with taxonomic abundance gate
ds_pathway_filtered = ds_pathway.sel(genome_clusters=retained_organisms)
```


### 7d. Reformatting Xarray NetCDF files into Pandas DataFrames
```python
# Load pathway abundances
ds_pathway = xr.open_dataset("leviathan_output/artifacts/pathway.genome_clusters.nc")

# Subset counts and coverage data
X_counts = ds_pathway["tpm"].stack(cols=["genome_clusters", "pathways"]).to_pandas().fillna(0) # Normalized
# X_counts = ds_pathway["number_of_reads"].stack(cols=["genome_clusters", "pathways"]).to_pandas().fillna(0) # Raw

X_coverage = ds_pathway["coverage"].stack(cols=["genome_clusters", "pathways"]).to_pandas().fillna(0)
assert np.all(X_counts.columns == X_coverage.columns)
n_samples, m_features = X_coverage.shape

# Set filtering thresholds 
# For more implentation example:
# Josh L Espinoza, Manolito Torralba, Pamela Leong, Richard Saffery, Michelle Bockmann, Claire Kuelbs, Suren Singh, Toby Hughes, Jeffrey M Craig, Karen E Nelson, Chris L Dupont, Differential network analysis of oral microbiome metatranscriptomes identifies community scale metabolic restructuring in dental caries, PNAS Nexus, Volume 1, Issue 5, November 2022, pgac239, https://doi.org/10.1093/pnasnexus/pgac239
tol_coverage = 0.75 # Only consider modules that are 75% complete in at least 50% of the samples
tol_prevalence = 0.5 # You may need to adjust these depending on your analysis (e.g., 50% complete in at least 25% of the samples)
n_samples_for_prevalence = tol_prevalence*n_samples

# Subet
features_passed_qc = (X_coverage > tol_coverage).sum(axis=0)[lambda x: x > n_samples_for_prevalence].index
X_counts = X_counts.loc[:,features_passed_qc]
X_coverage = X_coverage.loc[:,features_passed_qc]

# Downstream analysis with filtered `X_counts`
```

### 7d. Selecting coverage `prevalence` cutoff

```python
import compositional as coda
coda.plot_prevalence(X_coverage > tol_coverage, style="ggplot")

# Find where the curve drops off and cut there
```


## Utility
### Downloading fastq from SRA
If you want to use on samples from SRA, you can download them like this:

#### Option 1: `xsra` (faster)
##### Install `cargo`
```
curl https://sh.rustup.rs -sSf | sh

# Initialize
. "$HOME/.cargo/env"            # For sh/bash/zsh/ash/dash/pdksh
```

##### Install `xsra`
Confirm that `cmake` is installed (e.g., `brew install cmake` or `sudo apt-get install cmake` or `mamba install -c conda-forge cmake` or )
```
cargo install xsra
```

##### Download Fastq
```
n_threads=14
fastq_directory="../fastq"
mkdir -p ${fastq_directory}
for id in $(cat ../identifiers.list);
do
    xsra dump \
    -o ${fastq_directory} \
    -c g \
    -s \
    --prefix ${id}_ \
    -T ${n_threads} \
    ${id}
done
```
##### Relabel Files
This step will be deprecated eventually given [xsra issue/#54](https://github.com/ArcInstitute/xsra/issues/54)

```
for id in $(cat ../identifiers.list);
do
    mv ${fastq_directory}/${id}_0.fq.gz ${fastq_directory}/${id}_1.fastq.gz 
    mv ${fastq_directory}/${id}_1.fq.gz ${fastq_directory}/${id}_2.fastq.gz 
done
```

#### Option 2: `kingfisher` (easier for now)
##### Install `kingfisher`
```
mamba activate leviathan
mamba install -c bioconda kingfisher
```

##### Download Fastq

```
n_threads=14
fastq_directory="../fastq"
mkdir -p ${fastq_directory}
for id in $(cat ../identifiers.list);
do
    kingfisher get \
    -r ${id} \
    --output-directory  ${fastq_directory} \
    -m aws-http \
    -f fastq.gz

done
```








