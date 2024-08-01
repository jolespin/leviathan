# Leviathan
`Leviathan` is a fast, memory-efficient, and scalable taxonomic and pathway profiler for next generation sequencing (genome-resolved) metagenomics and metatranscriptomics.  `Leviathan` is powered by `Salmon` and `Sylph` in the backend.

## Modules
* `leviathan preprocess` - Preprocesses data into form than can be used for `leviathan index`
* `leviathan index` - Build, update, and validate leviathan database
* `leviathan info` - Report information about `leviathan` database
* `leviathan profile-taxonomy` - Profile taxonomy using `Sylph` with leviathan database
* `leviathan profile-pathway` - Profile pathways using `Salmon` with leviathan database
* `leviathan profile-targeted` - Profile taxonomy and pathways uing targeted approach which runs `profile-taxonomy` then gets the subset of detected genomes, builds a targeted Salmon index, then runs `profile-pathway`
* [?] `leviathan end-to-end` - Complete end-to-end pipeline which builds database, profiles, and converts tables

## Development Stage:
* `pre-alpha`