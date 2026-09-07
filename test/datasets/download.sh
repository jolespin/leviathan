url="https://zenodo.org/records/17783338/files/CAMI-II_Marine_n-100.tar.gz?download=1"
database_directory="."
curl -L "${url}" | tar -xz -C ${database_directory}
