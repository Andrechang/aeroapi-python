from setuptools import setup, find_packages

setup(
    name='aeroapi-python',
    version='0.0.11',
    author='Deren S',
    author_email='derens99@gmail.com',
    description='FlightAware AeroAPI Caller for Python',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
