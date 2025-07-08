# Leviathan
`Leviathan` is a fast, memory-efficient, and scalable taxonomic and pathway profiler for next generation sequencing (genome-resolved) metagenomics and metatranscriptomics.  `Leviathan` is powered by `Salmon` and `Sylph` in the backend.

## Install
```
pip install leviathan
```

## Benchmarking

### Benchmarking against 10,100,1000, and 10000 genomes
Benchmarking using trimmed SRR12042303 sample with 4 threads on ram16GB-cpu4 SageMaker instance (ml.m5.4xlarge)

| number_of_genomes | number_of_cds_with_features | preprocess | index | profile-taxonomy | profile-pathway |
|-------------------|-----------------------------|------------|-------|------------------|-----------------|
| 10                | 1928                        | 0:03       | 0:09  | 0:41             | 2:09            |
| 100               | 18410                       | 0:31       | 0:26  | 0:41             | 4:29            |
| 1000              | 191155                      | 5:29       | 3:55  | 0:43             | 12:50           |
| 10000             | 1684876                     | 46:00      | 39:10 | 0:48             | 18:14           |

### Benchmarking against CAMI-I and CAMI-II using 16 threads
#### Computational Performance
|                 |          | Leviathan          |                  | HUMAnN             |                  | Fold Improvement |             |
|-----------------|----------|--------------------|------------------|--------------------|------------------|------------------|-------------|
|                 |          | Duration (minutes) | Peak Memory (GB) | Duration (minutes) | Peak Memory (GB) | Duration         | Memory      |
| CAMI_high_toy   | H_S001   | 14.605             | 2.335016         | 1083.566667        | 32.314652        | 74.19148693      | 13.83915656 |
|                 | H_S002   | 14.89016667        | 2.347396         | 949.7333333        | 32.282708        | 63.78258582      | 13.75256156 |
|                 | H_S003   | 14.95683333        | 2.335868         | 875.8333333        | 32.6381          | 58.55740409      | 13.97257893 |
|                 | H_S004   | 15.02433333        | 2.345132         | 852.1833333        | 32.329528        | 56.72020944      | 13.7858031  |
|                 | H_S005   | 15.26516667        | 2.33234          | 826.25             | 32.233252        | 54.12649714      | 13.82013429 |
| CAMI_medium_toy | M2_S001  | 5.775166667        | 1.622448         | 219.25             | 15.95032         | 37.96427232      | 9.831020778 |
|                 | M2_S002  | 5.812666667        | 1.622288         | 174.1166667        | 16.958124        | 29.95469664      | 10.45321423 |
| CAMI_low_toy    | S_S001   | 3.286666667        | 1.271656         | 76.9               | 10.003484        | 23.39756592      | 7.866501633 |
| Marine          | sample_0 | 13.777             | 2.70192          | 119.5166667        | 17.92066         | 8.675086497      | 6.632564991 |
|                 | sample_1 | 15.21883333        | 2.689312         | 121.3              | 18.001524        | 7.970387568      | 6.693728359 |
|                 | sample_2 | 14.97316667        | 2.705192         | 120.2666667        | 17.989872        | 8.032146395      | 6.650127606 |
|                 | sample_3 | 17.103             | 2.706732         | 124.05             | 17.82616         | 7.253113489      | 6.585860735 |
|                 | sample_4 | 14.32116667        | 2.737092         | 118.4666667        | 17.82212         | 8.272137978      | 6.511333927 |
|                 | sample_5 | 15.5325            | 2.719652         | 119.4              | 17.796968        | 7.687107677      | 6.543840168 |
|                 | sample_6 | 16.09216667        | 2.707584         | 119.7166667        | 17.912484        | 7.439437407      | 6.61567065  |
|                 | sample_7 | 14.89716667        | 2.732396         | 119.9166667        | 17.918184        | 8.049629124      | 6.557681976 |
|                 | sample_8 | 16.4145            | 2.715812         | 121.7333333        | 17.948436        | 7.416207215      | 6.608865415 |
|                 | sample_9 | 14.45016667        | 2.730564         | 118.8666667        | 17.788184        | 8.225972019      | 6.514472468 |

#### Accuracy
|                 | Accuracy | Leviathan  |            | HUMAnN     |            | Improvement |            |
|-----------------|----------|------------|------------|------------|------------|-------------|------------|
| Dataset         | SampleID | Genome     | Pangenome  | Genome     | Pangenome  | Genome      | Pangenome  |
| CAMI_high_toy   | H_S001   | 0.94915203 | 0.9970141  | 0.90492296 | 0.96099582 | 0.04422907  | 0.03601828 |
|                 | H_S002   | 0.95507956 | 0.98985329 | 0.89924221 | 0.95906862 | 0.05583735  | 0.03078467 |
|                 | H_S003   | 0.95564508 | 0.98875279 | 0.90037051 | 0.95979967 | 0.05527457  | 0.02895312 |
|                 | H_S004   | 0.94958715 | 0.98723154 | 0.89474711 | 0.95878323 | 0.05484004  | 0.02844831 |
|                 | H_S005   | 0.94197596 | 0.98769996 | 0.89011268 | 0.95725972 | 0.05186328  | 0.03044024 |
| CAMI_medium_toy | M2_S001  | 0.96924915 | 0.99832387 | 0.91014644 | 0.9619824  | 0.05910271  | 0.03634146 |
|                 | M2_S002  | 0.97617708 | 0.99880572 | 0.91769031 | 0.96501348 | 0.05848677  | 0.03379224 |
| CAMI_low_toy    | S_S001   | 0.99999814 | 0.99999814 | 0.98451525 | 0.98451525 | 0.01548289  | 0.01548289 |
| Marine          | sample_0 | 0.97270418 | 0.99333348 | 0.87828926 | 0.95375065 | 0.09441491  | 0.03958283 |
|                 | sample_1 | 0.92979713 | 0.99215731 | 0.87930812 | 0.9554143  | 0.05048901  | 0.03674301 |
|                 | sample_2 | 0.96859487 | 0.98170284 | 0.87681461 | 0.93927266 | 0.09178026  | 0.04243018 |
|                 | sample_3 | 0.970627   | 0.9842153  | 0.85963049 | 0.95170583 | 0.1109965   | 0.03250948 |
|                 | sample_4 | 0.96609552 | 0.98796938 | 0.84541101 | 0.93889123 | 0.1206845   | 0.04907814 |
|                 | sample_5 | 0.96139369 | 0.98560529 | 0.87402325 | 0.96117239 | 0.08737045  | 0.0244329  |
|                 | sample_6 | 0.9282808  | 0.98685683 | 0.86840838 | 0.95736121 | 0.05987242  | 0.02949562 |
|                 | sample_7 | 0.92314993 | 0.99418101 | 0.87191047 | 0.94657898 | 0.05123946  | 0.04760204 |
|                 | sample_8 | 0.97032735 | 0.98893696 | 0.87636575 | 0.94880384 | 0.09396159  | 0.04013312 |
|                 | sample_9 | 0.94588769 | 0.9858854  | 0.86567696 | 0.95481384 | 0.08021073  | 0.03107156 |

## Modules
### `leviathan-preprocess`
Preprocesses data into form than can be used by `leviathan-index` 
    
    leviathan-preprocess.py \
        -i references/manifest.tsv \
        -a references/pykofamsearch.pathways.tsv.gz \
        -o references/
    

### `leviathan-index`
Build, update, and validate `leviathan` database

    leviathan-index.py \
        -f references/cds.fasta.gz \
        -m references/feature_mapping.tsv.gz \
        -g references/genomes.tsv.gz \
        -d references/index/ \
        -p=-1

### `leviathan-info`
Report information about `leviathan` database

    leviathan-info.py -d references/index/

### `leviathan-profile-taxonomy`
Profile taxonomy using `Sylph` with `leviathan` database

    leviathan-profile-taxonomy.py \
        -1 ../Fastq/SRR12042303_1.fastq.gz \
        -2 ../Fastq/SRR12042303_2.fastq.gz \
        -n SRR12042303 \
        -d references/index/ \
        -o leviathan_output/profiling/taxonomy/ \
        -p=-1

### `leviathan-profile-pathway`
Profile pathways using `Salmon` with `leviathan` database

    leviathan-profile-pathway.py \
        -1 ../Fastq/SRR12042303_1.fastq.gz \
        -2 ../Fastq/SRR12042303_2.fastq.gz \
        -n SRR12042303 \
        -d references/index/ \
        -o leviathan_output/profiling/pathway/ \
        -p=-1

### `leviathan-merge`
Merge sample-specific taxonomic and/or pathway profiling

    leviathan-merge.py \
        -t leviathan_output/profiling/taxonomy/ \
        -p leviathan_output/profiling/pathway/ \

## Utility Scripts
* `compile-manifest-from-veba.py` - Compiles manifest.tsv file for `leviathan preprocess` from `VEBA` binning output 

    compile-manifest-from-veba.py \
        -i path/to/veba_output/binning/ \
        -t prokaryotic,eukaryotic \
        -o references/manifest.tsv

## Output Description

### Sample Specific
#### Taxonomy profiles
* Examples: 
    - Genome = Metagenome-assembled genome (MAG)
    - Genome cluster = ANI ??? 95% & Alignment Fraction ??? 50%

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
 * `feature_prevalence-binary.genome_clusters.[parquet|tsv.gz]` - Binary feature prevalence relative to genome clusters
 * `feature_prevalence-binary.genomes.[parquet|tsv.gz]` - Binary feature prevalence relative to genomes
 * `feature_prevalence-ratio.genome_clusters.[parquet|tsv.gz]` - Ratio of genomes within a genome cluster with feature detected
 * `feature_prevalence.genome_clusters.[parquet|tsv.gz]` - Binary feature prevalence relative to genome clusters
 * `feature_prevalence.genomes.[parquet|tsv.gz]` - Feature prevalence relative to genomes

##### Gene abundances - The abundance of individual genes within genome
 * `gene_abundances.genomes.number_of_reads.[parquet|tsv.gz]` - Number of reads aligned to a gene within a genome
 * `gene_abundances.genomes.tpm.[parquet|tsv.gz]` - TPM normalized abundance of reads aligned to a gene within a genome

##### Pathway abundances - Pathway abundances for a genome and genome-cluster

 * `pathway_abundances.genome_clusters.coverage.[parquet|tsv.gz]` - Pathway coverage relative to genome clusters
 * `pathway_abundances.genome_clusters.number_of_reads.[parquet|tsv.gz]` - Pathway abundances as the number of reads aligned relative to genome clusters
 * `pathway_abundances.genome_clusters.tpm.[parquet|tsv.gz]` - TPM normalized pathway abundances as the number of reads aligned relative to genome clusters
 * `pathway_abundances.genomes.coverage.[parquet|tsv.gz]` - Pathway coverage relative to genomes
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

## Reading NetCDF files with Xarray

```python
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

## Pathway Databases
Currently, the only pathway database supported for pathway coverage calculations is the KEGG module database using KEGG orthologs as features.  This database can be pre-built using [KEGG Pathway Profiler](https://github.com/jolespin/kegg_pathway_profiler) or built with `leviathan index` if KEGG orthologs are used as features.  

To maintain generalizability for custom feature sets (e.g., enzymes, reactions), the pathway database is not required but if it is not used when building `leviathan index` then the `leviathan profile-pathway` skips the pathway abundance and coverage calculations.

If custom databases are built, then the following nested Python dictionary structure needs to be followed: 

```python
# General Example
{
    id_pathway:{
        "name":Name of pathway,
        "definition":KEGG module definition,
        "classes":KEGG module classes,
        "graph":NetworkX MultiDiGraph,
        "ko_to_nodes": Dictionary of KEGG ortholog to nodes in graph,
        "optional_kos": Set of optional KEGG orthologs
    },
    }

# Specific Example
{
    'M00001': {
        'name': 'Glycolysis (Embden-Meyerhof pathway), glucose => pyruvate',
        'definition': (
            '(K00844,K12407,K00845,K25026,K00886,K08074,K00918) '
            '(K01810,K06859,K13810,K15916) '
            '(K00850,K16370,K21071,K00918) '
            '(K01623,K01624,K11645,K16305,K16306) '
            'K01803 ((K00134,K00150) K00927,K11389) '
            '(K01834,K15633,K15634,K15635) '
            '(K01689,K27394) '
            '(K00873,K12406)'
        ),
        'classes': 'Pathway modules; Carbohydrate metabolism; Central carbohydrate metabolism',
        'graph': <networkx.classes.multidigraph.MultiDiGraph object at 0x132d2a9e0>,
        'ko_to_nodes': {
            'K00844': [[0, 2]],
            'K12407': [[0, 2]],
            'K00845': [[0, 2]],
            'K25026': [[0, 2]],
            'K00886': [[0, 2]],
            'K08074': [[0, 2]],
            'K00918': [[0, 2], [3, 4]],
            'K01810': [[2, 3]],
            'K06859': [[2, 3]],
            'K13810': [[2, 3]],
            'K15916': [[2, 3]],
            'K00850': [[3, 4]],
            'K16370': [[3, 4]],
            'K21071': [[3, 4]],
            'K01623': [[4, 5]],
            'K01624': [[4, 5]],
            'K11645': [[4, 5]],
            'K16305': [[4, 5]],
            'K16306': [[4, 5]],
            'K01803': [[5, 6]],
            'K00134': [[6, 8]],
            'K00150': [[6, 8]],
            'K00927': [[8, 7]],
            'K11389': [[6, 7]],
            'K01834': [[7, 9]],
            'K15633': [[7, 9]],
            'K15634': [[7, 9]],
            'K15635': [[7, 9]],
            'K01689': [[9, 10]],
            'K27394': [[9, 10]],
            'K00873': [[10, 1]],
            'K12406': [[10, 1]]
        },
        'optional_kos': set()
    },
    'M00002': {
        'name': 'Glycolysis, core module involving three-carbon compounds',
        'definition': (
            'K01803 ((K00134,K00150) K00927,K11389) '
            '(K01834,K15633,K15634,K15635) '
            '(K01689,K27394) '
            '(K00873,K12406)'
        ),
        'classes': 'Pathway modules; Carbohydrate metabolism; Central carbohydrate metabolism',
        'graph': <networkx.classes.multidigraph.MultiDiGraph object at 0x10d51b160>,
        'ko_to_nodes': {
            'K01803': [[0, 2]],
            'K00134': [[2, 4]],
            'K00150': [[2, 4]],
            'K00927': [[4, 3]],
            'K11389': [[2, 3]],
            'K01834': [[3, 5]],
            'K15633': [[3, 5]],
            'K15634': [[3, 5]],
            'K15635': [[3, 5]],
            'K01689': [[5, 6]],
            'K27394': [[5, 6]],
            'K00873': [[6, 1]],
            'K12406': [[6, 1]]
        },
        'optional_kos': set()
    },
    ...
}

```
For documentation for pathway theory or how `MultiDiGraph` objects are generated, please refer to the source repository for [KEGG Pathway Completeness Tool](https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool) as [KEGG Pathway Profiler](https://github.com/jolespin/kegg_pathway_profiler) is a reimplementation for production.

## Development Stage:
* `beta`

## Citation:
* In progress

## Contact:
* jol.espinoz@gmail.com

## Modules:
![Modules](images/modules.png)
