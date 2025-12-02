Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_3/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_3/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_3/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_3/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 4.6822 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 532.42 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 83.542 us
-----------------------------------------
[2025-12-02 12:08:53.588] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 12:08:53.588] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 12:08:53.588] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 12:08:53.588] [jointLog] [info] parsing read library format
[2025-12-02 12:08:53.588] [jointLog] [info] There is 1 library.
[2025-12-02 12:08:53.588] [jointLog] [info] Loading pufferfish index
[2025-12-02 12:08:53.588] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 20.234 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 33.226 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 10.144 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 400.3 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 12.223 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 2.0604 ms
-----------------------------------------




[2025-12-02 12:08:54.073] [jointLog] [info] done
[2025-12-02 12:08:54.263] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 12:08:54.282] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 27,485, hits per frag:  0.055269







[2025-12-02 12:09:24.118] [jointLog] [info] Computed 3,858 rich equivalence classes for further processing
[2025-12-02 12:09:24.118] [jointLog] [info] Counted 35,783 total reads in the equivalence classes 
[2025-12-02 12:09:24.119] [jointLog] [info] Number of mappings discarded because of alignment score : 95,688
[2025-12-02 12:09:24.119] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 67,507
[2025-12-02 12:09:24.119] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 12:09:24.119] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 11
[2025-12-02 12:09:24.120] [jointLog] [warning] Only 35783 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 12:09:24.120] [jointLog] [info] Mapping rate = 4.20629%

[2025-12-02 12:09:24.120] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 12:09:24.120] [jointLog] [info] Starting optimizer
[2025-12-02 12:09:24.123] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 12:09:24.123] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 12:09:24.129] [jointLog] [info] iteration = 100 | max rel diff. = 0.0681818
[2025-12-02 12:09:24.135] [jointLog] [info] iteration = 200 | max rel diff. = 0.0310465
[2025-12-02 12:09:24.141] [jointLog] [info] iteration = 300 | max rel diff. = 0.0196078
[2025-12-02 12:09:24.147] [jointLog] [info] iteration = 400 | max rel diff. = 0.0196078
[2025-12-02 12:09:24.153] [jointLog] [info] iteration = 500 | max rel diff. = 0.0149254
[2025-12-02 12:09:24.156] [jointLog] [info] iteration = 550 | max rel diff. = 0.00158913
[2025-12-02 12:09:24.156] [jointLog] [info] Finished optimizer
[2025-12-02 12:09:24.156] [jointLog] [info] writing output 


