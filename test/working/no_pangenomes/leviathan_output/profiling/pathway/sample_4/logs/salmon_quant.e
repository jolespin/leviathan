Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_4/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_4/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_4/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_4/intermediate/logs
[2025-12-02 12:08:53.440] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 12:08:53.440] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 12:08:53.442] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 12:08:53.442] [jointLog] [info] parsing read library format
[2025-12-02 12:08:53.443] [jointLog] [info] There is 1 library.
[2025-12-02 12:08:53.444] [jointLog] [info] Loading pufferfish index
[2025-12-02 12:08:53.444] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 20.411 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 3.672 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 1.0705 ms
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 69.65 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 42.205 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 23.587 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 406.27 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 47.714 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 2.0372 ms
-----------------------------------------
[2025-12-02 12:08:54.073] [jointLog] [info] done
[2025-12-02 12:08:54.267] [jointLog] [info] Index contained 38,726 targets




[2025-12-02 12:08:54.283] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 26,253, hits per frag:  0.0530358[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 52,482, hits per frag:  0.0524962[2025-12-02 12:09:31.848] [jointLog] [info] Automatically detected most likely library type as IU









[2025-12-02 12:09:34.153] [jointLog] [info] Computed 7,655 rich equivalence classes for further processing
[2025-12-02 12:09:34.153] [jointLog] [info] Counted 62,405 total reads in the equivalence classes 
[2025-12-02 12:09:34.153] [jointLog] [info] Number of mappings discarded because of alignment score : 154,985
[2025-12-02 12:09:34.153] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 116,021
[2025-12-02 12:09:34.153] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 12:09:34.153] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 8
[2025-12-02 12:09:34.154] [jointLog] [warning] Only 62405 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 12:09:34.154] [jointLog] [info] Mapping rate = 4.80767%

[2025-12-02 12:09:34.154] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 12:09:34.154] [jointLog] [info] Starting optimizer
[2025-12-02 12:09:34.158] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 12:09:34.158] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 12:09:34.168] [jointLog] [info] iteration = 100 | max rel diff. = 0.0666667
[2025-12-02 12:09:34.176] [jointLog] [info] iteration = 200 | max rel diff. = 0.0243902
[2025-12-02 12:09:34.187] [jointLog] [info] iteration = 300 | max rel diff. = 0.0243902
[2025-12-02 12:09:34.192] [jointLog] [info] iteration = 333 | max rel diff. = 5.33557e-06
[2025-12-02 12:09:34.192] [jointLog] [info] Finished optimizer
[2025-12-02 12:09:34.192] [jointLog] [info] writing output 


