Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_8/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_8/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_8/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_8/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 5.7122 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 1.5894 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 55.25 us
-----------------------------------------
[2025-12-02 10:47:38.675] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.675] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.675] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.675] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.675] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.675] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.675] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 42.629 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 37.01 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 15.072 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 410.6 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.825 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.1348 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.366] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.371] [jointLog] [info] Number of decoys : 0








[2025-12-02 10:47:49.360] [jointLog] [info] Computed 1,849 rich equivalence classes for further processing
[2025-12-02 10:47:49.360] [jointLog] [info] Counted 10,929 total reads in the equivalence classes 
[2025-12-02 10:47:49.360] [jointLog] [info] Number of mappings discarded because of alignment score : 26,844
[2025-12-02 10:47:49.360] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 20,300
[2025-12-02 10:47:49.360] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:47:49.360] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 0
[2025-12-02 10:47:49.361] [jointLog] [warning] Only 10929 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:47:49.361] [jointLog] [info] Mapping rate = 4.20086%

[2025-12-02 10:47:49.361] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:47:49.362] [jointLog] [info] Starting optimizer
[2025-12-02 10:47:49.367] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:47:49.367] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:47:49.372] [jointLog] [info] iteration = 100 | max rel diff. = 0.0666667
[2025-12-02 10:47:49.377] [jointLog] [info] iteration = 200 | max rel diff. = 0.0267379
[2025-12-02 10:47:49.382] [jointLog] [info] iteration = 300 | max rel diff. = 0.022535
[2025-12-02 10:47:49.387] [jointLog] [info] iteration = 400 | max rel diff. = 0.0143871
[2025-12-02 10:47:49.391] [jointLog] [info] iteration = 484 | max rel diff. = 0.00522151
[2025-12-02 10:47:49.391] [jointLog] [info] Finished optimizer
[2025-12-02 10:47:49.391] [jointLog] [info] writing output 


