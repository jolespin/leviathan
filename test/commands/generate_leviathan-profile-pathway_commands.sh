#!/usr/bin/env bash
rm -f commands.leviathan-profile-pathway.list
working_directory="../working"
database_directory="../databases/CAMI-II_Marine_n-100/"

index_directory="${working_directory}/references/index/"
profiling_directory="${working_directory}/leviathan_output/profiling"
mkdir -p ${profiling_directory}
table_format="parquet"

for id in $(cat identifiers.list);
do
	job_name="leviathan-profile-pathway__${id}"
	echo $job_name
	r1="${database_directory}/${id}/reads/reads_1.fastq.gz"
	r2="${database_directory}/${id}/reads/reads_2.fastq.gz"
	cmd="leviathan-profile-pathway.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=2 -o ${profiling_directory}/pathway/  -f ${table_format}"
	echo $cmd >> commands.leviathan-profile-pathway.list
done
