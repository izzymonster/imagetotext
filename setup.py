#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'imagetotext',
    'author': 'Izzy Monster',
    'url': 'https://github.com/izzymonster/imagetotext',
    'download_url': 'https://github.com/izzymonster/imagetotext',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['imagetotext'],
    'scripts': [],
    'name': 'imagetotext'
}

setup(**config)
