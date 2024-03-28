# To build our ML application as a package itself and deploy so that anyone else can use

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT  = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    This returns list of requirements
    '''
    requirements = []
    with  open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='SK',
    author_email='shubhamkrs2001@gamil.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
                      
)

