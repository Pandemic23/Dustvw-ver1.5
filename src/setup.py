import setuptools
from setuptools import setup, find_packages

 
#setup_requires = [
  #  ]

#install_requires = [
   # 'Folium==0.14.00',
   # 'os',
  #  'pandas==1.5.3', 
  #  'io',
 #   'webbrowser'
 #   ]

#dependency_links = [
 #   'https://github.com/Pandemic23/FCV-ver1.3/tree/main',
 #   ]

setuptools.setup(
    name="FCV",
    version="0.1.3",
    author="Youngco",
    author_email="popofh12345@naver.com",
    description="Fine dust visualization",
    url="https://github.com/Pandemic23/FCV-ver1.3/tree/main",
    packages=setuptools.find_packages(),
    install_requires=['Folium==0.14.00',
    'os',
    'pandas==1.5.3', 
    'io',
    'webbrowser'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['FCV']
) 