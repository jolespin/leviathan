Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_5/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_5/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_5/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_5/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 6.2952 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 165.42 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 79.25 us
-----------------------------------------
[2026-03-03 15:48:50.389] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.389] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.389] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.389] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.389] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.389] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.389] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 60.115 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 40.688 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 37.28 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 179.36 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 10.72 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 190.67 us
-----------------------------------------




[2026-03-03 15:48:50.725] [jointLog] [info] done
[2026-03-03 15:48:50.750] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.752] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 25,512, hits per frag:  0.0511741







[2026-03-03 15:49:23.565] [jointLog] [info] Computed 3,673 rich equivalence classes for further processing
[2026-03-03 15:49:23.565] [jointLog] [info] Counted 43,005 total reads in the equivalence classes 
[2026-03-03 15:49:23.565] [jointLog] [info] Number of mappings discarded because of alignment score : 100,925
[2026-03-03 15:49:23.565] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 80,796
[2026-03-03 15:49:23.565] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:49:23.565] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 16
[2026-03-03 15:49:23.566] [jointLog] [warning] Only 43005 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:49:23.566] [jointLog] [info] Mapping rate = 4.30438%

[2026-03-03 15:49:23.566] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:49:23.567] [jointLog] [info] Starting optimizer
[2026-03-03 15:49:23.570] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:49:23.570] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:49:23.576] [jointLog] [info] iteration = 100 | max rel diff. = 0.0769231
[2026-03-03 15:49:23.582] [jointLog] [info] iteration = 200 | max rel diff. = 0.03125
[2026-03-03 15:49:23.584] [jointLog] [info] iteration = 240 | max rel diff. = 0.0018169
[2026-03-03 15:49:23.585] [jointLog] [info] Finished optimizer
[2026-03-03 15:49:23.585] [jointLog] [info] writing output 


