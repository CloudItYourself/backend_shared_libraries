from setuptools import setup, find_packages

setup(
    name="tpc_backend_libraries",
    version="0.0.1",
    packages=find_packages(),
    install_requires=['pydantic', 'websockets', 'aioboto']
)
