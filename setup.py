# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from distutils import sysconfig
import sys

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""


setup(
    name="pywin32-stubs",
    version="0.1.6",
    description="stubs for pywin32",
    license="MIT",
    url=" https://pypi.org/project/pywin32-stubs/",
    author="Carlos Teng",
    author_email ="303359166@qq.com",
    keywords=["pywin32", "stubs"],
    packages=["win32-stubs", "pythonwin-stubs", "win32comext-stubs", "win32helper"],
    package_data={
        "win32-stubs":["*.py", "*.pyi"],
        "pythonwin-stubs":["*.py", "*.pyi"],
        "win32comext-stubs":["*.py", "*.pyi"],
        "win32helper":["*.py", "*.pyi"]
        },
    data_files=[("Lib/site-packages",["pywin32-stubs.pth"])],
    install_requires=['pywin32'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=False
)
