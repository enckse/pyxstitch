#!/usr/bin/python3
"""Simple/primitive logging."""


class Log(object):
    """Logging object."""

    is_verbose = True

    def writeln():
        """Write a blank line."""
        Log.write("")

    def write(message):
        """Write a logging line."""
        if Log.is_verbose:
            print(message)
