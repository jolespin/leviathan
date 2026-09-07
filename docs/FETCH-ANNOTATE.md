# Walkthrough: Fetching databases and annotating proteins
Leviathan does not require KEGG to run but this walkthrough shows how to use annotate proteins with KOfam, build a pathway database, and build a Leviathan database.  

This walkthrough assumes you've downloaded the [`toy CAMI-II marine 100 genomes dataset`](https://zenodo.org/records/17783338) but this walkthrough can be applied to any dataset.


### 1. Download the KEGG Pathways hosted by [EBI](https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool)

#### Install KEGG Pathway Profiler
[`KEGG-Pathway-Profiler`](https://github.com/jolespin/kegg_pathway_profiler) should be installed but if not...

```
pip install kegg-pathway-profiler
```

#### Download KEGG Pathway database
```
build-pathway-database.py --ebi latest test/databases/KEGG-Pathway-Profiler/database.pkl.gz
```

#### Get subset of pathway KOfams
```
cut -f2 test/databases/KEGG-Pathway-Profiler/test/databases/KEGG-Pathway-Profiler/pathway_kofams.list
```


### 2. Annotate proteins with KEGG orthology
If you don't have annotations already then you will need to annotate proteins yourself.  I recommend [`PyKOfamSearch`](https://github.com/jolespin/pykofamsearch) which is powered by [PyHMMER](https://doi.org/10.1093/bioinformatics/btad214). 

If you're only annotating for `Leviathan` then keep the `--subset` argument but if you want full KEGG ortholog annotation then remove it (it will take longer to annotate against all KOfam).

#### Install PyKOfamSearch
```
pip install pykofamsearch
```
#### Fetch and compile the latest KOfam database
```
serialize_kofam_models -o test/databases/KOfam
```

#### Annotate KOfams
Recommend using the `--anvio_bitscore_heuristic` which enables a relaxed heuristic that can recover remote homology. 

```
# KOfam database
kofam_database="test/databases/KOfam/database.pkl.gz"
pathway_subset="test/databases/KEGG-Pathway-Profiler/pathway_kofams.list"

# Protein fasta files
protein_fasta_files="test/databases/CAMI-II_Marine_n-100/sample_*/genomes/*.faa.gz"

# Run PyKOfamSearch
mkdir -p working/
n_threads=-1
cat ${protein_fasta_files} | pykofamsearch -b ${kofam_database} -p=${n_threads} -o working/pykofamsearch_results.pathway_subset.tsv.gz --anvio_bitscore_heuristic --subset ${pathway_subset}
```

### 3. Preprocess the annotations
Move to the [End-to-End Walkthrough](../docs/END-TO-END.md)

