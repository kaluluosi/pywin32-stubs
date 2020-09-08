# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from distutils import sysconfig
import sys

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

def create_pth():
    site_package_path = sysconfig.get_python_lib()
    lines = []
    pkg_dir = "pywin32_stubs-0.1.0-py{}.{}".format(*sys.version_info[:2])
    lines.append(os.path.join(pkg_dir, "win32-stubs\n"))
    lines.append(os.path.join(pkg_dir, "pythonwin-stubs\n"))
    lines.append(os.path.join(pkg_dir, "win32comext-stubs\n"))
    lines.append(os.path.join(pkg_dir, "win32helper\n"))
    with open(os.path.join(site_package_path,'pywin32-stubs.pth'), 'w', encoding='utf-8') as f:
        f.writelines(lines)

setup(
    name="pywin32-stubs",
    version="0.1.2",
    description="stubs for pywin32",
    license="MIT",
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
    install_requires=['pywin32'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=False
)

create_pth()