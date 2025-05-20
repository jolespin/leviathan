#### Daily Change Log:
* (UNTESTED) [2025.5.18] - Added `--salmon_include_mappings` to `profile-pathway.py` and `run_salmon_quant`
* (UNTESTED) [2025.5.18] - Added `taxonomic_abundance` and `sequence_abundance` levels to `taxonomic_abundance.*.parquet` files from `leviathan-merge.py`
* [2025.5.9] - Added `sequence_abundance.genomes.parquet` and `sequence_abundance.genome_clusters.parquet` to `leviathan-profile-taxonomy.py`
* [2025.3.13] - Added `-f/--output_format` to `profile-taxonomy.py` and `profile-pathway.py` modules with `parquet` as default but continued support for `.tsv`
* [2025.3.13] - Dropped gene_abundance merging because files are too big, sparse, and probably not that useful...
* [2025.3.12] - Added `h5netcdf` to `requirements.txt`
* [2025.3.12] - Removed option for output formats in `leviathan-merge.py`.  Taxonomic profiles are `pandas` stored as `parquet` and pathway profiles are `xarray` stored as `netcdf` files.
* [2025.3.12] - Changed `merge_taxonomic_profiling_tables` to `merge_taxonomic_profiling_tables_as_pandas`
* [2025.3.12] - Changed `merge_pathway_profiling_tables` to `merge_pathway_profiling_tables_as_pandas` and created `merge_pathway_profiling_tables_as_xarray`
* [2025.3.12] - Moved `merge_pathway_profiling_tables` from `utils` to `profile_pathway`
* [2025.3.12] - Moved `merge_taxonomic_profiling_tables` from `utils` to `profile_taxonomy`
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
* ! No support for gene_abundances.  Must figure out how to gzip .nc
* Add long read support
* Change `index` to `build-database`

#### Critical:
* Memory profiler is incorrect
