import setuptools as setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='nepali-municipalities',
    version='1.0.0',  # Required
    description='Nepali  municipalities is a python package to get data about Nepali municipalities based on districts ',
    url='https://github.com/shuds13/pyexample',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Navaraj Pokharel',
    author_email='navarajpokharel@outlook.com',
    license='BSD 2-clause',
    packages=setuptools.find_packages(),
    install_requires=[],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['Nepali', 'nepali districts', 'nepali municipalities', 'navaraj pokharel', 'nepali states'],
    python_requires='>=3.6',

)

