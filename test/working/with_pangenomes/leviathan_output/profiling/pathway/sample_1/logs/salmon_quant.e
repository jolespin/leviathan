Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_1/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_1/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_1/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_1/intermediate/logs
[2026-03-03 15:48:50.653] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.653] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.653] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.653] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.653] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.653] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.653] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 4.609 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 212.42 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 168.79 us
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 13.728 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 33.032 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 4.1098 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 140.11 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 9.361 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 81.792 us
-----------------------------------------
[2026-03-03 15:48:50.859] [jointLog] [info] done




[2026-03-03 15:48:50.906] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.908] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 21,676, hits per frag:  0.0440506[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 43,168, hits per frag:  0.0433352[2026-03-03 15:49:32.458] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 64,376, hits per frag:  0.0429525







[2026-03-03 15:49:33.951] [jointLog] [info] Computed 6,357 rich equivalence classes for further processing
[2026-03-03 15:49:33.951] [jointLog] [info] Counted 63,757 total reads in the equivalence classes 
[2026-03-03 15:49:33.951] [jointLog] [info] Number of mappings discarded because of alignment score : 128,376
[2026-03-03 15:49:33.951] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 118,584
[2026-03-03 15:49:33.951] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:33.951] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 4
[2026-03-03 15:49:33.952] [jointLog] [warning] Only 63757 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:33.952] [jointLog] [info] Mapping rate = 4.19186%

[2026-03-03 15:49:33.952] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:33.952] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:33.955] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:33.955] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:33.967] [jointLog] [info] iteration = 100 | max rel diff. = 0.0414446
[2026-03-03 15:49:33.975] [jointLog] [info] iteration = 154 | max rel diff. = 2.87889e-05
[2026-03-03 15:49:33.975] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:33.975] [jointLog] [info] writing output 


