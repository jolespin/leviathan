Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_1/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_1/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_1/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_1/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 5.2045 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 292.79 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 173.75 us
-----------------------------------------
[2025-12-02 10:47:38.795] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.795] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.795] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.795] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.795] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.795] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.795] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 24.575 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 31.815 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 5.4764 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 325.71 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.802 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.3124 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.373] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.375] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 21,692, hits per frag:  0.0440648[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 43,178, hits per frag:  0.0431879[2025-12-02 10:48:22.433] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 64,386, hits per frag:  0.0431528







[2025-12-02 10:48:24.010] [jointLog] [info] Computed 6,357 rich equivalence classes for further processing
[2025-12-02 10:48:24.010] [jointLog] [info] Counted 63,757 total reads in the equivalence classes 
[2025-12-02 10:48:24.011] [jointLog] [info] Number of mappings discarded because of alignment score : 128,376
[2025-12-02 10:48:24.011] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 118,584
[2025-12-02 10:48:24.011] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:48:24.011] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 4
[2025-12-02 10:48:24.012] [jointLog] [warning] Only 63757 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:48:24.012] [jointLog] [info] Mapping rate = 4.19186%

[2025-12-02 10:48:24.012] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:48:24.012] [jointLog] [info] Starting optimizer
[2025-12-02 10:48:24.015] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:48:24.015] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:48:24.025] [jointLog] [info] iteration = 100 | max rel diff. = 0.0414447
[2025-12-02 10:48:24.030] [jointLog] [info] iteration = 154 | max rel diff. = 2.87888e-05
[2025-12-02 10:48:24.030] [jointLog] [info] Finished optimizer
[2025-12-02 10:48:24.030] [jointLog] [info] writing output 


