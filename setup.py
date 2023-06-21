from setuptools import setup
from typing import List


#Declearing variables for setup functions


project_name ="housing-predictor"
version = "0.0.2"
author = "Vishal"
description = "this is my first live project"
packages = ["housing"]
requirement_file = "requirements.txt"



def get_requirements_list()->List[str]:

    """
    this function is going to return list of requirements
    mention in requirements.txt file
    """

    with open(requirement_file) as rfile:
        return rfile.readlines()

setup(
name = project_name,
version = version,
author = author,
description = description,
packages = packages,
install_requires = get_requirements_list()
)


