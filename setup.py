from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function will return list of e=requirements
    """
    requirement_list:List[str] =[]
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        return requirement_list

print(get_requirements())
setup(
    name="networksecurity",
    version="0.0.1",
    author="saisreenivas",
    author_email="sreenivassaiaic@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)