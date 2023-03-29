import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
 
setup_requires = [
    ]

install_requires = [
    'Folium==0.14.00',
    'os',
    'pandas==1.5.3', 
    'io',
    'webbrowser'
    ]

dependency_links = [
    'https://github.com/Pandemic23/FCV-ver1.3/tree/main',
    ]

setuptools.setup(
    name="FCV",
    version="0.1.3",
    author="Youngco",
    author_email="popofh12345@naver.com",
    description="Fine dust visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pandemic23/FCV-ver1.3/tree/main",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 