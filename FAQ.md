# Frequently Asked Questions
## 1. Is it required to run `leviathan-profile-taxonomy` before `leviathan-profile-pathway` or vice versa? 
No, they are functionally independent.  However, you can always filter the pathway profiling results by taxonomic filters post hoc. 

```python
# Load taxonomic profiling
ds_taxonomic = xr.open_dataset("leviathan_output/artifacts/taxonomic_abundances.genome_clusters.nc")

# Load functional profiling
ds_pathway = xr.open_dataset("leviathan_output/artifacts/pathway.genome_clusters.nc")

# Get (pan)genomes to retain from taxonomic abundances
minimum_samples_detected = 2
retained_organisms = (ds_taxonomic["taxonomic_abundances"].to_pandas() > 0).sum(axis=0)[lambda x: x >= minimum_samples_detected].index

# Filter functional profiling with taxonomic abundance gate
ds_pathway_filtered = ds_pathway.sel(genome_clusters=retained_organisms)
```
## 2. How can I estimate the reference coverage (i.e., percent of assigned reads)?
```python
# Load taxonomic profiling
ds_taxonomic = xr.open_dataset("leviathan_output/artifacts/taxonomic_abundances.genome_clusters.nc")

# Sum the sequence abundances (not taxonomic abundances)
percent_assigned_reads = ds_taxonomic["sequence_abundances"].sum(axis=1).to_pandas()
percent_unassigned_reads = 100 - percent_assigned_reads
```
## 3. Do I need my own genomes or are there reference catalogs?
