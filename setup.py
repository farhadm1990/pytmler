from setuptools import setup, find_packages


setup(

    name="pytmler",
    version="0.0.1",
    url='https://github.com/farhadm1990/pytmler',
    author="Farhad M. Panah",
    author_email="farhad@food.ku.dk",
    packages=find_packages(),
    install_requires=["jinja2", "datetime", "pandas", "numpy", "requests", "beautifulsoup4"]

)



