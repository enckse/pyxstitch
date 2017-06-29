#!/usr/bin/python
"""Defines the default font functionality to get char -> stitch mappings."""
from pyxstitch.character import Character, BackStitch, Stitch, BadCharException


class FontException(Exception):
    """Font exceptions."""


class FontFactory(object):
    """Character stitching font creator."""

    def height(self):
        """Get the height of the font."""
        raise FontException("not implemented.")

    def get(self, character):
        """Get a character definition."""
        raise FontException("not implemented.")

    def process(self, string_value):
        """Process a string before lexing."""
        raise FontException("not implemented.")

class DefaultFontFactory(FontFactory):
    """Create characters of the default stitching font."""

    def __init__(self):
        """Initialize the factory."""
        self._height = 11
        self._width = 5
        self._top_off = 1
        self._bot_off = 1
        self._replace = {'\t': '    ', '\r': '\n', '\f': '\n', '\v': '\n'}
        self._characters = self._initialize_characters()

    def height(self):
        """get the font factory range of height for characters."""
        return range(self._height)

    def width(self):
        """get the font width."""
        return range(self._width)

    def get(self, ch):
        """Lookup a character in the font."""
        if ch in self._characters:
            return self._characters[ch]
        raise FontException("No font entry for character {}".format(ch))

    def _set_flags(self, val_str, enums, add_to):
        """Check which enum flags are set - append them to a list."""
        val = int(val_str)
        for e in enums:
            if e & val:
                add_to.append(e)

    def process(self, value):
        """Process before lexer."""
        val = value
        for replacing in self._replace:
            val = val.replace(replacing, self._replace[replacing])
        return val

    def _parse(self, definition, ch):
        """Parse a character definition."""
        if definition is None:
            raise BadCharException("Invalid character definition")
        stripped = definition.strip()
        if len(stripped) == 0:
            raise BadCharException("Empty definition for character")
        parts = stripped.split("\n")
        has_height = len(parts)
        if has_height != self._height:
            if has_height != self._height - self._top_off - self._bot_off:
                raise BadCharException("Definition has an improper height")
            add_line = "|" + " | ".join(["" for x in range(self._width)]) + "|"
            for x in range(self._top_off):
                parts.insert(0, add_line)
            for x in range(self._bot_off):
                parts.append(add_line)
        height = 0
        for part in parts:
            defined = [x for x in part.split("|") if x != '']
            if len(defined) != self._width:
                raise BadCharException("Definition has an improper width")
            width = 0
            for entry in defined:
                if len(entry.strip()) > 0:
                    section = entry.split(".")
                    adding = []
                    self._set_flags(section[0], Stitch, adding)
                    self._set_flags(section[1], BackStitch, adding)
                    ch[height][width].stitches = adding
                width += 1
            height += 1
        return ch

    def _build_character(self, stitching):
        """Build a character into an object definition."""
        ch = Character(self._height, self._width)
        ch._pattern = self._parse(stitching, ch._pattern)
        return ch

    def _initialize_characters(self):
        """Initialize default characters."""
        objs = {}
        objs['A'] = self._build_character("""
|    |0.16|1.03|0.32|    |
|0.16|0.16|    |0.32|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.04|1.03|1.03|1.03|1.08|
|1.12|    |    |    |1.12|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['B'] = self._build_character("""
|1.05|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |0.20|
|1.12|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.06|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['C'] = self._build_character("""
|0.16|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.14|
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |1.13|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['D'] = self._build_character("""
|1.05|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.06|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['E'] = self._build_character("""
|1.05|1.03|1.03|1.03|1.11|
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.04|1.03|1.03|1.11|    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.06|1.03|1.03|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['F'] = self._build_character("""
|1.05|1.03|1.03|1.03|1.11|
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.04|1.03|1.03|1.11|    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.14|    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['G'] = self._build_character("""
|0.16|1.03|1.03|1.03|1.11|
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |1.07|1.09|
|1.12|    |    |    |1.12|
|0.32|1.03|1.03|1.03|1.10|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['H'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.04|1.03|1.03|1.03|1.08|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['I'] = self._build_character("""
|1.07|1.03|1.01|1.03|1.11|
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|1.07|1.03|1.02|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['J'] = self._build_character("""
|    |    |    |    |1.13|
|    |    |    |    |1.12|
|    |    |    |    |1.12|
|    |    |    |    |1.12|
|    |    |    |    |1.12|
|1.13|    |    |    |1.12|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['K'] = self._build_character("""
|1.13|    |    |0.16|1.09|
|1.12|    |0.16|1.00|0.16|
|1.12|0.16|1.00|0.16|    |
|1.04|1.00|1.08|    |    |
|1.12|0.32|1.00|0.32|    |
|1.12|    |0.32|1.00|0.32|
|1.14|    |    |0.32|1.10|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['L'] = self._build_character("""
|1.13|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.06|1.03|1.03|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['M'] = self._build_character("""
|1.05|0.32|    |0.16|1.09|
|1.04|1.00|1.01|1.00|1.08|
|1.12|0.32|1.02|0.16|1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['N'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.04|0.32|    |    |1.12|
|1.04|1.00|0.32|    |1.12|
|1.12|0.32|1.00|0.32|1.12|
|1.12|    |0.32|1.00|1.08|
|1.12|    |    |0.32|1.08|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['O'] = self._build_character("""
|0.16|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['P'] = self._build_character("""
|1.05|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.04|1.03|1.03|1.03|0.16|
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.14|    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['Q'] = self._build_character("""
|0.16|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |1.05|0.32|0.20|
|1.12|    |0.32|1.00|0.32|
|0.32|1.03|0.17|0.32|1.10|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['R'] = self._build_character("""
|1.05|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.04|1.01|1.01|1.03|0.16|
|1.12|0.32|1.00|0.32|    |
|1.12|    |0.32|1.00|0.32|
|1.14|    |    |0.32|1.10|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['S'] = self._build_character("""
|0.16|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.14|
|1.12|    |    |    |    |
|0.32|1.03|1.03|1.03|0.32|
|    |    |    |    |1.12|
|1.13|    |    |    |1.12|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['T'] = self._build_character("""
|1.07|1.03|1.01|1.03|1.11|
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.14|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['U'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['V'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|0.32|0.32|    |0.16|0.16|
|    |0.32|1.03|0.16|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['W'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.12|0.16|1.01|0.32|1.12|
|1.04|1.00|1.02|1.00|1.08|
|1.06|0.16|    |0.32|1.10|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['X'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.04|0.32|    |0.16|1.08|
|0.32|1.00|1.01|1.00|0.16|
|    |1.04|1.00|1.08|    |
|0.16|1.00|1.02|1.00|0.32|
|1.04|0.16|    |0.32|1.08|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['Y'] = self._build_character("""
|1.13|    |    |    |1.13|
|1.04|0.32|    |0.16|1.08|
|0.32|1.00|1.01|1.00|0.16|
|    |0.32|1.00|0.16|    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.14|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['0'] = self._build_character("""
|0.16|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |0.16|1.08|
|1.12|0.16|1.03|0.16|1.12|
|1.04|0.16|    |    |1.12|
|1.12|    |    |    |1.12|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['1'] = self._build_character("""
|0.16|1.01|1.09|    |    |
|1.06|0.16|1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|1.07|1.03|1.02|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['u'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|    |    |0.16|1.08|
|0.32|1.03|1.03|0.16|1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['a'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|0.16|1.03|1.03|1.03|1.09|
|1.12|    |    |    |1.12|
|1.12|    |    |0.16|1.08|
|0.32|1.03|1.03|0.16|1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['c'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|0.16|1.01|1.03|1.03|0.34|
|1.04|0.16|    |    |    |
|1.04|0.32|    |    |    |
|0.32|1.02|1.03|1.03|0.17|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['k'] = self._build_character("""
|1.13|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |0.16|0.17|    |
|1.04|1.03|1.08|    |    |
|1.12|    |0.32|0.32|    |
|1.14|    |    |0.32|0.34|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['h'] = self._build_character("""
|1.13|    |    |    |    |
|1.12|    |    |    |    |
|1.12|    |    |    |    |
|1.04|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['d'] = self._build_character("""
|    |    |    |    |1.13|
|    |    |    |    |1.12|
|    |    |    |    |1.12|
|0.16|1.03|1.03|1.03|1.08|
|1.12|    |    |    |1.12|
|1.12|    |    |0.16|1.08|
|0.32|1.03|1.03|0.16|1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['e'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|0.16|1.03|1.03|1.03|0.32|
|1.12|0.02|0.02|0.02|0.20|
|1.12|    |    |    |    |
|0.32|1.03|1.03|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['f'] = self._build_character("""
|    |    |1.05|1.03|1.11|
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|1.07|1.03|1.00|1.03|1.11|
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.14|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['t'] = self._build_character("""
|    |    |1.13|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|1.07|1.03|1.00|1.03|1.11|
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.06|1.11|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['#'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |0.16|0.16|    |
|    |0.03|0.15|0.03|    |
|    |0.16|0.16|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['"'] = self._build_character("""
|    |1.13|    |1.13|    |
|    |1.12|    |1.12|    |
|    |0.40|    |0.40|    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs["'"] = self._build_character("""
|    |    |1.13|    |    |
|    |    |1.12|    |    |
|    |    |0.40|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['g'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|0.16|1.03|1.03|1.03|1.09|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.08|
|0.32|1.03|1.03|1.03|1.12|
|    |    |    |    |1.12|
|    |1.07|1.03|1.03|0.16|
""")
        objs['l'] = self._build_character("""
|    |1.07|1.09|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|1.07|1.03|1.02|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['i'] = self._build_character("""
|    |    |    |    |    |
|    |    |1.15|    |    |
|    |    |    |    |    |
|    |1.07|1.09|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|1.07|1.03|1.02|1.03|1.11|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['n'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|1.13|0.16|1.03|1.01|0.32|
|1.04|0.16|    |0.32|1.08|
|1.12|    |    |    |1.12|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['m'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|1.05|0.32|    |0.16|1.09|
|1.12|0.32|1.03|0.16|1.12|
|1.12|    |    |    |1.12|
|1.14|    |    |    |1.14|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['w'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|1.13|    |    |    |1.13|
|1.12|    |    |    |1.12|
|1.12|0.16|1.03|0.32|1.12|
|1.06|0.16|    |0.32|1.10|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['o'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|0.16|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|0.32|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['p'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|1.05|1.03|1.03|1.03|0.32|
|1.12|    |    |    |1.12|
|1.12|    |    |    |1.12|
|1.04|1.03|1.03|1.03|0.16|
|1.12|    |    |    |    |
|1.14|    |    |    |    |
""")

        objs[':'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |1.15|    |    |
|    |    |    |    |    |
|    |    |1.15|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs[';'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |1.15|    |    |
|    |    |    |    |    |
|    |    |1.13|    |    |
|    |    |0.20|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['}'] = self._build_character("""
|    |1.07|0.32|    |    |
|    |    |0.32|0.32|    |
|    |    |0.16|0.16|    |
|    |    |1.12|    |    |
|    |    |0.32|0.32|    |
|    |    |0.16|0.16|    |
|    |1.07|0.16|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs[')'] = self._build_character("""
|    |1.07|0.32|    |    |
|    |    |0.32|0.32|    |
|    |    |    |1.12|    |
|    |    |    |1.12|    |
|    |    |    |1.12|    |
|    |    |0.16|0.16|    |
|    |1.07|0.16|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['s'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|0.16|1.03|1.03|1.03|0.34|
|0.40|0.02|0.02|0.02|    |
|    |    |    |    |0.36|
|0.33|1.03|1.03|1.03|0.16|
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['>'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |0.33|0.32|    |    |
|    |    |0.32|0.32|    |
|    |    |0.16|0.16|    |
|    |0.18|0.16|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['<'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |0.16|0.17|    |
|    |0.16|0.16|    |    |
|    |0.32|0.32|    |    |
|    |    |0.32|0.34|    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['{'] = self._build_character("""
|    |    |0.16|1.11|    |
|    |0.16|0.16|    |    |
|    |0.32|0.32|    |    |
|    |    |1.12|    |    |
|    |0.16|0.16|    |    |
|    |0.32|0.32|    |    |
|    |    |0.32|1.11|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['('] = self._build_character("""
|    |    |0.16|1.11|    |
|    |0.16|0.16|    |    |
|    |1.12|    |    |    |
|    |1.12|    |    |    |
|    |1.12|    |    |    |
|    |0.32|0.32|    |    |
|    |    |0.32|1.11|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['r'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|1.13|0.16|1.03|1.03|0.34|
|1.04|0.16|    |    |    |
|1.12|    |    |    |    |
|1.14|    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['!'] = self._build_character("""
|    |    |1.13|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.12|    |    |
|    |    |1.14|    |    |
|    |    |    |    |    |
|    |    |1.15|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['.'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |1.15|    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs[','] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |1.13|    |    |
|    |    |0.20|    |    |
|    |    |    |    |    |
""")
        objs['_'] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |1.07|1.03|1.11|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['='] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |1.07|1.03|1.11|    |
|    |    |    |    |    |
|    |1.07|1.03|1.11|    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs[' '] = self._build_character("""
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs[']'] = self._build_character("""
|    |1.07|1.03|1.09|    |
|    |    |    |1.12|    |
|    |    |    |1.12|    |
|    |    |    |1.12|    |
|    |    |    |1.12|    |
|    |    |    |1.12|    |
|    |1.07|1.03|1.09|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        objs['['] = self._build_character("""
|    |1.05|1.03|1.11|    |
|    |1.12|    |    |    |
|    |1.12|    |    |    |
|    |1.12|    |    |    |
|    |1.12|    |    |    |
|    |1.12|    |    |    |
|    |1.12|1.03|1.11|    |
|    |    |    |    |    |
|    |    |    |    |    |
""")
        return objs
