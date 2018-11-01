#!/usr/bin/python3
"""Utilities for dealing with any python requirements."""
import sys
import pyxstitch.log as log

_PY_35 = (3, 5)
_MIN_VERS = (3, 4)


def home():
    """Get the user's home directory."""
    v = supported()
    if v >= _PY_35:
        from pathlib import Path
        return str(Path.home())
    else:
        from os.path import expanduser
        return (expanduser("~"))


def supported():
    """Check (exits) that the python version is supported."""
    vers = sys.version_info
    v = _supported(vers)
    if v is None:
        log.Log.write("python {}.{} is not supported".format(vers[0], vers[1]))
        exit(1)
    return v


def _supported(vers):
    """Check (exits) that the python version is supported."""
    if vers < _MIN_VERS:
        return None
    return vers
