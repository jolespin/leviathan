#!/usr/bin/env bash
# Create manifest from VEBA
# bash commands.leviathan-manifest.sh

# Preprocess from manifest to get files needed for building index
#bash commands.leviathan-preprocess.sh

# Build index
bash commands.leviathan-index.sh

# Generate the commands for taxonomic profiling and run in parallel
bash generate_leviathan-profile-taxonomy_commands.sh
cat commands.leviathan-profile-taxonomy.list | parallel -j 9
rm -f commands.leviathan-profile-taxonomy.list

# Generate the commands for pathway profiling and run in parallel
bash generate_leviathan-profile-pathway_commands.sh
cat commands.leviathan-profile-pathway.list | parallel -j 9
rm -f commands.leviathan-profile-pathway.list

# Merge sample-specific results into xarray datasets
bash commands.leviathan-merge.sh
