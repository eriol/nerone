#!/usr/bin/env python

from setuptools import setup


setup(
    name='nerone',
    version='0.1.0',
    author='Daniele Tricoli',
    author_email='eriol@mornie.org',
    url='https://github.com/eriol/nerone',
    packages=[
        'nerone',
    ],
    install_requires=[
        'PyInstaller>=3.2',
        'click>=6.6',
    ],
    entry_points={
        'console_scripts': [
            'nerone = nerone.cli:main',
        ]
    },
    license='GPL-2+',
)
