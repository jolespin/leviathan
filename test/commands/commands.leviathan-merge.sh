#!/usr/bin/env bash
working_directory="../working"
profiling_directory="${working_directory}/leviathan_output/profiling"
artifact_directory="${working_directory}/leviathan_output/artifacts"
job_name="leviathan-merge"
leviathan-merge.py -t ${profiling_directory}/taxonomy/ -p ${profiling_directory}/pathway/ -o ${artifact_directory} 2> logs/${job_name}.err 1> logs/${job_name}.out


