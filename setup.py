# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('goto-commandline-tool/goto.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "goto",
    packages = ["goto-commandline-tool"],
    entry_points = {
        "console_scripts": ['goto = goto-commandline-tool.goto:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Caleb Hering",
    author_email = "cmhering1@gmail.com"
    #url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    )
