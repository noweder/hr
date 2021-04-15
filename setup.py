# This will call the setuptools module, then import the setup and find_packages functions from it
from setuptools import setup, find_packages

# This will read the package description from our README.md file
with open('README.md' encoding='UTF-8') as f:
    readme = f.read()

# This will actually do the calling out to setup, and set some of the information about the package itself
setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Hamza Noweder',
    author_email='hmnoweder@gmail.com',
    # This will define where to look for the package itself. We are pointing find_packages at the local src directory
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[],
    # This is essentially saying: When you are installed, create an executable named hr, that will call the "main" method inside the "cli" module, inside of the "hr" package.
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
