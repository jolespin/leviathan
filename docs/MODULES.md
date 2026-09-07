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
        -1 fastq/example_1.fastq.gz \
        -2 fastq/example_2.fastq.gz \
        -n example \
        -d references/index/ \
        -o leviathan_output/profiling/taxonomy/ \
        -p=-1

### `leviathan-profile-pathway`
Profile pathways using `Salmon` with `leviathan` database

    leviathan-profile-pathway.py \
        -1 fastq/example_1.fastq.gz \
        -2 fastq/example_2.fastq.gz \
        -n example \
        -d references/index/ \
        -o leviathan_output/profiling/pathway/ \
        -p=-1

### `leviathan-merge`
Merge sample-specific taxonomic and/or pathway profiling

    leviathan-merge.py \
        -t leviathan_output/profiling/taxonomy/ \
        -p leviathan_output/profiling/pathway/ \
