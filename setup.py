#!/usr/bin/env python

try:
      from setuptools import setup
except ImportError:
      from distutils.core import setup

setup(name='VUA_pylib',
      version='1.0',
      description='Library in python with includes several functionalities for dealing with NAF/KAF files',
      author='Ruben Izquierdo',
      author_email='rubensanvi@gmail.com',
      url='https://github.com/cltl/VUA_pylib',
      packages = ['VUA_pylib', 'VUA_pylib.lexicon', 'VUA_pylib.common', 'VUA_pylib.io', 'VUA_pylib.corpus_reader'],
      data_files = [('VU_pylib/lexicon/data', [])],
      package_data={"VUA_pylib.lexicon": ["data/subj*"]},
      install_requires = ['lxml', 'KafNafParserPy']
)

      
      
