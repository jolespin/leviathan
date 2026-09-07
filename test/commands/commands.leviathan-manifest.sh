#!/usr/bin/env bash
source "$(dirname "$0")/config.sh"
manifest_type="${MANIFEST_TYPE}"

job_name="leviathan-manifest"
input_directory="../inputs/${manifest_type}"
reference_directory="${input_directory}/references"
veba_directory="../../Analysis/veba_output/"
manifest="manifest.${manifest_type}.tsv.gz"
compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest} --veba_major_version 2
