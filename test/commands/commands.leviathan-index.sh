#!/usr/bin/env bash
source "$(dirname "$0")/config.sh"
manifest_type="${MANIFEST_TYPE}"

job_name="leviathan-index"

# Datasets
dataset_directory="../datasets/CAMI-II_Marine_n-100/"

# Databases
mkdir -p ../databases/
pathway_database="../databases/KEGG-Pathway-Profiler/database.pkl.gz"

# Output Directories
input_directory="../inputs/${manifest_type}"
reference_directory="${input_directory}/references"
index_directory="${reference_directory}/index/"

# Inputs
fasta="${reference_directory}/cds.fasta.gz"
feature_mapping="${reference_directory}/feature_mapping.tsv.gz"
genomes="${reference_directory}/genomes.tsv.gz"

# Fetch KEGG Pathway database
build-pathway-database.py --ebi latest -d ${pathway_database}

# Run
leviathan-index.py -f ${fasta} -m ${feature_mapping} -g ${genomes} -d ${index_directory} -p=-1 --pathway_database ${pathway_database}
