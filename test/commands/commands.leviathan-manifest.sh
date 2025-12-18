#!/usr/bin/env bash
job_name="leviathan-manifest"
working_directory="../working"
reference_directory="${working_directory}/references"
veba_directory="../../Analysis/veba_output/"
manifest="${reference_directory}/manifest.tsv.gz"
compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest}

