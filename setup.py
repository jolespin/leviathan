from setuptools import setup
import os

script_directory = os.path.abspath(os.path.dirname(__file__))

package_name = "leviathan"
version = None
with open(os.path.join(script_directory, package_name, '__init__.py')) as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip().strip('"')
assert version is not None, f"Check version in {package_name}/__init__.py"

setup(name='leviathan',
      version=version,
      description='Genome-resolved taxonomic and pathway profiling',
      url='https://github.com/new-atlantis-labs/leviathan',
      author='Josh L. Espinoza',
      author_email='jolespin@newatlantis.io, jol.espinoz@gmail.com',
      license='GNU AGPL_v3 License',
      packages=["leviathan"],
      install_requires=[
      "pandas",
      "tqdm",
      "memory_profiler",
      "biopython",
      ],
    include_package_data=False,
     scripts=[
       "bin/leviathan-index.py",
        ],

)

