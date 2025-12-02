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
| Loading contig table | Time = 5.9603 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 1.9923 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 105.58 us
-----------------------------------------
[2025-12-02 10:47:38.674] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.674] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.674] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.674] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.674] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.674] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.674] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 45.428 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 39.083 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 14.061 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 407.47 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.851 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.2033 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.371] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.374] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 24,069, hits per frag:  0.0482512[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 47,818, hits per frag:  0.0481343[2025-12-02 10:48:20.151] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 71,912, hits per frag:  0.0481734







[2025-12-02 10:48:28.407] [jointLog] [info] Computed 7,288 rich equivalence classes for further processing
[2025-12-02 10:48:28.407] [jointLog] [info] Counted 78,547 total reads in the equivalence classes 
[2025-12-02 10:48:28.408] [jointLog] [info] Number of mappings discarded because of alignment score : 166,904
[2025-12-02 10:48:28.408] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 145,516
[2025-12-02 10:48:28.408] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:48:28.408] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 359
[2025-12-02 10:48:28.408] [jointLog] [warning] Only 78547 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:48:28.409] [jointLog] [info] Mapping rate = 4.49677%

[2025-12-02 10:48:28.409] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:48:28.409] [jointLog] [info] Starting optimizer
[2025-12-02 10:48:28.411] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:48:28.411] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:48:28.423] [jointLog] [info] iteration = 100 | max rel diff. = 0.0608784
[2025-12-02 10:48:28.436] [jointLog] [info] iteration = 200 | max rel diff. = 0.0267369
[2025-12-02 10:48:28.444] [jointLog] [info] iteration = 279 | max rel diff. = 0.00481609
[2025-12-02 10:48:28.445] [jointLog] [info] Finished optimizer
[2025-12-02 10:48:28.445] [jointLog] [info] writing output 


