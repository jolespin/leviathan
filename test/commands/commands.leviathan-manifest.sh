#!/usr/bin/env bash
manifest_type="$1"

job_name="leviathan-manifest"
working_directory="../working/${manifest_type}"
reference_directory="${working_directory}/references"
veba_directory="../../Analysis/veba_output/"
manifest="${reference_directory}/manifest.${manifest_type}.tsv.gz"
compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest}

