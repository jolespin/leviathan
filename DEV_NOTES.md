# Internal Development Notes

### Salmon Index Benchmarking: 
    * Number of sequences (~400 enzymes per prokaryotic genome):
        10k genomes: OceanDNA.n_10000.fasta:3729135
        1k genomes: OceanDNA.n_1000.fasta:419841
        100 genomes: OceanDNA.n_100.fasta:40017
        10 genomes: OceanDNA.n_10.fasta:4006
    * File sizes: 
        3.9G    OceanDNA.n_10000.fasta
        432M    OceanDNA.n_1000.fasta
        41M     OceanDNA.n_100.fasta
        4.1M    OceanDNA.n_10.fasta
    * Index Size:
        8.2G    OceanDNA.n_10000.salmon_index
        1.5G    OceanDNA.n_1000.salmon_index
        143M    OceanDNA.n_100.salmon_index
        13M     OceanDNA.n_10.salmon_index
    * Index (Peak memory using 16 threads): 
        OceanDNA.n_10.salmon_index.log: Maximum resident set size (kbytes): 99428 (0.1GB)
        OceanDNA.n_100.salmon_index.log:        Maximum resident set size (kbytes): 172776 (0.17GB)
        OceanDNA.n_1000.salmon_index.log:       Maximum resident set size (kbytes): 1499528 (1.5GB)
        OceanDNA.n_10000.salmon_index.log:      Maximum resident set size (kbytes): 9649924 (9.65GB)


quant: 
    * --meta mode https://salmon.readthedocs.io/en/develop/salmon.html#meta
    * salmon quant --meta --libType A --index ${INDEX} -1 ${R1} -2 ${R2} --threads ${N_JOBS}  --minScoreFraction=0.87 --writeUnmappedNames


* needs pathway abundance and completion/coverage estimation 

#### Relevant Discussion:
* Regarding --keepDuplicates https://github.com/COMBINE-lab/salmon/issues/223
* Metagenomics usage: https://github.com/COMBINE-lab/salmon/issues/330