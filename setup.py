from setuptools import setup, find_packages

setup(
    name='aeroapi-python',
    version='0.0.1',
    author='Deren S',
    author_email='derens99@gmail.com',
    description='FlightAware AeroAPI Caller for Python',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
    