Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_2/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_2/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_2/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_2/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 5.3877 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 733.21 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 108.42 us
-----------------------------------------
[2025-12-02 10:47:38.782] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.782] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.782] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.782] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.782] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.782] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.782] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 28.549 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 31.907 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 5.8596 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 333.36 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.844 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.1973 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.375] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.377] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 20,521, hits per frag:  0.0412505







[2025-12-02 10:47:59.126] [jointLog] [info] Computed 2,674 rich equivalence classes for further processing
[2025-12-02 10:47:59.126] [jointLog] [info] Counted 21,007 total reads in the equivalence classes 
[2025-12-02 10:47:59.127] [jointLog] [info] Number of mappings discarded because of alignment score : 40,655
[2025-12-02 10:47:59.127] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 40,206
[2025-12-02 10:47:59.127] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:47:59.127] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 0
[2025-12-02 10:47:59.128] [jointLog] [warning] Only 21007 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:47:59.128] [jointLog] [info] Mapping rate = 4.08972%

[2025-12-02 10:47:59.128] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:47:59.129] [jointLog] [info] Starting optimizer
[2025-12-02 10:47:59.132] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:47:59.132] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:47:59.137] [jointLog] [info] iteration = 100 | max rel diff. = 0.00668682
[2025-12-02 10:47:59.137] [jointLog] [info] Finished optimizer
[2025-12-02 10:47:59.137] [jointLog] [info] writing output 


