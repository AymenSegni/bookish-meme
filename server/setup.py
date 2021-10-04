from setuptools import find_packages
from setuptools import setup

from pip._internal.req import parse_requirements

requirements = parse_requirements('requirements/dev.txt', session='null')

setup(
    name="server",
    version="0.0.1",
    url="http://aymen-segni.com",
    license="Apache License 2.0",
    maintainer="Aymen Segni",
    maintainer_email="segniaymen1@gmail.com",
    description="Bookish Meme - When you're asked to Terraform Pluto",
    long_description="Simple Containerized Python Application",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[str(requirement.requirement) for requirement in requirements],
    extras_require={"test": ["pytest", "coverage"]},
)