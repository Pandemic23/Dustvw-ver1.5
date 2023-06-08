from setuptools import setup, find_packages

 


#install_requires = [
   # 'Folium==0.14.00',
   # 'os',
  #  'pandas==1.5.3', 
  #  'io',
 #   'webbrowser',
 # 'urllib.request'
 #   ]



setup(name="Dustvw",
    version="0.1.7",
    author="Youngco",
    author_email="popofh12345@naver.com",
    description="Fine dust visualization",
    url="https://github.com/Pandemic23/FCV-ver1.5",
    install_requires=['Folium','pandas' ],
    packages=['Dustvw'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    )