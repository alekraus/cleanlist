import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cleanlist',
    version='0.1.0',
    author='Alejandro Krauskopf',
    author_email='alekraus@gmail.com',
    description='Package for cleaning lists of times or floats as strings',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alekraus/cleanlist',
    project_urls = {
        "Issues Tracker": "https://github.com/alekraus/cleanlist/issues"
    },
    license='MIT',
    packages=['cleanlist'],
    install_requires=[],
)