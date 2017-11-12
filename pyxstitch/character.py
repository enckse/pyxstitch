#!/usr/bin/python
"""Defines a character for formatting text -> cross stitch character."""
from enum import IntFlag


class BadCharException(Exception):
    """Character is not defined or not fully defined."""


class Stitch(IntFlag):
    """Types of stitching."""

    CrossStitch = 1
    BottomLeft = 2
    BottomRight = 4
    TopLeft = 8
    TopRight = 16


class BackStitch(IntFlag):
    """Grid-based backstitching."""

    Top = 1
    Bottom = 2
    Left = 4
    Right = 8
    BottomLeftTopRight = 16
    TopLeftBottomRight = 32
    BottomLeft = 64
    BottomRight = 128
    TopLeft = 256
    TopRight = 512
    TopLeftMid = 1024
    TopRightMid = 2048
    BottomLeftMid = 4096
    BottomRightMid = 8192
    TopBottomMid = 16384


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
        self._width = width
        self._pattern = _empty_grid(width, height)
        self.raw = None

    def cells(self, height):
        """Get stitches for  a specied character and returns them for it."""
        if height > self._height or height < 0:
            return None
        wide = self._pattern[height]
        for width in range(0, self._width):
            grid = wide[width]
            yield grid.stitches
        yield []

    def metadata(self):
        """Character metadata."""
        return [self._height, self._width]
