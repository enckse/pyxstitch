#!/usb/bin/python

"""Setup for pyxstitch."""

from setuptools import setup, find_packages
import os

__pkg_name__ = "pyxstitch"
with open(os.path.join(__pkg_name__, "version.py")) as v_file:
    exec(v_file.read())

setup(
    author="Sean Enck",
    author_email="enckse@gmail.com",
    name=__pkg_name__,
    version=__version__,
    description='Convert source code to cross stitch patterns',
    url='https://github.com/enckse/pyxstitch',
    license='MIT',
    python_requires='>=3',
    packages=[__pkg_name__, __pkg_name__ + ".fonts"],
    install_requires=['pygments', 'pillow'],
    keywords='crossstitch cross stitch',
    entry_points={
        'console_scripts': [
            'pyxstitch = pyxstitch.pyxstitch:main',
        ],
    },
)
