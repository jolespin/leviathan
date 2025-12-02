Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100/sample_7/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100/sample_7/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/leviathan_output/profiling/pathway/sample_7/intermediate }
Logs will be written to ../working/leviathan_output/profiling/pathway/sample_7/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 9.9383 ms
-----------------------------------------
size = 141170
[2025-12-02 10:47:38.445] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 10:47:38.445] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 10:47:38.451] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 10:47:38.451] [jointLog] [info] parsing read library format
[2025-12-02 10:47:38.452] [jointLog] [info] There is 1 library.
[2025-12-02 10:47:38.454] [jointLog] [info] Loading pufferfish index
[2025-12-02 10:47:38.454] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig offsets | Time = 12.52 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 1.3551 ms
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 122.57 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 55.27 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 28.619 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 499.51 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 53.83 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 1.1974 ms
-----------------------------------------




[2025-12-02 10:47:39.244] [jointLog] [info] done
[2025-12-02 10:47:39.369] [jointLog] [info] Index contained 38,726 targets
[2025-12-02 10:47:39.371] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 25,386, hits per frag:  0.051354[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 50,984, hits per frag:  0.051206[2025-12-02 10:48:18.316] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 76,603, hits per frag:  0.0512575[A

[32mprocessed[31m 2,000,000 [32mfragments[0m
hits: 101,751, hits per frag:  0.0509913[A

[32mprocessed[31m 2,500,000 [32mfragments[0m
hits: 127,094, hits per frag:  0.0509427[A

[32mprocessed[31m 3,000,000 [32mfragments[0m
hits: 152,651, hits per frag:  0.0509661[A

[32mprocessed[31m 3,500,000 [32mfragments[0m
hits: 177,909, hits per frag:  0.0509024[A

[32mprocessed[31m 4,000,000 [32mfragments[0m
hits: 203,483, hits per frag:  0.050934







[2025-12-02 10:49:03.405] [jointLog] [info] Computed 6,133 rich equivalence classes for further processing
[2025-12-02 10:49:03.405] [jointLog] [info] Counted 199,714 total reads in the equivalence classes 
[2025-12-02 10:49:03.405] [jointLog] [info] Number of mappings discarded because of alignment score : 411,194
[2025-12-02 10:49:03.405] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 367,558
[2025-12-02 10:49:03.405] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 10:49:03.405] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 311
[2025-12-02 10:49:03.406] [jointLog] [warning] Only 199714 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 10:49:03.406] [jointLog] [info] Mapping rate = 4.73534%

[2025-12-02 10:49:03.406] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 10:49:03.406] [jointLog] [info] Starting optimizer
[2025-12-02 10:49:03.408] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 10:49:03.408] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 10:49:03.416] [jointLog] [info] iteration = 100 | max rel diff. = 0.0491803
[2025-12-02 10:49:03.424] [jointLog] [info] iteration = 200 | max rel diff. = 0.0208333
[2025-12-02 10:49:03.432] [jointLog] [info] iteration = 300 | max rel diff. = 0.0208333
[2025-12-02 10:49:03.440] [jointLog] [info] iteration = 400 | max rel diff. = 0.0133333
[2025-12-02 10:49:03.449] [jointLog] [info] iteration = 500 | max rel diff. = 0.0133333
[2025-12-02 10:49:03.457] [jointLog] [info] iteration = 600 | max rel diff. = 0.0133333
[2025-12-02 10:49:03.458] [jointLog] [info] iteration = 623 | max rel diff. = 1.73945e-06
[2025-12-02 10:49:03.459] [jointLog] [info] Finished optimizer
[2025-12-02 10:49:03.459] [jointLog] [info] writing output 


