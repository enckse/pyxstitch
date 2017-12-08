#!/usr/bin/python
"""Simple/primitive logging."""

IS_VERBOSE = True


def change_verbosity(quiet):
    """Change verbosity."""
    global IS_VERBOSE
    if quiet:
        IS_VERBOSE = False


def writeln():
    """Write an (empty) message."""
    write("")


def write(message):
    """Write a message."""
    global IS_VERBOSE
    if IS_VERBOSE:
        print(message)
