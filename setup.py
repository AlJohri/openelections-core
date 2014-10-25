#!/usr/bin/env python

import sys
from setuptools import setup

# TODO: More informative message about Python version support, version reflected
# classifiers argument to setup(). Perhaps setup should fail altogether for 
# unsupported Python versions.
if sys.version_info < (2,7) or sys.version_info >= (3,):
    print("This package is primarily developed and tested using Python 2.7.*. "
          "It may not not work with older or newer Python distributions.")

setup(
    name='OpenElections Core',
    version='0.1.0',
    author='OpenElections',
    author_email='openelections@gmail.com',
    url='http://openelections.net',
    packages=['openelex'],
    entry_points={
        'console_scripts': [
            'openelex = openelex.tasks:cli',
        ],
    }
)
