#### Daily Change Log:
* [2025.3.11] - Added default to transpose tables in `leviathan-merge.py` but added `--no_transpose_taxonomic_profiles` and `--no_transpose_pathway_profiles`
* [2025.3.6] - Added default --output_format for `leviathan-merge.py` to be parquet (which will be transposed relative to tsv and pickle)
* [2025.1.21] - Added `leviathan-merge` module along with adding `merge_taxonomic_profiling_tables` and `merge_pathway_profiling_tables` to `utils`
* [2025.1.18] - Added support for `pykofamsearch-reformatted` and `pyhmmsearch-reformatted` in `leviathan-preprocess.py` and `read_annotations`
* [2025.1.17] - Port functions from `pyexeggutor`
* [2025.1.17] - Added `compile-manifest-from-veba.py` script
* [2024.9.27] - Removed dependency for every genome to require a hit in the feauture mapping table
* [2024.9.23] - Fixed bug where `feature_abundances.genomes.tsv.gz` had multiple rows per feature.
* [2024.9.23] - Replaced `BioPython` with the faster and more lightweight `PyFastx`
* [2024.9.23] - Added pathway support for `leviathan index` and `leviath profile-pathway`.  The latter, outputs pathway abundance and coverage values if a pathway database is available.
* [2024.9.23] - Added `KEGG Pathway Profiler` as dependency which is used for building pathway databases if the input features are KEGG orthologs
* [2024.7.31] - Added `leviathan profile-pathway` but still needs pathway abundance and coverage support.
* [2024.7.30] - Added `leviathan profile-taxonomy`
* [2024.7.26] - Unversioned pre-alpha release on GitHub which only includes utils and index modules.  

#### Pending: 
* Add long read support
* Change `index` to `build-database`

#### Critical:
* Memory profiler is incorrect
