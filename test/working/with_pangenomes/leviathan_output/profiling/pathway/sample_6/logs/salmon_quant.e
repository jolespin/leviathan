Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_6/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_6/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_6/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_6/intermediate/logs
[2025-12-02 10:47:38.822] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.822] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.822] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.822] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.822] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.822] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.822] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 4.3728 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 279.67 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 110.96 us
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 16.715 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 31.135 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 4.7043 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 308.62 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.862 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.1687 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.374] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.376] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 22,086, hits per frag:  0.0443329[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 44,329, hits per frag:  0.0447678







[2025-12-02 10:48:19.586] [jointLog] [info] Computed 4,981 rich equivalence classes for further processing
[2025-12-02 10:48:19.586] [jointLog] [info] Counted 55,411 total reads in the equivalence classes 
[2025-12-02 10:48:19.587] [jointLog] [info] Number of mappings discarded because of alignment score : 108,612
[2025-12-02 10:48:19.587] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 102,855
[2025-12-02 10:48:19.587] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:48:19.587] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 0
[2025-12-02 10:48:19.588] [jointLog] [warning] Only 55411 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:48:19.588] [jointLog] [info] Mapping rate = 4.29098%

[2025-12-02 10:48:19.588] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:48:19.588] [jointLog] [info] Starting optimizer
[2025-12-02 10:48:19.592] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:48:19.592] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:48:19.598] [jointLog] [info] iteration = 100 | max rel diff. = 0.000176144
[2025-12-02 10:48:19.599] [jointLog] [info] Finished optimizer
[2025-12-02 10:48:19.599] [jointLog] [info] writing output 


