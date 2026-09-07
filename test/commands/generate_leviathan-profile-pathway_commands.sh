#!/usr/bin/env bash
source "$(dirname "$0")/config.sh"
manifest_type="${MANIFEST_TYPE}"

rm -f commands.leviathan-profile-pathway.list
input_directory="../inputs/${manifest_type}"
dataset_directory="../datasets/CAMI-II_Marine_n-100/"
output_directory="../outputs/${manifest_type}"

index_directory="${input_directory}/references/index/"
profiling_directory="${output_directory}/profiling"
mkdir -p ${profiling_directory}
table_format="parquet"

for id in $(cat identifiers.list);
do
	job_name="leviathan-profile-pathway__${id}"
	echo $job_name
	r1="${dataset_directory}/${id}/reads/reads_1.fastq.gz"
	r2="${dataset_directory}/${id}/reads/reads_2.fastq.gz"
	cmd="leviathan-profile-pathway.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=2 -o ${profiling_directory}/pathway/  -f ${table_format}"
	echo $cmd >> commands.leviathan-profile-pathway.list
done
