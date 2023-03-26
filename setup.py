from setuptools import setup , find_packages
from typing import List

##conda activate ./envs to activate the specified the conda environment
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the description of list
    """
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Personalitytest',
    version='0.0.1',
    author='Vishal',
    author_email='gaikwadvishal114@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)

