from setuptools import setup, find_packages

setup(
    name="stats",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author="Cristian",
    author_email="crislm1322@gmail.com",
    description="A package for statistics",
    python_requires=">=3.9",
)
