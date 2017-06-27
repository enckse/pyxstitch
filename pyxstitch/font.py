# 8 states
# no color
# full cross stitch
# |X
# ^-
# _
# X|
# \
# /
# X + others
from enum import IntFlag
import string
class Stitch(IntFlag):
    CrossStitch = 1

class BackStitch(IntFlag):
    Top = 1
    Bottom = 2
    Left = 4
    Right = 8
    BottomLeftTopRight = 16
    TopLeftBottomRight = 32

HEIGHT = 9

class Grid(object):
    def __init__(self):
        self.stitches = []

def _empty_grid(width):
    return [[Grid() for x in range(width)] for y in range(HEIGHT)]

class BadCharException(Exception):
    """Character is not defined or not fully defined."""

class Character(object):
    def __init__(self, width):
        self._pattern = _empty_grid(width)
        self._whitespace = False

    def cells(self, height):
        wide = self._pattern[height]
        for width in range(len(wide)):
            grid = wide[width]
            yield grid.stitches
        yield []

class FontFactory(object):

    def __init__(self):
        self._characters = _initialize_characters()
    def get(self, character):
        if character in self._characters:
            return self._characters[character]
        raise BadCharException("Not font entry for charcter {}".format(character))

def _parse(input_width, definition, use_enum, ch):
    if definition is None:
        raise BadCharException("Invalid character definition")
    stripped = definition.strip()
    if len(stripped) == 0:
        raise BadCharException("Empty definition for character")
    parts = stripped.split("\n")
    if len(parts) != HEIGHT:
        raise BadCharException("Definition has an improper height")
    height = 0
    for part in parts:
        defined = [x for x in part.split("|") if x != '' ]
        if len(defined) != input_width:
            raise BadCharException("Definition has an improper width")
        width = 0
        for entry in defined:
            if len(entry.strip()) > 0:
                val = int(entry)
                for e in use_enum:
                    is_set = e & val
                    if is_set:
                        ch[height][width].stitches.append(e)
            width += 1
        height += 1
    return ch

def _build_character(width, stitching, backstitching, is_whitespace=False):
    """Build a character into an object definition."""
    ch = Character(width)
    ch._pattern = _parse(width, stitching, Stitch, ch._pattern)
    ch._pattern = _parse(width, backstitching, BackStitch, ch._pattern)
    ch._whitespace = is_whitespace
    return ch

def _initialize_characters():
    objs = {}
        
    objs['A'] = _build_character(3, """
| |1| |
|1| |1|
|1| |1|
|1|1|1|
|1| |1|
|1| |1|
|1| |1|
| | | |
| | | |
""", """
|16| 3|32|
|12|  |12|
|12|  |12|
| 4| 3| 8|
|12|  |12|
|12|  |12|
|14|  |14|
|  |  |  |
|  |  |  |
""")
    objs['W'] = _build_character(5, """
|1| | | |1|
|1| | | |1|
|1| | | |1|
|1| |1| |1|
|1| |1| |1|
|1|1|1|1|1|
| |1| |1| |
| | | | | |
| | | | | |
""","""
|13|  |  |  |13|
|12|  |  |  |12|
|12|  |  |  |12|
|12|  |13|  |12|
| 4|32|12|16| 8|
| 4|  | 2|  | 8|
|32|10|  |6|16|
|  |  |  |  |  |
|  |  |  |  |  |
""")
    objs['!'] = _build_character(1, """
|1|
|1|
|1|
|1|
|1|
| |
|1|
| |
| |
""", """
|13|
|12|
|12|
|12|
|14|
|  |
|15|
|  |
|  |
""")
    objs[' '] = _build_character(2, """
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
""","""
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
""", is_whitespace=True)
    return objs
