'''
Author: 饕餮
Date: 2021-12-23 21:23:03
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 11:35:47
Description: setup
'''
from __future__ import print_function
from setuptools import setup,find_packages
import sys

setup(
    name="hunter_sdk",
    version="latest",
    author="spensercai",
    author_email="spensercai@gmail.com",
    description="Hunter SDK",
    long_description="Hunter SDK",
    license="MIT",
    url="https://github.com/SpenserCai/Hunter-SDK",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[

    ],
    install_requires=[

    ],
    zip_safe=True,

)