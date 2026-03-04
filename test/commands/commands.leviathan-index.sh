#!/usr/bin/env bash
manifest_type="$1"

job_name="leviathan-index"

# Databases
database_directory="../databases/CAMI-II_Marine_n-100/"
pathway_database="${HOME}/Databases/KEGG-Pathway-Profiler/database.pkl.gz"

# Output Directories
working_directory="../working/${manifest_type}"
reference_directory="${working_directory}/references"
index_directory="${reference_directory}/index/"

# Inputs
reference_directory="${working_directory}/references"
fasta="${reference_directory}/cds.fasta.gz"
feature_mapping="${reference_directory}/feature_mapping.tsv.gz"
genomes="${reference_directory}/genomes.tsv.gz"

# Run
leviathan-index.py -f ${fasta} -m ${feature_mapping} -g ${genomes} -d ${index_directory} -p=-1 --pathway_database ${pathway_database}
