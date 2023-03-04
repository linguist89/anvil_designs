from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/linguist89/anvil_designs',
    author='Stephan Smuts',
    author_email='smuts1989@gmail.com',

    py_modules=['my_pip_package'],
)