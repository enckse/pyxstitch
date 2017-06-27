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

def _set_flags(val_str, enums, add_to):
    val = int(val_str)
    for e in enums:
        if e & val:
            add_to.append(e)

def _parse(input_width, definition, ch):
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
                section = entry.split(".")
                adding = []
                _set_flags(section[0], Stitch, adding)
                _set_flags(section[1], BackStitch, adding)
                ch[height][width].stitches = adding
                #val = int(entry)
                #for e in use_enum:
                #    is_set = e & val
                #    if is_set:
                #        ch[height][width].stitches.append(e)
            width += 1
        height += 1
    return ch

def _build_character(width, stitching, is_whitespace=False):
    """Build a character into an object definition."""
    ch = Character(width)
    ch._pattern = _parse(width, stitching, ch._pattern)
    ch._whitespace = is_whitespace
    return ch

def _initialize_characters():
    objs = {} 
    objs['A'] = _build_character(3, """
| | | |
|0.16|1.03|0.32|
|1.12|    |1.12|
|1.12|    |1.12|
|1.04|1.03|1.08|
|1.12|    |1.12|
|1.14|    |1.14|
| | | |
| | | |
""")
    objs['B'] = _build_character(3, """
| | | |
|1.05|1.03|0.32|
|1.12|    |1.12|
|1.12|    |0.20|
|1.12|0.01|0.36|
|1.12|    |1.12|
|1.06|1.03|0.16|
| | | |
| | | |
""")

    objs['W'] = _build_character(5, """
| | | | | |
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|    |1.13|    |1.12|
|1.04|0.32|1.12|0.16|1.08|
|1.04|1.00|1.02|1.00|1.08|
|0.32|1.10|    |1.06|0.16|
| | | | | |
| | | | | |
""")
    objs['d'] = _build_character(3, """
| | | |
| | | |
|    |    |1.13|
|    |    |1.12|
|0.16|1.03|1.08|
|1.12|    |1.12|
|0.32|1.03|1.10|
| | | |
| | | |
""")
    objs['e'] = _build_character(3, """
| | | |
| | | |
| | | |
| | | |
|0.16|1.03|0.32|
|1.14|0.10|0.16|
|0.32|0.02|0.02|
| | | |
| | | |
""")
    objs['!'] = _build_character(1, """
|1.13|
|1.12|
|1.12|
|1.12|
|1.14|
| |
|1.15|
| |
| |
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
""", is_whitespace=True)
    return objs
