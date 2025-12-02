Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_5/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_5/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_5/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_5/intermediate/logs
[2025-12-02 12:08:53.621] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 12:08:53.621] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 12:08:53.621] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 12:08:53.621] [jointLog] [info] parsing read library format
[2025-12-02 12:08:53.621] [jointLog] [info] There is 1 library.
[2025-12-02 12:08:53.621] [jointLog] [info] Loading pufferfish index
[2025-12-02 12:08:53.621] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 4.3385 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 198.08 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 100.17 us
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 30.466 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 35.301 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 7.3068 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 367.2 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 25.153 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 112.29 us
-----------------------------------------




[2025-12-02 12:08:54.091] [jointLog] [info] done
[2025-12-02 12:08:54.297] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 12:08:54.299] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 25,526, hits per frag:  0.0520753







[2025-12-02 12:09:27.591] [jointLog] [info] Computed 3,673 rich equivalence classes for further processing
[2025-12-02 12:09:27.591] [jointLog] [info] Counted 43,005 total reads in the equivalence classes 
[2025-12-02 12:09:27.592] [jointLog] [info] Number of mappings discarded because of alignment score : 100,925
[2025-12-02 12:09:27.592] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 80,796
[2025-12-02 12:09:27.592] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 12:09:27.592] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 16
[2025-12-02 12:09:27.593] [jointLog] [warning] Only 43005 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 12:09:27.593] [jointLog] [info] Mapping rate = 4.30438%

[2025-12-02 12:09:27.593] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 12:09:27.593] [jointLog] [info] Starting optimizer
[2025-12-02 12:09:27.597] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 12:09:27.597] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 12:09:27.603] [jointLog] [info] iteration = 100 | max rel diff. = 0.0769231
[2025-12-02 12:09:27.609] [jointLog] [info] iteration = 200 | max rel diff. = 0.03125
[2025-12-02 12:09:27.611] [jointLog] [info] iteration = 240 | max rel diff. = 0.00181705
[2025-12-02 12:09:27.611] [jointLog] [info] Finished optimizer
[2025-12-02 12:09:27.611] [jointLog] [info] writing output 


