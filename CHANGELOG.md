#### Daily Change Log:
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
* Port functions from `pyexeggutor`

#### Critical:
* Memory profiler is incorrect