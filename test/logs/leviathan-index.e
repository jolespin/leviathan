Loading fasta: ../../Analysis/leviathan_output/references/cds.fasta.gz: 0it [00:00, ?it/s]Loading fasta: ../../Analysis/leviathan_output/references/cds.fasta.gz: 20353it [00:00, 203409.92it/s]Loading fasta: ../../Analysis/leviathan_output/references/cds.fasta.gz: 33627it [00:00, 197321.78it/s]
Loading feature mapping with genome clusters: ../../Analysis/leviathan_output/references/feature_mapping.tsv.gz: 0it [00:00, ?it/s]Loading feature mapping with genome clusters: ../../Analysis/leviathan_output/references/feature_mapping.tsv.gz: 9449it [00:00, 94484.91it/s]Loading feature mapping with genome clusters: ../../Analysis/leviathan_output/references/feature_mapping.tsv.gz: 19436it [00:00, 97651.22it/s]Loading feature mapping with genome clusters: ../../Analysis/leviathan_output/references/feature_mapping.tsv.gz: 29202it [00:00, 76272.98it/s]Loading feature mapping with genome clusters: ../../Analysis/leviathan_output/references/feature_mapping.tsv.gz: 33626it [00:00, 82937.28it/s]
Loading genomes: ../../Analysis/leviathan_output/references/genomes.tsv.gz: 0it [00:00, ?it/s]Loading genomes: ../../Analysis/leviathan_output/references/genomes.tsv.gz: 23it [00:00, 170741.58it/s]
Command Successful: /home/ubuntu/jolespin-volume/miniforge3/envs/leviathan/bin/salmon index --keepDuplicates --threads 30 --transcripts ../../Analysis/leviathan_output/references/cds.fasta.gz --index ../../Analysis/leviathan_output/references/index/salmon_index
Writing filepaths: ../../Analysis/leviathan_output/references/index/tmp/genome_filepaths.list:   0%|                                                                                                                                                | 0/23 [00:00<?, ?it/s]Writing filepaths: ../../Analysis/leviathan_output/references/index/tmp/genome_filepaths.list: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 23/23 [00:00<00:00, 432596.38it/s]
Command Successful: /home/ubuntu/jolespin-volume/miniforge3/envs/leviathan/bin/sylph sketch -t 30 --gl ../../Analysis/leviathan_output/references/index/tmp/genome_filepaths.list -o ../../Analysis/leviathan_output/references/index/database/genomes -k 31 --min-spacing 30 -c 200
	Command being timed: "leviathan-index.py -f ../../Analysis/leviathan_output/references/cds.fasta.gz -m ../../Analysis/leviathan_output/references/feature_mapping.tsv.gz -g ../../Analysis/leviathan_output/references/genomes.tsv.gz -d ../../Analysis/leviathan_output/references/index/ -p=-1 --pathway_database /home/ubuntu/jolespin-volume/s3/newatlantis-raw-veba-db-prod/KEGG/v2024.11.11/KEGG-Pathway-Profiler/database.pkl.gz"
	User time (seconds): 751.11
	System time (seconds): 1.37
	Percent of CPU this job got: 1446%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:52.02
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 217932
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 648
	Minor (reclaiming a frame) page faults: 309010
	Voluntary context switches: 36979
	Involuntary context switches: 146020
	Swaps: 0
	File system inputs: 1072
	File system outputs: 602560
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
