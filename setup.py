from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function will return the List of Requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## Read Lines From the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                 ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                   requirement_lst.append(requirement)

    except FileNotFoundError:
       print("requirements.txt file not Found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sarthya Prakash",
    author_email="sarthyaprakash2007@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
