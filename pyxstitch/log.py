#!/usr/bin/python
"""Simple/primitive logging."""

IS_VERBOSE = True


def change_verbosity(quiet):
    """Change verbosity."""
    IS_VERBOSE = quiet


def writeln():
    """Write an (empty) message."""
    write("")


def write(message):
    """Write a message."""
    if IS_VERBOSE:
        print(message)
