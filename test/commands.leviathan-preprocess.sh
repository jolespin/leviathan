job_name="leviathan-preprocess"
manifest="../../Analysis/leviathan_output/references/manifest.tsv"
annotations="../../Analysis/veba_output/annotation/intermediate/8__pykofamsearch/output.tsv.gz"
output_directory="../../Analysis/leviathan_output/references/"
/usr/bin/time -v leviathan-preprocess.py -i ${manifest} -a ${annotations} -o ${output_directory} --annotation_format pykofamsearch-reformatted 2> logs/${job_name}.e 1> logs/${job_name}.o
