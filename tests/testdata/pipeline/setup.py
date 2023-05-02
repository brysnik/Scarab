from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='test_pipeline',
    version='0.0.1',
    description='Test pipeline',
    author='Test',
    find_packages=find_packages(str(Path(__file__).parent / "src")),
    install_requires=[
        "numpy", #  get some ugly stuff
        "scipy",
        "PIL",
        "matplotlib"
    ]
)