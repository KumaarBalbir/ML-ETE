# setup.py will be responsible for creating the machine learning model as package.
from setuptools import find_packages, setup
from typing import List

# find_packages() will go and see how many folders have __init__.py file and build it as packages

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements


setup(
    name='ml_ete',
    version='0.1',
    author='Balbir',
    author_email='prasadbalbir1056@gmail.com',
    description='Machine Learning end to end project',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
