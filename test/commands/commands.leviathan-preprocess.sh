#!/usr/bin/env bash
manifest_type="$1"

job_name="leviathan-preprocess"
working_directory="../working/${manifest_type}"
reference_directory="${working_directory}/references"
database_directory="../databases/CAMI-II_Marine_n-100/"
manifest="manifest.${manifest_type}.tsv.gz"
annotations="${database_directory}/analysis/pykofamsearch_output.pathways.tsv.gz"
leviathan-preprocess.py -i ${manifest} -a ${annotations} -o ${reference_directory} --annotation_format pykofamsearch
