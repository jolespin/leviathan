Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 48 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../../Analysis/leviathan_output/references/index/salmon_index }
### [ mates1 ] => { /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592225/output/trimmed_1.fastq.gz }
### [ mates2 ] => { /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592225/output/trimmed_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../../Analysis/leviathan_output/profiling/DNA/pathway/SRR7592225/intermediate }
Logs will be written to ../../Analysis/leviathan_output/profiling/DNA/pathway/SRR7592225/intermediate/logs
[2025-03-05 06:13:44.062] [jointLog] [info] setting maxHashResizeThreads to 48
[2025-03-05 06:13:44.062] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-03-05 06:13:44.062] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-03-05 06:13:44.063] [jointLog] [info] parsing read library format
[2025-03-05 06:13:44.063] [jointLog] [info] There is 1 library.
[2025-03-05 06:13:44.063] [jointLog] [info] Loading pufferfish index
[2025-03-05 06:13:44.063] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 9.0827 s
-----------------------------------------
size = 10861019
-----------------------------------------
| Loading contig offsets | Time = 21.477 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 10.208 ms
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 633.57 ms
-----------------------------------------
size = 704023998
Number of ones: 10861018
Number of ones per inventory item: 512
Inventory entries filled: 21213
-----------------------------------------
| Loading contig boundaries | Time = 1.7611 s
-----------------------------------------
size = 704023998
-----------------------------------------
| Loading sequence | Time = 888.42 ms
-----------------------------------------
size = 378193458
-----------------------------------------
| Loading positions | Time = 7.0432 s
-----------------------------------------
size = 3231347829
-----------------------------------------
| Loading reference sequence | Time = 4.0504 s
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 141.63 ms
-----------------------------------------
[2025-03-05 06:14:07.705] [jointLog] [info] done
[2025-03-05 06:14:07.930] [jointLog] [info] Index contained 3,225,512 targets
[2025-03-05 06:14:08.893] [jointLog] [info] Number of decoys : 0




[2025-03-05 06:14:11.197] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 1,646,029, hits per frag:  4.20865[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 3,253,274, hits per frag:  5.31252[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 4,899,172, hits per frag:  3.80058[A

[32mprocessed[31m 2,000,000 [32mfragments[0m
hits: 6,529,843, hits per frag:  3.52537[A

[32mprocessed[31m 2,500,000 [32mfragments[0m
hits: 8,184,744, hits per frag:  3.68171[A

[32mprocessed[31m 3,000,000 [32mfragments[0m
hits: 9,828,639, hits per frag:  3.40404[A

[32mprocessed[31m 3,500,000 [32mfragments[0m
hits: 11,470,450, hits per frag:  3.36401[A

[32mprocessed[31m 4,000,000 [32mfragments[0m
hits: 13,110,466, hits per frag:  3.41203[A

[32mprocessed[31m 4,500,000 [32mfragments[0m
hits: 14,764,843, hits per frag:  3.63038[A

[32mprocessed[31m 5,000,000 [32mfragments[0m
hits: 16,388,912, hits per frag:  3.42382[A

[32mprocessed[31m 5,500,000 [32mfragments[0m
hits: 18,025,078, hits per frag:  3.3985[A

[32mprocessed[31m 6,000,000 [32mfragments[0m
hits: 19,655,575, hits per frag:  3.36422[A

[32mprocessed[31m 6,500,000 [32mfragments[0m
hits: 21,293,170, hits per frag:  3.30841[A

[32mprocessed[31m 7,000,000 [32mfragments[0m
hits: 22,933,597, hits per frag:  3.34555[A

[32mprocessed[31m 7,500,000 [32mfragments[0m
hits: 24,575,941, hits per frag:  3.42453[A

[32mprocessed[31m 8,000,000 [32mfragments[0m
hits: 26,232,793, hits per frag:  3.32064[A

[32mprocessed[31m 8,500,000 [32mfragments[0m
hits: 27,884,999, hits per frag:  3.38064[A

[32mprocessed[31m 9,000,000 [32mfragments[0m
hits: 29,529,552, hits per frag:  3.44161[A

[32mprocessed[31m 9,500,000 [32mfragments[0m
hits: 31,181,150, hits per frag:  3.33968[A

[32mprocessed[31m 10,000,000 [32mfragments[0m
hits: 32,836,379, hits per frag:  3.35266[A

[32mprocessed[31m 10,500,000 [32mfragments[0m
hits: 34,484,744, hits per frag:  3.34745[A

[32mprocessed[31m 11,000,000 [32mfragments[0m
hits: 36,130,246, hits per frag:  3.32656[A

[32mprocessed[31m 11,500,000 [32mfragments[0m
hits: 37,781,896, hits per frag:  3.31772[A

[32mprocessed[31m 12,000,000 [32mfragments[0m
hits: 39,427,253, hits per frag:  3.34087[A

[32mprocessed[31m 12,500,000 [32mfragments[0m
hits: 41,079,810, hits per frag:  3.34026[A

[32mprocessed[31m 13,000,000 [32mfragments[0m
hits: 42,725,649, hits per frag:  3.34524[A

[32mprocessed[31m 13,500,000 [32mfragments[0m
hits: 44,372,495, hits per frag:  3.31915[A

[32mprocessed[31m 14,000,000 [32mfragments[0m
hits: 46,020,718, hits per frag:  3.31608[A

[32mprocessed[31m 14,500,000 [32mfragments[0m
hits: 47,674,555, hits per frag:  3.31112[A

[32mprocessed[31m 15,000,000 [32mfragments[0m
hits: 49,328,348, hits per frag:  3.31648[A

[32mprocessed[31m 15,500,000 [32mfragments[0m
hits: 50,973,411, hits per frag:  3.31784[A

[32mprocessed[31m 16,000,000 [32mfragments[0m
hits: 52,625,720, hits per frag:  3.31147[A

[32mprocessed[31m 16,500,000 [32mfragments[0m
hits: 54,271,182, hits per frag:  3.31321[A

[32mprocessed[31m 17,000,000 [32mfragments[0m
hits: 55,925,040, hits per frag:  3.34532[A

[32mprocessed[31m 17,500,000 [32mfragments[0m
hits: 57,558,444, hits per frag:  3.31175[A

[32mprocessed[31m 18,000,000 [32mfragments[0m
hits: 59,218,597, hits per frag:  3.31578[A

[32mprocessed[31m 18,500,000 [32mfragments[0m
hits: 60,866,891, hits per frag:  3.36687[A

[32mprocessed[31m 19,000,000 [32mfragments[0m
hits: 62,521,864, hits per frag:  3.31094[A

[32mprocessed[31m 19,500,000 [32mfragments[0m
hits: 64,177,534, hits per frag:  3.31385[A

[32mprocessed[31m 20,000,000 [32mfragments[0m
hits: 65,821,913, hits per frag:  3.32495[A

[32mprocessed[31m 20,500,000 [32mfragments[0m
hits: 67,479,261, hits per frag:  3.31331[A

[32mprocessed[31m 20,500,930 [32mfragments[0m
hits: 67,482,676, hits per frag:  3.32613[A

[32mprocessed[31m 21,000,000 [32mfragments[0m
hits: 69,125,869, hits per frag:  3.31702[A

[32mprocessed[31m 21,500,000 [32mfragments[0m
hits: 70,773,523, hits per frag:  3.29726[A

[32mprocessed[31m 22,000,000 [32mfragments[0m
hits: 72,421,384, hits per frag:  3.3053[A

[32mprocessed[31m 22,500,000 [32mfragments[0m
hits: 74,049,894, hits per frag:  3.29463[A

[32mprocessed[31m 23,000,000 [32mfragments[0m
hits: 75,705,778, hits per frag:  3.30363[A

[32mprocessed[31m 23,500,000 [32mfragments[0m
hits: 77,361,110, hits per frag:  3.36619[A

[32mprocessed[31m 24,000,000 [32mfragments[0m
hits: 79,016,373, hits per frag:  3.32254[A

[32mprocessed[31m 24,500,000 [32mfragments[0m
hits: 80,677,109, hits per frag:  3.31439[A

[32mprocessed[31m 25,000,000 [32mfragments[0m
hits: 82,335,341, hits per frag:  3.31133[A

[32mprocessed[31m 25,500,000 [32mfragments[0m
hits: 83,971,570, hits per frag:  3.29717[A

[32mprocessed[31m 26,000,000 [32mfragments[0m
hits: 85,622,113, hits per frag:  3.33337



[2025-03-05 06:27:58.441] [jointLog] [info] Computed 1,852,670 rich equivalence classes for further processing
[2025-03-05 06:27:58.441] [jointLog] [info] Counted 5,784,780 total reads in the equivalence classes 




[2025-03-05 06:27:58.738] [jointLog] [info] Number of mappings discarded because of alignment score : 88,176,191
[2025-03-05 06:27:58.738] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 3,438,315
[2025-03-05 06:27:58.738] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-03-05 06:27:58.738] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 15,599
[2025-03-05 06:27:58.738] [jointLog] [info] Mapping rate = 22.0349%

[2025-03-05 06:27:58.738] [jointLog] [info] finished quantifyLibrary()
[2025-03-05 06:27:58.738] [jointLog] [info] Starting optimizer
[2025-03-05 06:28:11.401] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-03-05 06:28:11.984] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-03-05 06:29:02.403] [jointLog] [info] iteration = 100 | max rel diff. = 0.115282
[2025-03-05 06:29:52.800] [jointLog] [info] iteration = 200 | max rel diff. = 0.0568787
[2025-03-05 06:30:43.163] [jointLog] [info] iteration = 300 | max rel diff. = 0.0407505
[2025-03-05 06:31:31.450] [jointLog] [info] iteration = 400 | max rel diff. = 0.0261116
[2025-03-05 06:32:24.296] [jointLog] [info] iteration = 500 | max rel diff. = 0.0236337
[2025-03-05 06:33:17.315] [jointLog] [info] iteration = 600 | max rel diff. = 0.0173834
[2025-03-05 06:34:04.942] [jointLog] [info] iteration = 700 | max rel diff. = 0.0153332
[2025-03-05 06:34:53.421] [jointLog] [info] iteration = 800 | max rel diff. = 0.011678
[2025-03-05 06:35:38.796] [jointLog] [info] iteration = 900 | max rel diff. = 0.0159894
[2025-03-05 06:36:24.816] [jointLog] [info] iteration = 1,000 | max rel diff. = 0.0124747
[2025-03-05 06:36:43.526] [jointLog] [info] iteration = 1,047 | max rel diff. = 0.00994667
[2025-03-05 06:36:43.976] [jointLog] [info] Finished optimizer
[2025-03-05 06:36:43.976] [jointLog] [info] writing output 

[2025-03-05 06:36:55.659] [jointLog] [warning] NOTE: Read Lib [[ /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592225/output/trimmed_1.fastq.gz, /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592225/output/trimmed_2.fastq.gz]] :

Detected a *potential* strand bias > 1% in an unstranded protocol check the file: ../../Analysis/leviathan_output/profiling/DNA/pathway/SRR7592225/intermediate/lib_format_counts.json for details


