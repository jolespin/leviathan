Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_3/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_3/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_3/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_3/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 5.927 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 130.62 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 43.833 us
-----------------------------------------
[2026-03-03 15:48:50.389] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.389] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.389] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.389] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.389] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.389] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.389] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 57.726 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 42.773 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 37.451 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 181.09 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 11.275 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 134.67 us
-----------------------------------------




[2026-03-03 15:48:50.727] [jointLog] [info] done
[2026-03-03 15:48:50.755] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.757] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 27,487, hits per frag:  0.0554176







[2026-03-03 15:49:20.119] [jointLog] [info] Computed 3,858 rich equivalence classes for further processing
[2026-03-03 15:49:20.119] [jointLog] [info] Counted 35,783 total reads in the equivalence classes 
[2026-03-03 15:49:20.119] [jointLog] [info] Number of mappings discarded because of alignment score : 95,688
[2026-03-03 15:49:20.119] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 67,507
[2026-03-03 15:49:20.119] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:20.119] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 11
[2026-03-03 15:49:20.120] [jointLog] [warning] Only 35783 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:20.120] [jointLog] [info] Mapping rate = 4.20629%

[2026-03-03 15:49:20.120] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:20.120] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:20.123] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:20.123] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:20.130] [jointLog] [info] iteration = 100 | max rel diff. = 0.0681818
[2026-03-03 15:49:20.137] [jointLog] [info] iteration = 200 | max rel diff. = 0.0310481
[2026-03-03 15:49:20.143] [jointLog] [info] iteration = 300 | max rel diff. = 0.0196078
[2026-03-03 15:49:20.149] [jointLog] [info] iteration = 400 | max rel diff. = 0.0196078
[2026-03-03 15:49:20.156] [jointLog] [info] iteration = 500 | max rel diff. = 0.0149254
[2026-03-03 15:49:20.159] [jointLog] [info] iteration = 550 | max rel diff. = 0.00159045
[2026-03-03 15:49:20.159] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:20.159] [jointLog] [info] writing output 


