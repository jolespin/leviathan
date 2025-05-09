# DNA
rm -f commands.leviathan-profile-pathway.list
index_directory="../../Analysis/leviathan_output/references/index/"
for id in $(cat ../../identifiers.list);
do
	job_name="leviathan-profile-pathway__${id}"
	echo $job_name
        r1="../../Analysis/veba_output/preprocess/${id}/output/trimmed_1.fastq.gz"
        r2="../../Analysis/veba_output/preprocess/${id}/output/trimmed_2.fastq.gz"
	cmd="/usr/bin/time -v leviathan-profile-pathway.py -1 ${r1} -2 ${r2} -n ${id} -d ${index_directory} -p=-1 -o ../../Analysis/leviathan_output/profiling/pathway/  2> logs/${job_name}.e > logs/${job_name}.o"
	echo $cmd >> commands.leviathan-profile-pathway.list
done
