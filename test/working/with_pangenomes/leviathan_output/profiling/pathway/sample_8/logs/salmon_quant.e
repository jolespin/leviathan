Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_8/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_8/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_8/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_8/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 10.515 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 129.75 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 55.084 us
-----------------------------------------
[2026-03-03 15:48:50.384] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.384] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.384] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.384] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.384] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.384] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.384] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 58.344 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 43.598 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 38.101 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 178.58 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 9.9828 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 139 us
-----------------------------------------




[2026-03-03 15:48:50.725] [jointLog] [info] done
[2026-03-03 15:48:50.755] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.758] [jointLog] [info] Number of decoys : 0








[2026-03-03 15:49:00.785] [jointLog] [info] Computed 1,849 rich equivalence classes for further processing
[2026-03-03 15:49:00.785] [jointLog] [info] Counted 10,929 total reads in the equivalence classes 
[2026-03-03 15:49:00.785] [jointLog] [info] Number of mappings discarded because of alignment score : 26,844
[2026-03-03 15:49:00.785] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 20,300
[2026-03-03 15:49:00.785] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:00.785] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 0
[2026-03-03 15:49:00.786] [jointLog] [warning] Only 10929 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:00.786] [jointLog] [info] Mapping rate = 4.20086%

[2026-03-03 15:49:00.786] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:00.787] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:00.789] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:00.790] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:00.795] [jointLog] [info] iteration = 100 | max rel diff. = 0.0666667
[2026-03-03 15:49:00.800] [jointLog] [info] iteration = 200 | max rel diff. = 0.026743
[2026-03-03 15:49:00.805] [jointLog] [info] iteration = 300 | max rel diff. = 0.0225403
[2026-03-03 15:49:00.809] [jointLog] [info] iteration = 400 | max rel diff. = 0.0143959
[2026-03-03 15:49:00.814] [jointLog] [info] iteration = 484 | max rel diff. = 0.00522293
[2026-03-03 15:49:00.814] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:00.814] [jointLog] [info] writing output 


