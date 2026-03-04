Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 2 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../working/with_pangenomes/references/index/salmon_index }
### [ mates1 ] => { ../databases/CAMI-II_Marine_n-100//sample_7/reads/reads_1.fastq.gz }
### [ mates2 ] => { ../databases/CAMI-II_Marine_n-100//sample_7/reads/reads_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_7/intermediate }
Logs will be written to ../working/with_pangenomes/leviathan_output/profiling/pathway/sample_7/intermediate/logs
-----------------------------------------
| Loading contig table | Time = 21.256 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 138.46 us
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 52.583 us
-----------------------------------------
[2026-03-03 15:48:50.373] [jointLog] [info] setting maxHashResizeThreads to 2
[2026-03-03 15:48:50.373] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2026-03-03 15:48:50.373] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2026-03-03 15:48:50.373] [jointLog] [info] parsing read library format
[2026-03-03 15:48:50.373] [jointLog] [info] There is 1 library.
[2026-03-03 15:48:50.373] [jointLog] [info] Loading pufferfish index
[2026-03-03 15:48:50.373] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 55.789 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 43.343 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 36.703 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 182.69 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 9.1008 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 99.709 us
-----------------------------------------




[2026-03-03 15:48:50.723] [jointLog] [info] done
[2026-03-03 15:48:50.744] [jointLog] [info] Index contained 38,726 targets
[2026-03-03 15:48:50.747] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 25,382, hits per frag:  0.0513163[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 50,979, hits per frag:  0.0512174[2026-03-03 15:49:28.404] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 76,604, hits per frag:  0.0512137[A

[32mprocessed[31m 2,000,000 [32mfragments[0m
hits: 101,756, hits per frag:  0.0509881[A

[32mprocessed[31m 2,500,000 [32mfragments[0m
hits: 127,094, hits per frag:  0.0509521[A

[32mprocessed[31m 3,000,000 [32mfragments[0m
hits: 152,653, hits per frag:  0.0509647[A

[32mprocessed[31m 3,500,000 [32mfragments[0m
hits: 177,909, hits per frag:  0.0509028[A

[32mprocessed[31m 4,000,000 [32mfragments[0m
hits: 203,484, hits per frag:  0.0509354







[2026-03-03 15:50:11.666] [jointLog] [info] Computed 6,133 rich equivalence classes for further processing
[2026-03-03 15:50:11.666] [jointLog] [info] Counted 199,714 total reads in the equivalence classes 
[2026-03-03 15:50:11.667] [jointLog] [info] Number of mappings discarded because of alignment score : 411,194
[2026-03-03 15:50:11.667] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 367,558
[2026-03-03 15:50:11.667] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2026-03-03 15:50:11.667] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 311
[2026-03-03 15:50:11.668] [jointLog] [warning] Only 199714 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2026-03-03 15:50:11.668] [jointLog] [info] Mapping rate = 4.73534%

[2026-03-03 15:50:11.668] [jointLog] [info] finished quantifyLibrary()
[2026-03-03 15:50:11.668] [jointLog] [info] Starting optimizer
[2026-03-03 15:50:11.670] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2026-03-03 15:50:11.670] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2026-03-03 15:50:11.678] [jointLog] [info] iteration = 100 | max rel diff. = 0.0491803
[2026-03-03 15:50:11.691] [jointLog] [info] iteration = 200 | max rel diff. = 0.0208333
[2026-03-03 15:50:11.700] [jointLog] [info] iteration = 300 | max rel diff. = 0.0208333
[2026-03-03 15:50:11.708] [jointLog] [info] iteration = 400 | max rel diff. = 0.0133333
[2026-03-03 15:50:11.717] [jointLog] [info] iteration = 500 | max rel diff. = 0.0133333
[2026-03-03 15:50:11.725] [jointLog] [info] iteration = 600 | max rel diff. = 0.0133333
[2026-03-03 15:50:11.727] [jointLog] [info] iteration = 623 | max rel diff. = 1.73945e-06
[2026-03-03 15:50:11.728] [jointLog] [info] Finished optimizer
[2026-03-03 15:50:11.728] [jointLog] [info] writing output 


