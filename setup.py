# Project Management
from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name = "Hotel Reservation Prediction",
    version = "0.1",
    author = "Pranay",
    packages = find_packages(), # finds all packages (the ones that we set up using __init__.py)
    install_requires = requirements,
)

# to run this file -> pip install -e .