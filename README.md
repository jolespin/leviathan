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
* `alpha`

## Modules:
![Modules](images/modules.png)

