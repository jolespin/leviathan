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
| Loading contig table | Time = 8.6739 ms
-----------------------------------------
size = 141170
-----------------------------------------
| Loading contig offsets | Time = 1.9058 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 539.38 us
-----------------------------------------
[2025-12-02 12:08:53.467] [jointLog] [info] setting maxHashResizeThreads to 2
[2025-12-02 12:08:53.467] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-12-02 12:08:53.467] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-12-02 12:08:53.467] [jointLog] [info] parsing read library format
[2025-12-02 12:08:53.467] [jointLog] [info] There is 1 library.
[2025-12-02 12:08:53.468] [jointLog] [info] Loading pufferfish index
[2025-12-02 12:08:53.468] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading mphf table | Time = 69.498 ms
-----------------------------------------
size = 42886739
Number of ones: 141169
Number of ones per inventory item: 512
Inventory entries filled: 276
-----------------------------------------
| Loading contig boundaries | Time = 44.52 ms
-----------------------------------------
size = 42886739
-----------------------------------------
| Loading sequence | Time = 21.419 ms
-----------------------------------------
size = 38651669
-----------------------------------------
| Loading positions | Time = 416.97 ms
-----------------------------------------
size = 42745248
-----------------------------------------
| Loading reference sequence | Time = 37.045 ms
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 2.056 ms
-----------------------------------------
[2025-12-02 12:08:54.073] [jointLog] [info] done
[2025-12-02 12:08:54.284] [jointLog] [info] Index contained 38,726 targets




[2025-12-02 12:08:54.293] [jointLog] [info] Number of decoys : 0
[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 25,378, hits per frag:  0.051237[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 50,977, hits per frag:  0.0513337[2025-12-02 12:09:32.765] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 76,624, hits per frag:  0.0513097[A

[32mprocessed[31m 2,000,000 [32mfragments[0m
hits: 101,755, hits per frag:  0.0509701[A

[32mprocessed[31m 2,500,000 [32mfragments[0m
hits: 127,092, hits per frag:  0.0509085[A

[32mprocessed[31m 3,000,000 [32mfragments[0m
hits: 152,655, hits per frag:  0.0509942[A

[32mprocessed[31m 3,500,000 [32mfragments[0m
hits: 177,904, hits per frag:  0.050883[A

[32mprocessed[31m 4,000,000 [32mfragments[0m
hits: 203,485, hits per frag:  0.0509474







[2025-12-02 12:10:16.335] [jointLog] [info] Computed 6,133 rich equivalence classes for further processing
[2025-12-02 12:10:16.335] [jointLog] [info] Counted 199,714 total reads in the equivalence classes 
[2025-12-02 12:10:16.335] [jointLog] [info] Number of mappings discarded because of alignment score : 411,194
[2025-12-02 12:10:16.335] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 367,558
[2025-12-02 12:10:16.335] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-12-02 12:10:16.335] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 311
[2025-12-02 12:10:16.336] [jointLog] [warning] Only 199714 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-12-02 12:10:16.336] [jointLog] [info] Mapping rate = 4.73534%

[2025-12-02 12:10:16.336] [jointLog] [info] finished quantifyLibrary()
[2025-12-02 12:10:16.337] [jointLog] [info] Starting optimizer
[2025-12-02 12:10:16.338] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-12-02 12:10:16.339] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-12-02 12:10:16.347] [jointLog] [info] iteration = 100 | max rel diff. = 0.0491803
[2025-12-02 12:10:16.355] [jointLog] [info] iteration = 200 | max rel diff. = 0.0208333
[2025-12-02 12:10:16.363] [jointLog] [info] iteration = 300 | max rel diff. = 0.0208333
[2025-12-02 12:10:16.371] [jointLog] [info] iteration = 400 | max rel diff. = 0.0133333
[2025-12-02 12:10:16.379] [jointLog] [info] iteration = 500 | max rel diff. = 0.0133333
[2025-12-02 12:10:16.387] [jointLog] [info] iteration = 600 | max rel diff. = 0.0133333
[2025-12-02 12:10:16.389] [jointLog] [info] iteration = 623 | max rel diff. = 1.73945e-06
[2025-12-02 12:10:16.389] [jointLog] [info] Finished optimizer
[2025-12-02 12:10:16.389] [jointLog] [info] writing output 


