import sys
import os

from setuptools import setup

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from scarab import version


def get_version():
    return version


setup(
    name="Scarab", 
    version=get_version(),
    packages=["scarab"],
    install_requires=[
       "FastAPI",
       "jinja2",
    ]
)
