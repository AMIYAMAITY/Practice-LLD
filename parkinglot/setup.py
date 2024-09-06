from setuptools import setup, find_packages

setup(
    name='Setup File',
    version='1.1',
    packages=find_packages(include=['models/*'])
)