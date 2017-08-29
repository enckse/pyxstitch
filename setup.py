#!/usb/bin/python

"""Setup for pyxstitch."""

from setuptools import setup, find_packages
import os

__pkg_name__ = "pyxstitch"
version = ''
with open(os.path.join(__pkg_name__, 'VERSION')) as v_file:
    version = v_file.read().strip()

setup(
    name=__pkg_name__,
    version=version,
    description='Convert source code to cross stitch patterns',
    url='https://github.com/enckse/pyxstitch',
    license='MIT',
    packages=[__pkg_name__],
    install_requires=['webcolors', 'pygments', 'pillow'],
    entry_points={
        'console_scripts': [
            'pyxstitch = pyxstitch.pyxstitch:main',
        ],
    },
)
