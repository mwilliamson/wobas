#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='wobas',
    version='0.1.0',
    description='wordbucketandspoon.com',
    long_description=read("README"),
    author='Michael Williamson',
    author_email='mike@zwobble.org',
    url='https://github.com/mwilliamson/wobas',
    packages=['wobas'],
    install_requires=[
        "nltk>=2.0.4,<3.0",
        "zuice>=0.2.4,<0.3",
        "funk>=0.3,<0.4",
    ],
    keywords="word bucket spoon",
)
