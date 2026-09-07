#!/usr/bin/env bash
source "$(dirname "$0")/config.sh"
manifest_type="${MANIFEST_TYPE}"

output_directory="../outputs/${manifest_type}"
profiling_directory="${output_directory}/profiling"
artifact_directory="${output_directory}/artifacts"
job_name="leviathan-merge"
table_format="parquet"
taxonomy_directory="${profiling_directory}/taxonomy/"
pathway_directory="${profiling_directory}/pathway/"
leviathan-merge.py -t ${taxonomy_directory} -p ${pathway_directory} -o ${artifact_directory} -f ${table_format}
