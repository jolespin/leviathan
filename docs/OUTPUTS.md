# Outputs

## Descriptions
### Sample Specific
#### Taxonomy profiles
* Examples: 
    - Genome = Metagenome-assembled genome (MAG)
    - Genome cluster = ANI ≥ 95% & Alignment Fraction ≥ 50%

##### Taxonomic abundances - Relative abundance of a genome/genome-cluster within a sample
 * `taxonomic_abundance.genome_clusters.[parquet|tsv.gz]` - Genome-cluster-level taxonomic relative abundance profiles
 * `taxonomic_abundance.genomes.[parquet|tsv.gz]` - Genome-level taxonomic relative abundance profiles

**Note:** `Sylph` is run with `--estimate-unknown` so relative abundances do not sum to 100% and the remaining % represents the unassigned reads.

#### Functional profiles

* Examples:
    - Feature = KEGG ortholog
    - Pathway = KEGG module

##### Feature abundances - The (normalized) abundance of a feature relative to a genome/genome-cluster
 * `feature_abundances.genome_clusters.number_of_reads.[parquet|tsv.gz]` - Feature abundances for each genome cluster (number of reads aligned)
 * `feature_abundances.genome_clusters.tpm.[parquet|tsv.gz]` - Feature abundances for each genome cluster (TPM normalized abundances)
 * `feature_abundances.genomes.number_of_reads.[parquet|tsv.gz]` - Feature abundances for each genome (number of reads aligned)
 * `feature_abundances.genomes.tpm.[parquet|tsv.gz]` - Feature abundances for each genome (TPM normalized abundances)

##### Feature prevalence - The number of genome/genome-clusters where a feature is detected
 * `feature_prevalence-binary.genome_clusters.[parquet|tsv.gz]` - Presence/absence of feature relative to genome clusters
 * `feature_prevalence-binary.genomes.[parquet|tsv.gz]` - Presence/absence of feature relative to genomes
 * `feature_prevalence-ratio.genome_clusters.[parquet|tsv.gz]` - Ratio of genomes within a genome cluster with feature detected
 * `feature_prevalence.genome_clusters.[parquet|tsv.gz]` - The count of uniques that correspond to the features relative to the genome clusters
 * `feature_prevalence.genomes.[parquet|tsv.gz]` - The count of uniques that correspond to the features relative to the genomes

##### Gene abundances - The abundance of individual genes within genome
 * `gene_abundances.genomes.number_of_reads.[parquet|tsv.gz]` - Number of reads aligned to a gene within a genome
 * `gene_abundances.genomes.tpm.[parquet|tsv.gz]` - TPM normalized abundance of reads aligned to a gene within a genome

##### Pathway abundances - Pathway abundances for a genome and genome-cluster

 * `pathway_abundances.genome_clusters.coverage.[parquet|tsv.gz]` - Pathway coverage (i.e., pathway completion ratio) relative to genome clusters
 * `pathway_abundances.genome_clusters.number_of_reads.[parquet|tsv.gz]` - Pathway abundances as the number of reads aligned relative to genome clusters
 * `pathway_abundances.genome_clusters.tpm.[parquet|tsv.gz]` - TPM normalized pathway abundances as the number of reads aligned relative to genome clusters
 * `pathway_abundances.genomes.coverage.[parquet|tsv.gz]` - Pathway coverage (i.e., pathway completion ratio) relative to genomes
 * `pathway_abundances.genomes.number_of_reads.[parquet|tsv.gz]` - Pathway abundances as the number of reads aligned relative to genomes
 * `pathway_abundances.genomes.tpm.[parquet|tsv.gz]` - TPM normalized pathway abundances as the number of reads aligned relative to genomes

### Merged

##### Taxonomy profiles
Sequence abundances can be used to determine the proportion of reads that were detected in database.

 * `taxonomic_abundance.genome_clusters.nc` - Genome-level taxonomic and sequence relative abundance profiles for all samples
 * `taxonomic_abundance.genomes.nc` - Genome-level taxonomic and sequence relative abundance profiles for all samples.

#### Functional profiles
##### Feature
 * `feature.genome_clusters.nc` - Feature abundances (number of reads, tpm) and prevalences (binary, total, ratio) of genome clusters for all samples
 * `feature.genomes.nc` - Feature abundances (number of reads, tpm) and prevalences (binary, total, ratio) of genomes for all samples

##### Pathway
 * `pathway.genome_clusters.nc` - Pathway abundances (number of reads, tpm) and coverages of genome clusters for all samples
 * `pathway.genomes.nc` - Pathway abundances (number of reads, tpm) and coverages of genomes for all samples

## Reading output files
### Reading Parquet files with Pandas
```python
!pip install pyarrow
df = pd.read_parquet("path/to/file.parquet")
```

### Reading NetCDF files with Xarray
> [!NOTE]
> To load `.nc` files you must have `h5netcdf` installed before `xarray` is loaded
```python
!pip install xarray h5netcdf
import xarray as xr

# Taxonomic abundances for genomes
ds_taxonomic = xr.open_dataset("../outputs/with_pangenomes/artifacts/taxonomic_abundances.genomes.nc")
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
ds_pathway = xr.open_dataset("../outputs/with_pangenomes/artifacts/pathway.genome_clusters.nc")
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

### Estimating the percent of unassigned reads (i.e., reference coverage)
Sequence coverage only sums to 100% if every read was assigned so you can subtract from 100% to determine the percent of unassigned reads
```python
# Load taxonomic profiling
ds_taxonomic = xr.open_dataset("../outputs/with_pangenomes/artifacts/taxonomic_abundances.genome_clusters.nc")

# Sum the sequence abundances (not taxonomic abundances)
percent_assigned_reads = ds_taxonomic["sequence_abundances"].sum(axis=1).to_pandas()
percent_unassigned_reads = 100 - percent_assigned_reads
```

### Filtering functional profiling results with taxonomy gate
```python
# Load taxonomic profiling
ds_taxonomic = xr.open_dataset("../outputs/with_pangenomes/artifacts/taxonomic_abundances.genome_clusters.nc")

# Load functional profiling
ds_pathway = xr.open_dataset("../outputs/with_pangenomes/artifacts/pathway.genome_clusters.nc")

# Get (pan)genomes to retain from taxonomic abundances
minimum_samples_detected = 2
retained_organisms = (ds_taxonomic["taxonomic_abundances"].to_pandas() > 0).sum(axis=0)[lambda x: x >= minimum_samples_detected].index

# Filter functional profiling with taxonomic abundance gate
ds_pathway_filtered = ds_pathway.sel(genome_clusters=retained_organisms)
```

### Reformatting Xarray NetCDF files into Pandas DataFrames
```python
# Load pathway abundances
ds_pathway = xr.open_dataset("../outputs/with_pangenomes/artifacts/pathway.genome_clusters.nc")

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

### Selecting coverage `prevalence` cutoff

```python
import compositional as coda
coda.plot_prevalence(X_coverage > tol_coverage, style="ggplot")

# Find where the curve drops off and cut there
```