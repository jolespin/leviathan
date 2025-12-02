Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_1/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_1/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_1/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_1/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 4.677 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 259.38 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 93.625 us
-----------------------------------------
[2025-12-02 12:08:53.614] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 12:08:53.614] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 12:08:53.614] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 12:08:53.614] [jointLog] [info] parsing read library format
[2025-12-02 12:08:53.614] [jointLog] [info] There is 1 library.
[2025-12-02 12:08:53.614] [jointLog] [info] Loading pufferfish index
[2025-12-02 12:08:53.615] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 26.478 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 36.599 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 6.6549 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 376.28 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 26.455 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 125.96 us
-----------------------------------------




[2025-12-02 12:08:54.092] [jointLog] [info] done
[2025-12-02 12:08:54.297] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 12:08:54.299] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 21,679, hits per frag:  0.0439983[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 43,172, hits per frag:  0.0433029[2025-12-02 12:09:36.222] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 64,380, hits per frag:  0.0430706







[2025-12-02 12:09:37.686] [jointLog] [info] Computed 6,357 rich equivalence classes for further processing
[2025-12-02 12:09:37.686] [jointLog] [info] Counted 63,757 total reads in the equivalence classes 
[2025-12-02 12:09:37.686] [jointLog] [info] Number of mappings discarded because of alignment score : 128,376
[2025-12-02 12:09:37.686] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 118,584
[2025-12-02 12:09:37.686] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 12:09:37.686] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 4
[2025-12-02 12:09:37.687] [jointLog] [warning] Only 63757 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 12:09:37.687] [jointLog] [info] Mapping rate = 4.19186%

[2025-12-02 12:09:37.687] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 12:09:37.687] [jointLog] [info] Starting optimizer
[2025-12-02 12:09:37.690] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 12:09:37.690] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 12:09:37.703] [jointLog] [info] iteration = 100 | max rel diff. = 0.0414445
[2025-12-02 12:09:37.711] [jointLog] [info] iteration = 154 | max rel diff. = 2.87895e-05
[2025-12-02 12:09:37.712] [jointLog] [info] Finished optimizer
[2025-12-02 12:09:37.712] [jointLog] [info] writing output 


