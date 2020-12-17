#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='git-jock',
    # This will be updated automatically
    version='0.2.0',
    author='Gavin Fenton',
    author_email='contact@gavinfenton.com',
    description='Git helper for multi-repository management',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    python_requires='>=3.7',
)
