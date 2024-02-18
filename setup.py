from setuptools import setup, find_packages

setup(
    name="ciy_backend_libraries",
    version="0.0.7",
    packages=find_packages(),
    install_requires=['pydantic', 'websockets', 'aioboto3', 'axiom-logger', 'pymongo', 'certifi']
)
