#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# package setup
# 
# @author <bprinty@gmail.com>
# ------------------------------------------------


# config
# ------
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import animation

with open('requirements.txt', 'r') as reqs:
    requirements = map(lambda x: x.rstrip(), reqs.readlines())

test_requirements = [
    'nose',
    'nose-parameterized'
]


# files
# -----
with open('README.rst') as readme_file:
    readme = readme_file.read()


# exec
# ----
setup(
    name='animation',
    version=animation.__version__,
    description="Tools for terminal-based await animations",
    long_description=readme,
    author="Blake Printy",
    author_email='bprinty@gmail.com',
    url='https://github.com/bprinty/animation',
    packages=['animation'],
    package_dir={'animation': 'animation'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache-2.0",
    zip_safe=False,
    keywords=['animation', 'wait', 'waiting', 'status'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apple Public Source License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='nose.collector'
)
