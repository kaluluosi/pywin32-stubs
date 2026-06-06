# -*- coding: utf-8 -*-
from setuptools import setup

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""


setup(
    name="pywin32-stubs",
    version="1.0.8",
    description="DEPRECATED: use types-pywin32 instead (https://pypi.org/project/types-pywin32/)",
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
        "Development Status :: 7 - Inactive",
    ],
    zip_safe=False
)
