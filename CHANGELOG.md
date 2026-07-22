#### Daily Change Log:
* [2026.7.22] - Changed the `KEGG Pathwayer Profiler` database downloader in `leviathan-index.py`/`index.py` to use EBI's `kegg-pathways-completeness-tool`.
* [2026.7.16] - Added parallelization support for pathway coverage using `profile_pathway_coverage` from `kegg_pathway_profiler>=2026.7.16` in `leviathan-profile-pathway.py`. The `--n_jobs` flag now applies to both `salmon quant` and pathway coverage computation.
* [2026.7.16] - Added `--deterministic` flag to `leviathan-profile-pathway.py` which passes `--deterministic` to `salmon quant` for byte-identical results across runs and thread counts.
* [2026.7.8] - Added `--update_salmon_index` to `leviathan-index.py` and remove `-u` alias on `--update_with_genomes`
* [2026.7.8] - **BREAKING CHANGE:** `Salmon` is reimplemented with `Rust` from `C++` so any `Leviathan` databases using `Salmon 1.x` will need to be updated.  `Leviathan` now requires `Salmon ≥ 2.x`.
* [2026.3.11] - Added support for `-r/--single_reads` in both `profile-taxonomy.py` and `profile-pathway.py`. However, the `profile-pathway.py` needs `oarfish` to use long reads but there are no synthetic long-read metatranscriptomics to benchmark. [issue/#24](https://github.com/jolespin/leviathan/issues/24)
* [2026.3.10] - Added `--veba_major_version` to `compile-manifest-from-veba.py` since `cluster` output directory is changing
* [2026.3.3] - Added `step_coverage` output files [issue/#22](https://github.com/jolespin/leviathan/issues/22)
* [2025.12.17] - Added `--table_format parquet|tsv` to `leviathan-merge.py` and merge functions in `leviathan-profile-pathway.py`/`leviathan-profile-taxonomy.py` [Issue #20](https://github.com/jolespin/leviathan/issues)
* [2025.12.2] - Updated `xarray` concatenation to prepare for usage change in future versions [issue/#17](https://github.com/jolespin/leviathan/issues/17)
* [2025.12.2] - Fixed [issue/#15](https://github.com/jolespin/leviathan/issues/15) where `parquet` files weren't being created when user is not using genome clusters (i.e., 4 column input).  Related to [issue/#18](https://github.com/jolespin/leviathan/issues/18) where `contains_genome_cluster_mapping` was set to `True` even when genome clusters were not provided.
* [2025.12.1] - Fixed [issue/#16](https://github.com/jolespin/leviathan/issues/16) where `feature_prevalence` and `feature_prevalence-binary` output the same values.  Needed to provide `df_gene_abundance` instead of `df_feature_abundance`
* [2025.7.10] - Updated `MIT` to `Apache 2.0`
* [2025.7.3] - Remove genomes that do not have features in `leviathan-preprocess.py` and write excluded genomes to `genomes_excluded.list`.  Also checks in `leviathan-index.py` to make sure genomes in `feature_mapping.tsv.gz` matches those in `genomes.tsv.gz`
* [2025.7.1] - Adding gzipping as an option to maintain consistent runtime benchmarking and removing `aux_info/unmapped_names.txt` from `Salmon` output
* [2025.6.30] - Gzipped `quant.sf` from `Salmon` [Issue #12](https://github.com/jolespin/leviathan/issues/12)
* [2025.6.27] - Updated `--sylph_profile_minimum_number_kmers 20` to `--sylph_profile_minimum_number_kmers 50`
* [2025.5.18] - Added `--salmon_include_mappings` to `profile-pathway.py` and `run_salmon_quant`
* [2025.5.18] - Added `taxonomic_abundance` and `sequence_abundance` levels to `taxonomic_abundances.*.nc` files from `leviathan-merge.py`
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


#### Bugs:
* Memory profiler is incorrect
