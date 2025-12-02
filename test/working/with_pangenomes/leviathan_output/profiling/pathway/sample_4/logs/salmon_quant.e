Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_4/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_4/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_4/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_4/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 6.8269 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 1.5471 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 1.2191 ms
-----------------------------------------
[2025-12-02 10:47:38.682] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.682] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.682] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.682] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.682] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.682] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.682] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 45.261 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 41.597 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 15.396 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 394.02 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.828 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.2252 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.375] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.377] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 26,256, hits per frag:  0.0531233[A

[32mprocessed[31m 1,000,001 [32mfragments[0m
hits: 52,466, hits per frag:  0.0527694[2025-12-02 10:48:17.896] [jointLog] [info] Automatically detected most likely library type as IU









[2025-12-02 10:48:20.116] [jointLog] [info] Computed 7,655 rich equivalence classes for further processing
[2025-12-02 10:48:20.116] [jointLog] [info] Counted 62,405 total reads in the equivalence classes 
[2025-12-02 10:48:20.117] [jointLog] [info] Number of mappings discarded because of alignment score : 154,985
[2025-12-02 10:48:20.117] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 116,021
[2025-12-02 10:48:20.117] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:48:20.117] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 8
[2025-12-02 10:48:20.117] [jointLog] [warning] Only 62405 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:48:20.117] [jointLog] [info] Mapping rate = 4.80767%

[2025-12-02 10:48:20.117] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:48:20.118] [jointLog] [info] Starting optimizer
[2025-12-02 10:48:20.121] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:48:20.122] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:48:20.137] [jointLog] [info] iteration = 100 | max rel diff. = 0.0666667
[2025-12-02 10:48:20.149] [jointLog] [info] iteration = 200 | max rel diff. = 0.0243902
[2025-12-02 10:48:20.160] [jointLog] [info] iteration = 300 | max rel diff. = 0.0243902
[2025-12-02 10:48:20.166] [jointLog] [info] iteration = 333 | max rel diff. = 5.33413e-06
[2025-12-02 10:48:20.166] [jointLog] [info] Finished optimizer
[2025-12-02 10:48:20.166] [jointLog] [info] writing output 


