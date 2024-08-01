# Leviathan
`Leviathan` is a fast, memory-efficient, and scalable taxonomic and pathway profiler for next generation sequencing (genome-resolved) metagenomics and metatranscriptomics.  `Leviathan` is powered by `Salmon` and `Sylph` in the backend.

## Modules
* `leviathan preprocess` - Preprocesses data into form than can be used for `leviathan index` [Pending]
* `leviathan index` - Build, update, and validate leviathan database [Complete]
    ```
    leviathan-index.py \
        -f leviathan-test-n10.fasta \
        -m leviathan-test-n10.feature_mapping.tsv \
        -g leviathan-test-n10.genome_filepaths.tsv \
        -d leviathan-test-n10-index/ \
        -p=-1
    ```
* `leviathan info` - Report information about `leviathan` database [Complete]
    ```
    leviathan-info.py -d leviathan-test-n10-index/
    ```
* `leviathan profile-taxonomy` - Profile taxonomy using `Sylph` with leviathan database [Complete]
    ```
    leviathan-profile-taxonomy.py \
        -1 ../Fastq/SRR12042303_1.fastq.gz \
        -2 ../Fastq/SRR12042303_2.fastq.gz \
        -n SRR12042303 \
        -d index/leviathan-test-n10-index/ \
        -p=-1
    ```
* `leviathan profile-pathway` - Profile pathways using `Salmon` with leviathan database [In progress]
    ```
    leviathan-profile-pathway.py \
        -1 ../Fastq/SRR12042303_1.fastq.gz \
        -2 ../Fastq/SRR12042303_2.fastq.gz \
        -n SRR12042303 \
        -d index/leviathan-test-n10-index/ \
        -p=-1
    ```
* `leviathan profile-targeted` - Profile taxonomy and pathways uing targeted approach which runs `profile-taxonomy` then gets the subset of detected genomes, builds a targeted Salmon index, then runs `profile-pathway` [Pending]
* `leviathan reformat` - Reformat tables into various formats and shapes [Pending]
* [?] `leviathan end-to-end` - Complete end-to-end pipeline which builds database, profiles, and converts tables [Pending]

## Development Stage:
* `pre-alpha`

## Modules:
![Modules](images/modules.png)

