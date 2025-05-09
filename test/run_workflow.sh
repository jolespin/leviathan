bash commands.leviathan-manifest.sh
bash commands.leviathan-preprocess.sh
bash commands.leviathan-index.sh

bash generate_leviathan-profile-taxonomy_commands.sh
cat commands.leviathan-profile-taxonomy.list | parallel -j 4

bash generate_leviathan-profile-pathway_commands.sh
cat commands.leviathan-profile-pathway.list | parallel -j 4

bash commands.leviathan-merge.sh
