from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='aeroapi-python',
    version='0.0.11',
    author='Deren S',
    author_email='derens99@gmail.com',
    description='FlightAware AeroAPI Caller for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",  # This field indicates that your long_description is in Markdown.
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
