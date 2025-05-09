Command Successful: /home/ubuntu/jolespin-volume/miniforge3/envs/leviathan/bin/sylph sketch -t 30 -k 31 -c 200 --min-spacing 30 -d ../../Analysis/leviathan_output/profiling/taxonomy/S1/intermediate -1 ../../Analysis/veba_output/preprocess/S1/output/trimmed_1.fastq.gz -2 ../../Analysis/veba_output/preprocess/S1/output/trimmed_2.fastq.gz && mv ../../Analysis/leviathan_output/profiling/taxonomy/S1/intermediate/trimmed_1.fastq.gz.paired.sylsp ../../Analysis/leviathan_output/profiling/taxonomy/S1/intermediate/reads.sylsp
Command Successful: /home/ubuntu/jolespin-volume/miniforge3/envs/leviathan/bin/sylph profile --estimate-unknown -t 30 --minimum-ani 95 --min-number-kmers 20 --min-count-correct 3 ../../Analysis/leviathan_output/references/index/database/genomes.syldb ../../Analysis/leviathan_output/profiling/taxonomy/S1/intermediate/reads.sylsp | gzip > ../../Analysis/leviathan_output/profiling/taxonomy/S1/output/sylph_profile.tsv.gz
Getting filepaths associated with genomes:   0%|          | 0/23 [00:00<?, ?it/s]Getting filepaths associated with genomes: 100%|██████████| 23/23 [00:00<00:00, 405331.90it/s]
	Command being timed: "leviathan-profile-taxonomy.py -1 ../../Analysis/veba_output/preprocess/S1/output/trimmed_1.fastq.gz -2 ../../Analysis/veba_output/preprocess/S1/output/trimmed_2.fastq.gz -n S1 -d ../../Analysis/leviathan_output/references/index/ -p=-1 -o ../../Analysis/leviathan_output/profiling/taxonomy/"
	User time (seconds): 5.53
	System time (seconds): 0.19
	Percent of CPU this job got: 114%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:05.01
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 83224
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 290
	Minor (reclaiming a frame) page faults: 66264
	Voluntary context switches: 6666
	Involuntary context switches: 1962
	Swaps: 0
	File system inputs: 0
	File system outputs: 8832
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
