from setuptools import find_packages, setup

__version__ = "0.0.0"

REPO_NAME = "Medical-ChatBot_GenAI"
AUTHOR_USER_NAME = "adityakr38"
AUTHOR_EMAIL = "kumaraditya233007@gmail.com"

setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    packages= find_packages(),
    install_requires = []
)