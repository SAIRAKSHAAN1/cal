from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest==7.4.3",
        "pytest-cov==4.1.0",
    ],
) 