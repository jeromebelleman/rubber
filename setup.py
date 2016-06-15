#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='rubber',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Talk to Elasticsearch",
    long_description="Talk to the Elasticsearch REST API.",
    scripts=['rubber'],
    data_files=[],
)
