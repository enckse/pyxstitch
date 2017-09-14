#!/usr/bin/python
"""Hex tooling/utilities for operations."""

_HEX = '0123456789abcdefABCDEF'
_HEX_LOOKUP = {x: int(x, 16) for x in (y + z for y in _HEX for z in _HEX)}


def to_hex(rgb):
    """Convert a hex string 001122 -> tuple (0, 1, 2)."""
    return (_HEX_LOOKUP[rgb[0:2]],
            _HEX_LOOKUP[rgb[2:4]],
            _HEX_LOOKUP[rgb[4:6]])


def to_rgb_string(rgb):
    """Convert to rgb string."""
    return ('%02x%02x%02x' % rgb).lower()


def is_rgb_string(value):
    """Sanity check against an rgb string."""
    if value is not None:
        lower = value.lower()
        check = [x for x in lower if x in ['a',
                                           'b',
                                           'c',
                                           'd',
                                           'e',
                                           'f',
                                           '0',
                                           '1',
                                           '2',
                                           '3',
                                           '4',
                                           '5',
                                           '6',
                                           '7',
                                           '8',
                                           '9']]
        return len(check) == 6
    return False
