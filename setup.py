from typing import List
from setuptools import find_packages, setup

def get_requirements(file_name):
    with open(file_name) as f:
        pakages = f.readlines()
        pakages=[item.replace("\n","") for item in pakages]
    
    return pakages

setup(
name='ml-project5',
version='1.0.0',
author='nilay',
author_email='nilaykarade@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)