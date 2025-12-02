Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_5/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_5/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_5/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_5/intermediate/logs
[2025-12-02 10:47:38.687] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.687] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.687] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.687] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.687] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.687] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.687] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 5.7306 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 891.33 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 85.166 us
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 45.353 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 38.985 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 14.504 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 393.45 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.819 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.2124 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.371] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.373] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 25,519, hits per frag:  0.052108







[2025-12-02 10:48:13.343] [jointLog] [info] Computed 3,673 rich equivalence classes for further processing
[2025-12-02 10:48:13.343] [jointLog] [info] Counted 43,005 total reads in the equivalence classes 
[2025-12-02 10:48:13.344] [jointLog] [info] Number of mappings discarded because of alignment score : 100,925
[2025-12-02 10:48:13.344] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 80,796
[2025-12-02 10:48:13.344] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:48:13.344] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 16
[2025-12-02 10:48:13.346] [jointLog] [warning] Only 43005 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:48:13.346] [jointLog] [info] Mapping rate = 4.30438%

[2025-12-02 10:48:13.346] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:48:13.346] [jointLog] [info] Starting optimizer
[2025-12-02 10:48:13.349] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:48:13.349] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:48:13.356] [jointLog] [info] iteration = 100 | max rel diff. = 0.0769231
[2025-12-02 10:48:13.361] [jointLog] [info] iteration = 200 | max rel diff. = 0.03125
[2025-12-02 10:48:13.364] [jointLog] [info] iteration = 240 | max rel diff. = 0.00181637
[2025-12-02 10:48:13.364] [jointLog] [info] Finished optimizer
[2025-12-02 10:48:13.364] [jointLog] [info] writing output 


