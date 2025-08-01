from setuptools import setup, find_packages

with open("requirements.txt") as f:
    reqs = f.read().splitlines()

setup(
    name="Project01",
    version="0.1",
    author="Davann Tet",
    author_email="davanncr@gmail.com",
    install_requires=reqs,
    packages=find_packages(),
)