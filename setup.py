from setuptools import setup, find_packages

def get_requirements(file_path:str) -> list:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    HYPEN_REQUIREMENTS = '-e .'

    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip().replace("\n","") for req in requirements if req.strip()]
        requirements = [req for req in requirements if not req.startswith('#')]
    
    if HYPEN_REQUIREMENTS in requirements:
        requirements.remove(HYPEN_REQUIREMENTS)
    # Remove any whitespace characters like `\n` at the end of each line
    return requirements

setup(
    name='BasePackage',
    version='0.1',
    author='Mukul Garg',
    author_email='mukulgarg0097@gmail.com',
    description='A base package to reuse for Python-ML projects.',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)    