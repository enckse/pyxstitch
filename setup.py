#!/usb/bin/python

"""Setup for pyxstitch."""

from setuptools import setup, find_packages

setup(
    name='pyxstitch',
    version="1.1.0",
    description='Convert source code to cross stitch patterns',
    url='https://github.com/enckse/pyxstitch',
    license='MIT',
    packages=['pyxstitch'],
    install_requires=['webcolors', 'pygments', 'pillow'],
    entry_points={
        'console_scripts': [
            'pyxstitch = pyxstitch.pyxstitch:main',
        ],
    },
)
