## Downloading Fastq
### Downloading fastq from SRA
If you want to use on samples from SRA, you can download them like this:

#### Option 1: `xsra` (faster)
##### Install `cargo`
```
curl https://sh.rustup.rs -sSf | sh

# Initialize
. "$HOME/.cargo/env"            # For sh/bash/zsh/ash/dash/pdksh
```

##### Install `xsra`
Confirm that `cmake` is installed (e.g., `brew install cmake` or `sudo apt-get install cmake` or `mamba install -c conda-forge cmake` or )
```
cargo install xsra
```

##### Download Fastq
```
n_threads=14
fastq_directory="../fastq"
mkdir -p ${fastq_directory}
for id in $(cat ../identifiers.list);
do
    xsra dump \
    -o ${fastq_directory} \
    -c g \
    -s \
    --prefix ${id}_ \
    -T ${n_threads} \
    ${id}
done
```
##### Relabel Files
This step will be deprecated eventually given [xsra issue/#54](https://github.com/ArcInstitute/xsra/issues/54)

```
for id in $(cat ../identifiers.list);
do
    mv ${fastq_directory}/${id}_0.fq.gz ${fastq_directory}/${id}_1.fastq.gz 
    mv ${fastq_directory}/${id}_1.fq.gz ${fastq_directory}/${id}_2.fastq.gz 
done
```

#### Option 2: `kingfisher` (easier for now)
##### Install `kingfisher`
```
mamba activate leviathan
mamba install -c bioconda kingfisher
```

##### Download Fastq

```
n_threads=14
fastq_directory="../fastq"
mkdir -p ${fastq_directory}
for id in $(cat ../identifiers.list);
do
    kingfisher get \
    -r ${id} \
    --output-directory  ${fastq_directory} \
    -m aws-http \
    -f fastq.gz

done
```
