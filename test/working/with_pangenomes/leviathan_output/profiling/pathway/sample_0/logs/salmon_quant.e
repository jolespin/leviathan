Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_0/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_0/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_0/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_0/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 13.052 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 121.12 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 41.959 us
-----------------------------------------
[2026-03-03 15:48:50.380] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.380] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.380] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.380] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.380] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.382] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.382] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 58.907 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 43.693 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 38.199 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 179 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 11.113 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 493.38 us
-----------------------------------------




[2026-03-03 15:48:50.727] [jointLog] [info] done
[2026-03-03 15:48:50.755] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.757] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 24,061, hits per frag:  0.0489559[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 47,808, hits per frag:  0.0481871[2026-03-03 15:49:30.006] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 71,920, hits per frag:  0.0482202







[2026-03-03 15:49:38.094] [jointLog] [info] Computed 7,288 rich equivalence classes for further processing
[2026-03-03 15:49:38.094] [jointLog] [info] Counted 78,547 total reads in the equivalence classes 
[2026-03-03 15:49:38.095] [jointLog] [info] Number of mappings discarded because of alignment score : 166,904
[2026-03-03 15:49:38.095] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 145,516
[2026-03-03 15:49:38.095] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:38.095] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 359
[2026-03-03 15:49:38.096] [jointLog] [warning] Only 78547 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:38.096] [jointLog] [info] Mapping rate = 4.49677%

[2026-03-03 15:49:38.096] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:38.096] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:38.099] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:38.099] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:38.110] [jointLog] [info] iteration = 100 | max rel diff. = 0.0608787
[2026-03-03 15:49:38.119] [jointLog] [info] iteration = 200 | max rel diff. = 0.0267366
[2026-03-03 15:49:38.128] [jointLog] [info] iteration = 279 | max rel diff. = 0.00481598
[2026-03-03 15:49:38.128] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:38.128] [jointLog] [info] writing output 


