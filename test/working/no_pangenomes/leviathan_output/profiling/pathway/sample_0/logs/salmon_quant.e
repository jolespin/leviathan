Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_0/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_0/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_0/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_0/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 4.9396 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 1.5099 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 246.12 us
-----------------------------------------
[2025-12-02 12:08:53.559] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 12:08:53.559] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 12:08:53.559] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 12:08:53.559] [jointLog] [info] parsing read library format
[2025-12-02 12:08:53.559] [jointLog] [info] There is 1 library.
[2025-12-02 12:08:53.559] [jointLog] [info] Loading pufferfish index
[2025-12-02 12:08:53.559] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 38.372 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 32.497 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 6.4671 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 413.35 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 12.879 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 3.2429 ms
-----------------------------------------
[2025-12-02 12:08:54.073] [jointLog] [info] done
[2025-12-02 12:08:54.262] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 12:08:54.281] [jointLog] [info] Number of decoys : 0




[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 24,072, hits per frag:  0.0481914[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 47,809, hits per frag:  0.0478359[2025-12-02 12:09:33.925] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 71,920, hits per frag:  0.0482159







[2025-12-02 12:09:41.905] [jointLog] [info] Computed 7,288 rich equivalence classes for further processing
[2025-12-02 12:09:41.905] [jointLog] [info] Counted 78,547 total reads in the equivalence classes 
[2025-12-02 12:09:41.906] [jointLog] [info] Number of mappings discarded because of alignment score : 166,904
[2025-12-02 12:09:41.906] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 145,516
[2025-12-02 12:09:41.906] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 12:09:41.906] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 359
[2025-12-02 12:09:41.906] [jointLog] [warning] Only 78547 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 12:09:41.906] [jointLog] [info] Mapping rate = 4.49677%

[2025-12-02 12:09:41.906] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 12:09:41.906] [jointLog] [info] Starting optimizer
[2025-12-02 12:09:41.908] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 12:09:41.909] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 12:09:41.920] [jointLog] [info] iteration = 100 | max rel diff. = 0.0608785
[2025-12-02 12:09:41.937] [jointLog] [info] iteration = 200 | max rel diff. = 0.0267368
[2025-12-02 12:09:41.951] [jointLog] [info] iteration = 279 | max rel diff. = 0.00481606
[2025-12-02 12:09:41.951] [jointLog] [info] Finished optimizer
[2025-12-02 12:09:41.951] [jointLog] [info] writing output 


