#!/usr/bin/env bash
job_name="leviathan-manifest"
working_directory="../working"
reference_directory="${working_directory}/references"
veba_directory="../../Analysis/veba_output/"
manifest="${reference_directory}/manifest.tsv"
compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest} 2> logs/${job_name}.err 1> logs/${job_name}.out

