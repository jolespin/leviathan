#!/usr/bin/env bash
source "$(dirname "$0")/config.sh"
manifest_type="${MANIFEST_TYPE}"

job_name="leviathan-preprocess"
input_directory="../inputs/${manifest_type}"
reference_directory="${input_directory}/references"
dataset_directory="../datasets/CAMI-II_Marine_n-100/"
manifest="manifest.${manifest_type}.tsv.gz"
annotations="${dataset_directory}/analysis/pykofamsearch_output.pathways.tsv.gz"
leviathan-preprocess.py -i ${manifest} -a ${annotations} -o ${reference_directory} --annotation_format pykofamsearch
