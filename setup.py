#!/usr/bin/python3

"""Setup for pyxstitch."""

from setuptools import setup
import os

__pkg_name__ = "pyxstitch"
with open(os.path.join(__pkg_name__, "version.py")) as v_file:
    exec(v_file.read())

long_description = ""
with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    author="Sean Enck",
    author_email="enckse@voidedtech.com",
    name=__pkg_name__,
    version="1.9.3",
    description='Convert source code to cross stitch patterns',
    long_description=long_description,
    url='https://cgit.voidedtech.com/pyxstitch',
    license='MIT',
    python_requires='>=3.4',
    packages=[__pkg_name__, __pkg_name__ + ".fonts"],
    install_requires=['pygments', 'Pillow'],
    keywords='crossstitch cross stitch',
    entry_points={
        'console_scripts': [
            'pyxstitch = pyxstitch.pyxstitch:main',
        ],
    },
)
