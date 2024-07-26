# Leviathan
`Leviathan` is a fast, memory-efficient, and scalable taxonomic and pathway profiler for next generation sequencing (genome-resolved) metagenomics and metatranscriptomics.  `Leviathan` is powered by `Salmon` and `Sylph` in the backend.

## Modules
* `leviathan preprocess` - Preprocesses data into form than can be used for `leviathan index`
* `leviathan index` - Build, update, and check leviathan database
* `leviathan info` - Report information about leviathan database
* `leviathan profile-taxonomy` - Profile taxonomy using `Sylph` with leviathan database (provide --subset option for only using certain genomes)
* `leviathan profile-pathway` - Profile pathways using `Salmon` with leviathan database (provide --subset option for only using certain genomes)
* `leviathan convert` - Convert abundance tables (e.g., format for `metabolic_niche_space`)
* `leviathan end-to-end` - Complete end-to-end pipeline which builds database, profiles, and converts tables

## Development Stage:
* `pre-alpha`