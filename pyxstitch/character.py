#!/usr/bin/python
"""Defines a character for formatting text -> cross stitch character."""
from enum import IntFlag


class BadCharException(Exception):
    """Character is not defined or not fully defined."""


class Stitch(IntFlag):
    """Types of stitching."""

    CrossStitch = 1


class BackStitch(IntFlag):
    """Grid-based backstitching."""

    Top = 1
    Bottom = 2
    Left = 4
    Right = 8
    BottomLeftTopRight = 16
    TopLeftBottomRight = 32


class Grid(object):
    """Defines a character grid of stitches."""

    def __init__(self):
        """Init a grid instance."""
        self.stitches = []


def _empty_grid(width, height):
    """Create an empty grid."""
    return [[Grid() for x in range(width)] for y in range(height)]


class Character(object):
    """Defines a cross stitch character."""

    def __init__(self, height, width):
        """Instance the character, creates an empty pattern grid."""
        self._height = height
        self._pattern = _empty_grid(width, height)

    def cells(self, height):
        """Get stitches for  a specied character and returns them for it."""
        if height > self._height:
            return None
        wide = self._pattern[height]
        for width in range(len(wide)):
            grid = wide[width]
            yield grid.stitches
        yield []
