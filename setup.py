#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-yapf',
    version='0.1.1',
    author='Roman Osipenko',
    author_email='roman.osipenko@djangostars.com',
    maintainer='Roman Osipenko',
    maintainer_email='roman.osipenko@djangostars.com',
    license='MIT',
    url='https://github.com/django-stars/pytest-yapf',
    description='Run yapf',
    long_description=read('README.rst'),
    py_modules=['pytest_yapf'],
    install_requires=['pytest>=3.1.1', 'yapf>=0.16.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'yapf = pytest_yapf',
        ],
    },
)
