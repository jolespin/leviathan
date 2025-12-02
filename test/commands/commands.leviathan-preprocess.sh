#!/usr/bin/env bash
job_name="leviathan-preprocess"
working_directory="../working/"
reference_directory="${working_directory}/references"
# manifest="manifest.with_pangenomes.tsv.gz"
manifest="manifest.no_pangenomes.tsv.gz"
annotations="../databases/CAMI-II_Marine_n-100/analysis/pykofamsearch_output.pathways.tsv.gz"
leviathan-preprocess.py -i ${manifest} -a ${annotations} -o ${reference_directory} --annotation_format pykofamsearch 2> logs/${job_name}.err 1> logs/${job_name}.out
