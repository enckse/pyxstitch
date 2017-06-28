#!/usr/bin/python
"""Supports generating unique(ish) symbols for colors."""
import string


class SymbolError(Exception):
    """Symbol generation errors."""


class SymbolGenerator(object):
    """Generate symbols by color name."""

    def next(self, color):
        """Next color."""
        raise SymbolError("not implemented")


class DefaultSymbolGenerator(SymbolGenerator):
    """Default generator."""

    def __init__(self):
        """Create a new instance."""
        self._tracked = {}
        self._symbols = self._generate()
        self._idx = 0

    def _generate(self):
        """Generate the symbols."""
        syms = []
        syms = syms + sorted([x for x in string.printable if x.isalnum()])
        syms = syms + sorted([x for x in string.printable if not x.isalnum()])
        return syms

    def next(self, color):
        """Next color."""
        if color in self._tracked:
            return self._tracked[color]
        if self._idx >= len(self._symbols):
            raise SymbolError("out of symbols!")
        c = self._symbols[self._idx]
        self._idx += 1
        self._tracked[color] = c
        return c
