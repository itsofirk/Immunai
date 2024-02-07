from setuptools import setup, find_packages

setup(
    name='immunai',
    version='1.0.0',
    description='Immunai assignment',
    packages=find_packages(),
    install_requires=[
        'pydantic==2.6.1',
        'pydantic_settings==2.1.0'
    ],
)
