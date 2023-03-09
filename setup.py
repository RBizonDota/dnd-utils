import os
from setuptools import setup

from dnd_utls import __app_name__, __version__

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = __app_name__,
    version = __version__,
    author = "rbizondota",
    author_email = "rbaybarin@gmail.com",
    description = ("Number of utils, that provides utils for DnD"),
    license = "BSD",
    install_requires=['pydantic'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)