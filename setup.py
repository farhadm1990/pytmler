from setuptools import setup, find_packages


setup(

    name="pytmler",
    version="0.1.2",
    url='https://github.com/farhadm1990/pytmler',
    author="Farhad M. Panah",
    author_email="farhad@food.ku.dk",
    packages=find_packages(),
    install_requires=["jinja2", "datetime", "pandas", "numpy", "requests", "beautifulsoup4", "pygments"],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]

)



