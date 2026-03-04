Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_2/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_2/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_2/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_2/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 5.7135 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 330.96 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 350.92 us
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 16.899 ms
-----------------------------------------
size = 42886739
[2026-03-03 15:48:50.531] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.531] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.531] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.531] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.531] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.531] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.531] [jointLog] [info] Loading dense pufferfish index.
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 31.258 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 5.8112 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 160.22 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 3.81 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 89.959 us
-----------------------------------------
[2026-03-03 15:48:50.757] [jointLog] [info] done




[2026-03-03 15:48:50.774] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.775] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 20,519, hits per frag:  0.0410727







[2026-03-03 15:49:09.763] [jointLog] [info] Computed 2,674 rich equivalence classes for further processing
[2026-03-03 15:49:09.763] [jointLog] [info] Counted 21,007 total reads in the equivalence classes 
[2026-03-03 15:49:09.764] [jointLog] [info] Number of mappings discarded because of alignment score : 40,655
[2026-03-03 15:49:09.764] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 40,206
[2026-03-03 15:49:09.764] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:09.764] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 0
[2026-03-03 15:49:09.765] [jointLog] [warning] Only 21007 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:09.765] [jointLog] [info] Mapping rate = 4.08972%

[2026-03-03 15:49:09.765] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:09.765] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:09.768] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:09.768] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:09.773] [jointLog] [info] iteration = 100 | max rel diff. = 0.00668909
[2026-03-03 15:49:09.774] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:09.774] [jointLog] [info] writing output 


