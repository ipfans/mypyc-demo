from mypyc.build import mypycify
from setuptools import setup

setup(
    name="fib",
    version="0.1.0",
    description="A package to compile fib with mypyc for performance improvement",
    ext_modules=mypycify(["fib"], opt_level="3", debug_level="1"),
    packages=["fib"],
    install_requires=["mypy>=1.11.2", "setuptools", "wheel"],
)
