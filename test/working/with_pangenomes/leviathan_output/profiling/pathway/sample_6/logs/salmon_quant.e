Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_6/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_6/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_6/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_6/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 5.0278 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 835.04 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 720.38 us
-----------------------------------------
[2026-03-03 15:48:50.335] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.335] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.335] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.335] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.335] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.335] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.336] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 20.491 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 31.44 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 3.7368 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 108.41 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 10.345 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 200 us
-----------------------------------------
[2026-03-03 15:48:50.517] [jointLog] [info] done




[2026-03-03 15:48:50.554] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.556] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 22,085, hits per frag:  0.0448854[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 44,331, hits per frag:  0.0444191







[2026-03-03 15:49:29.845] [jointLog] [info] Computed 4,981 rich equivalence classes for further processing
[2026-03-03 15:49:29.845] [jointLog] [info] Counted 55,411 total reads in the equivalence classes 
[2026-03-03 15:49:29.845] [jointLog] [info] Number of mappings discarded because of alignment score : 108,612
[2026-03-03 15:49:29.845] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 102,855
[2026-03-03 15:49:29.845] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:29.845] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 0
[2026-03-03 15:49:29.846] [jointLog] [warning] Only 55411 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:29.846] [jointLog] [info] Mapping rate = 4.29098%

[2026-03-03 15:49:29.846] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:29.846] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:29.850] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:29.850] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:29.858] [jointLog] [info] iteration = 100 | max rel diff. = 0.000176173
[2026-03-03 15:49:29.858] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:29.858] [jointLog] [info] writing output 


