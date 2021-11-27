#!/usr/bin/env python
"""Raesymatto."""
import os
from distutils.core import setup

import raesymatto

# read the long description
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'README.md'),encoding='utf-8') as f:
    long_description = f.read()

# read the package requirements
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'requirements.txt'),encoding='utf-8') as f:
    install_requires = f.read().splitlines()

setup(name='raesymatto',
      version=raesymatto.__version__,
      description='Raesymatto: visualize genomic data',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author=raesymatto.__author__,
      url='https://github.com/tare/raesymatto',
      license=raesymatto.__license__,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Other Audience',
          ('License :: OSI Approved :: BSD 3-Clause "New" or '
           '"Revised" License (BSD-3-Clause)'),
          'Programming Language :: Python :: 3'],
      packages=['raesymatto'],
      install_requires=install_requires
)
