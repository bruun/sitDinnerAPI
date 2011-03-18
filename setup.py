from setuptools import setup, find_packages

setup(
    name = "SiT-Dinner-API",
    version = "1.0",
    url = 'http://github.com/bruun/sitDinnerAPI',
    license = 'TBA',
    description = "A simple API to SiT's dinner information.",
    author = 'Thomas Bruun',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)