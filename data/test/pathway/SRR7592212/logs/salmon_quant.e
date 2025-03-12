Version Server Response: Not Found
### salmon (selective-alignment-based) v1.10.3
### [ program ] => salmon 
### [ command ] => quant 
### [ meta ] => { }
### [ libType ] => { A }
### [ threads ] => { 48 }
### [ minScoreFraction ] => { 0.87 }
### [ index ] => { ../../Analysis/leviathan_output/references/index/salmon_index }
### [ mates1 ] => { /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592212/output/trimmed_1.fastq.gz }
### [ mates2 ] => { /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592212/output/trimmed_2.fastq.gz }
### [ writeUnmappedNames ] => { }
### [ output ] => { ../../Analysis/leviathan_output/profiling/DNA/pathway/SRR7592212/intermediate }
Logs will be written to ../../Analysis/leviathan_output/profiling/DNA/pathway/SRR7592212/intermediate/logs
[2025-03-05 06:13:44.074] [jointLog] [info] setting maxHashResizeThreads to 48
[2025-03-05 06:13:44.074] [jointLog] [info] Fragment incompatibility prior below threshold.  Incompatible fragments will be ignored.
[2025-03-05 06:13:44.074] [jointLog] [info] Setting consensusSlack to selective-alignment default of 0.35.
[2025-03-05 06:13:44.074] [jointLog] [info] parsing read library format
[2025-03-05 06:13:44.074] [jointLog] [info] There is 1 library.
[2025-03-05 06:13:44.074] [jointLog] [info] Loading pufferfish index
[2025-03-05 06:13:44.074] [jointLog] [info] Loading dense pufferfish index.
-----------------------------------------
| Loading contig table | Time = 9.0709 s
-----------------------------------------
size = 10861019
-----------------------------------------
| Loading contig offsets | Time = 21.455 ms
-----------------------------------------
-----------------------------------------
| Loading reference lengths | Time = 10.224 ms
-----------------------------------------
-----------------------------------------
| Loading mphf table | Time = 633.17 ms
-----------------------------------------
size = 704023998
Number of ones: 10861018
Number of ones per inventory item: 512
Inventory entries filled: 21213
-----------------------------------------
| Loading contig boundaries | Time = 1.7637 s
-----------------------------------------
size = 704023998
-----------------------------------------
| Loading sequence | Time = 885.81 ms
-----------------------------------------
size = 378193458
-----------------------------------------
| Loading positions | Time = 7.0431 s
-----------------------------------------
size = 3231347829
-----------------------------------------
| Loading reference sequence | Time = 4.0504 s
-----------------------------------------
-----------------------------------------
| Loading reference accumulative lengths | Time = 141.61 ms
-----------------------------------------
[2025-03-05 06:14:07.705] [jointLog] [info] done
[2025-03-05 06:14:07.924] [jointLog] [info] Index contained 3,225,512 targets
[2025-03-05 06:14:08.887] [jointLog] [info] Number of decoys : 0




[2025-03-05 06:14:13.010] [jointLog] [info] Automatically detected most likely library type as IU

[A

[32mprocessed[31m 500,000 [32mfragments[0m
hits: 2,394,442, hits per frag:  7.64831[A

[32mprocessed[31m 1,000,000 [32mfragments[0m
hits: 4,755,188, hits per frag:  6.3514[A

[32mprocessed[31m 1,500,000 [32mfragments[0m
hits: 7,151,343, hits per frag:  5.56169[A

[32mprocessed[31m 2,000,001 [32mfragments[0m
hits: 9,544,622, hits per frag:  4.93386[A

[32mprocessed[31m 2,500,000 [32mfragments[0m
hits: 11,955,518, hits per frag:  5.3764[A

[32mprocessed[31m 3,000,000 [32mfragments[0m
hits: 14,364,083, hits per frag:  4.88967[A

[32mprocessed[31m 3,500,000 [32mfragments[0m
hits: 16,761,202, hits per frag:  4.9511[A

[32mprocessed[31m 4,000,000 [32mfragments[0m
hits: 19,144,946, hits per frag:  4.97719[A

[32mprocessed[31m 4,500,000 [32mfragments[0m
hits: 21,516,131, hits per frag:  4.88992[A

[32mprocessed[31m 5,000,000 [32mfragments[0m
hits: 23,922,688, hits per frag:  4.82572[A

[32mprocessed[31m 5,500,000 [32mfragments[0m
hits: 26,332,362, hits per frag:  4.89865[A

[32mprocessed[31m 6,000,000 [32mfragments[0m
hits: 28,749,974, hits per frag:  4.85068[A

[32mprocessed[31m 6,500,000 [32mfragments[0m
hits: 31,160,827, hits per frag:  4.89025[A

[32mprocessed[31m 7,000,000 [32mfragments[0m
hits: 33,589,101, hits per frag:  4.83851[A

[32mprocessed[31m 7,500,000 [32mfragments[0m
hits: 35,964,120, hits per frag:  4.93206[A

[32mprocessed[31m 8,000,000 [32mfragments[0m
hits: 38,340,280, hits per frag:  4.82016[A

[32mprocessed[31m 8,500,000 [32mfragments[0m
hits: 40,740,150, hits per frag:  4.84195[A

[32mprocessed[31m 9,000,000 [32mfragments[0m
hits: 43,154,019, hits per frag:  4.9015[A

[32mprocessed[31m 9,500,000 [32mfragments[0m
hits: 45,578,322, hits per frag:  4.81268[A

[32mprocessed[31m 10,000,000 [32mfragments[0m
hits: 47,971,970, hits per frag:  4.80502[A

[32mprocessed[31m 10,500,000 [32mfragments[0m
hits: 50,370,372, hits per frag:  4.88014[A

[32mprocessed[31m 11,000,000 [32mfragments[0m
hits: 52,763,906, hits per frag:  4.87419[A

[32mprocessed[31m 11,500,000 [32mfragments[0m
hits: 55,168,983, hits per frag:  4.85888[A

[32mprocessed[31m 12,000,000 [32mfragments[0m
hits: 57,571,038, hits per frag:  4.85663[A

[32mprocessed[31m 12,500,000 [32mfragments[0m
hits: 59,991,796, hits per frag:  4.89437[A

[32mprocessed[31m 13,000,000 [32mfragments[0m
hits: 62,400,758, hits per frag:  4.88622[A

[32mprocessed[31m 13,500,000 [32mfragments[0m
hits: 64,798,964, hits per frag:  4.83591[A

[32mprocessed[31m 14,000,000 [32mfragments[0m
hits: 67,196,605, hits per frag:  4.82709[A

[32mprocessed[31m 14,500,000 [32mfragments[0m
hits: 69,585,998, hits per frag:  4.83392[A

[32mprocessed[31m 15,000,000 [32mfragments[0m
hits: 72,009,087, hits per frag:  4.83098[A

[32mprocessed[31m 15,500,000 [32mfragments[0m
hits: 74,419,863, hits per frag:  4.84488[A

[32mprocessed[31m 16,000,000 [32mfragments[0m
hits: 76,839,556, hits per frag:  4.83213[A

[32mprocessed[31m 16,500,000 [32mfragments[0m
hits: 79,247,141, hits per frag:  4.84477[A

[32mprocessed[31m 17,000,000 [32mfragments[0m
hits: 81,651,676, hits per frag:  4.84704[A

[32mprocessed[31m 17,500,000 [32mfragments[0m
hits: 84,047,593, hits per frag:  4.82566[A

[32mprocessed[31m 18,000,000 [32mfragments[0m
hits: 86,462,057, hits per frag:  4.84652[A

[32mprocessed[31m 18,500,000 [32mfragments[0m
hits: 88,862,411, hits per frag:  4.8171[A

[32mprocessed[31m 19,000,000 [32mfragments[0m
hits: 91,254,496, hits per frag:  4.86026[A

[32mprocessed[31m 19,500,000 [32mfragments[0m
hits: 93,652,637, hits per frag:  4.83635[A

[32mprocessed[31m 20,000,000 [32mfragments[0m
hits: 96,037,998, hits per frag:  4.84632[A

[32mprocessed[31m 20,500,000 [32mfragments[0m
hits: 98,455,524, hits per frag:  4.83901[A

[32mprocessed[31m 21,000,001 [32mfragments[0m
hits: 100,860,182, hits per frag:  4.82811[A

[32mprocessed[31m 21,500,000 [32mfragments[0m
hits: 103,274,079, hits per frag:  4.85029







[2025-03-05 06:26:01.247] [jointLog] [info] Computed 1,180,055 rich equivalence classes for further processing
[2025-03-05 06:26:01.247] [jointLog] [info] Counted 4,888,723 total reads in the equivalence classes 
[2025-03-05 06:26:01.610] [jointLog] [info] Number of mappings discarded because of alignment score : 241,140,248
[2025-03-05 06:26:01.610] [jointLog] [info] Number of fragments entirely discarded because of alignment score : 2,910,107
[2025-03-05 06:26:01.610] [jointLog] [info] Number of fragments discarded because they are best-mapped to decoys : 0
[2025-03-05 06:26:01.610] [jointLog] [info] Number of fragments discarded because they have only dovetail (discordant) mappings to valid targets : 98,312
[2025-03-05 06:26:03.115] [jointLog] [warning] Only 4888723 fragments were mapped, but the number of burn-in fragments was set to 5000000.
The effective lengths have been computed using the observed mappings.

[2025-03-05 06:26:03.115] [jointLog] [info] Mapping rate = 22.5795%

[2025-03-05 06:26:03.115] [jointLog] [info] finished quantifyLibrary()
[2025-03-05 06:26:03.117] [jointLog] [info] Starting optimizer
[2025-03-05 06:26:17.379] [jointLog] [info] Marked 0 weighted equivalence classes as degenerate
[2025-03-05 06:26:17.860] [jointLog] [info] iteration = 0 | max rel diff. = 99
[2025-03-05 06:26:52.596] [jointLog] [info] iteration = 100 | max rel diff. = 0.127926
[2025-03-05 06:27:30.805] [jointLog] [info] iteration = 200 | max rel diff. = 0.0787947
[2025-03-05 06:28:10.724] [jointLog] [info] iteration = 300 | max rel diff. = 0.0363161
[2025-03-05 06:28:56.620] [jointLog] [info] iteration = 400 | max rel diff. = 0.0243442
[2025-03-05 06:29:42.528] [jointLog] [info] iteration = 500 | max rel diff. = 0.0279507
[2025-03-05 06:30:24.862] [jointLog] [info] iteration = 600 | max rel diff. = 0.0178638
[2025-03-05 06:31:09.701] [jointLog] [info] iteration = 700 | max rel diff. = 0.0150613
[2025-03-05 06:31:54.022] [jointLog] [info] iteration = 800 | max rel diff. = 0.0156326
[2025-03-05 06:32:44.338] [jointLog] [info] iteration = 900 | max rel diff. = 0.010698
[2025-03-05 06:33:23.924] [jointLog] [info] iteration = 984 | max rel diff. = 0.00995188
[2025-03-05 06:33:24.170] [jointLog] [info] Finished optimizer
[2025-03-05 06:33:24.170] [jointLog] [info] writing output 

[2025-03-05 06:33:44.877] [jointLog] [warning] NOTE: Read Lib [[ /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592212/output/trimmed_1.fastq.gz, /home/ec2-user/SageMaker/s3/newatlantis-case-studies-db-prod/PRJNA621969-Nowinski_et_al_2019-PhytoplanktonBloom/DNA/SRR7592212/output/trimmed_2.fastq.gz]] :

Detected a *potential* strand bias > 1% in an unstranded protocol check the file: ../../Analysis/leviathan_output/profiling/DNA/pathway/SRR7592212/intermediate/lib_format_counts.json for details


