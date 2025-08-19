from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list:
    """
    Reads a requirements file and returns a cleaned list of dependencies.
    - Removes comments (full-line and inline starting with #)
    - Removes blank lines
    - Removes '-e .' if present
    """
    HYPEN_REQUIREMENTS = "-e ."
    requirements = []

    with open(file_path, "r") as file:
        for line in file:
            # Remove inline comments and strip whitespace
            line = line.split("#")[0].strip()
            if line and line != HYPEN_REQUIREMENTS:
                requirements.append(line)

    return requirements

setup(
    name="BasePackage",
    version="0.1",
    author="Mukul Garg",
    author_email="mukulgarg0097@gmail.com",
    description="A base package to reuse for Python-ML projects.",
    packages=find_packages(where="src"),  # src layout
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
