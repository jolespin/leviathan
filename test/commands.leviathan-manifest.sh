job_name="leviathan-manifest"
veba_directory="../../Analysis/veba_output/"
manifest="../../Analysis/leviathan_output/references/manifest.tsv"
/usr/bin/time -v compile-manifest-from-veba.py -i ${veba_directory} -t prokaryotic,eukaryotic -o ${manifest} 2> logs/${job_name}.e 1> logs/${job_name}.o

