#!/usr/bin/python
"""Simple/primitive logging."""

IS_VERBOSE = True


def change_verbosity(quiet):
    IS_VERBOSE = quiet


def write(message):
    if IS_VERBOSE:
        print(message)
