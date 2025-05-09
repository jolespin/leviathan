s3_path="/home/ubuntu/jolespin-volume/s3"
job_name="leviathan-index"
fasta="../../Analysis/leviathan_output/references/cds.fasta.gz"
feature_mapping="../../Analysis/leviathan_output/references/feature_mapping.tsv.gz"
genomes="../../Analysis/leviathan_output/references/genomes.tsv.gz"
index_directory="../../Analysis/leviathan_output/references/index/"
pathway_database="${s3_path}/newatlantis-raw-veba-db-prod/KEGG/v2024.11.11/KEGG-Pathway-Profiler/database.pkl.gz"
/usr/bin/time -v  leviathan-index.py -f ${fasta} -m ${feature_mapping} -g ${genomes} -d ${index_directory} -p=-1 --pathway_database ${pathway_database} 2> logs/${job_name}.e > logs/${job_name}.o
