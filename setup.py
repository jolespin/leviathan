from setuptools import setup

exec(open('leviathan/__init__.py').read())

setup(name='leviathan',
      version=__version__,
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
         ],

)

