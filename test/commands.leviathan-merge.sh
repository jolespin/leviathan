case_study="TestCaseStudy"
case_study_directory="../../"

job_name="leviathan-merge"
/usr/bin/time -v leviathan-merge.py -t ${case_study_directory}/Analysis/leviathan_output/profiling/taxonomy/ -p ${case_study_directory}/Analysis/leviathan_output/profiling/pathway/ -o ../../Analysis/leviathan_output/artifacts/ 2> logs/${job_name}.e 1> logs/${job_name}.o


