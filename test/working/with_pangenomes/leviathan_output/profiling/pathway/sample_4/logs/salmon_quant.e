Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_4/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_4/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_4/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_4/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 10.497 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 131.58 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 45.666 us
-----------------------------------------
[2026-03-03 15:48:50.384] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.384] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.384] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.384] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.384] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.384] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.384] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 50.207 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 38.698 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 9.066 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 185.03 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 3.9718 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 148.12 us
-----------------------------------------




[2026-03-03 15:48:50.683] [jointLog] [info] done
[2026-03-03 15:48:50.699] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.701] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 26,238, hits per frag:  0.0525143[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 52,471, hits per frag:  0.0529006[2026-03-03 15:49:28.127] [jointLog] [info] Automatically detected most likely library type as IU









[2026-03-03 15:49:30.261] [jointLog] [info] Computed 7,655 rich equivalence classes for further processing
[2026-03-03 15:49:30.261] [jointLog] [info] Counted 62,405 total reads in the equivalence classes 
[2026-03-03 15:49:30.261] [jointLog] [info] Number of mappings discarded because of alignment score : 154,985
[2026-03-03 15:49:30.261] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 116,021
[2026-03-03 15:49:30.261] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:30.261] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 8
[2026-03-03 15:49:30.263] [jointLog] [warning] Only 62405 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:30.263] [jointLog] [info] Mapping rate = 4.80767%

[2026-03-03 15:49:30.263] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:30.263] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:30.267] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:30.267] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:30.278] [jointLog] [info] iteration = 100 | max rel diff. = 0.0666667
[2026-03-03 15:49:30.297] [jointLog] [info] iteration = 200 | max rel diff. = 0.0243902
[2026-03-03 15:49:30.308] [jointLog] [info] iteration = 300 | max rel diff. = 0.0243902
[2026-03-03 15:49:30.310] [jointLog] [info] iteration = 333 | max rel diff. = 5.33534e-06
[2026-03-03 15:49:30.311] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:30.311] [jointLog] [info] writing output 


