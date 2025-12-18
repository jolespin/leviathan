#!/usr/bin/env bash
working_directory="../working"
profiling_directory="${working_directory}/leviathan_output/profiling"
artifact_directory="${working_directory}/leviathan_output/artifacts"
job_name="leviathan-merge"
table_format="parquet"
taxonomy_directory="${profiling_directory}/taxonomy/"
pathway_directory="${profiling_directory}/pathway/"
leviathan-merge.py -t ${taxonomy_directory} -p ${pathway_directory} -o ${artifact_directory} -f ${table_format}


