#!/usr/bin/python
"""An ASCII 3x5 (monospace) pattern."""
from pyxstitch.font import BaseFontFactory
from pyxstitch.fonts.three_by_seven import ThreeBySeven


class ThreeByFive(BaseFontFactory):
    """Font factory definition."""

    def _set_drops(self, chars, size, write_to, secondary=8):
        for c in chars:
            write_to[c] = [size, secondary]

    def display(self):
        """Display name."""
        return self._monospace_ascii()

    def _height_width(self):
        """Height and width of font."""
        return (5, 3)

    def _downsize(self, write_to, ch, chars, spaces):
        self._drop_lines(write_to, ch, chars, spaces)

    def _initialize_characters(self):
        """Initialize default characters."""
        objs = {}
        basis = ThreeBySeven()._initialize_characters()
        # drop lines
        drops = {}
        self._set_drops(['A', 'P', 'R', ' ', '`', '^', '7'], 5, drops)
        self._set_drops(['G', 'V'], 3, drops)
        self._set_drops(['j'], 2, drops, secondary=5)
        self._set_drops(['+', '-', '=', '*', ':', ';', '@'], 7, drops)
        self._set_drops(['a',
                         'c',
                         'h',
                         'k',
                         'u',
                         'd',
                         'e',
                         'f',
                         '4',
                         't',
                         'b',
                         'z',
                         'l',
                         's',
                         'r',
                         'v',
                         'x',
                         'm',
                         'w',
                         'p',
                         'n',
                         'q',
                         'o',
                         'i',
                         '_',
                         '.',
                         ',',
                         '|',
                         '!',
                         '~'], 2, drops)
        self._set_drops(['D',
                         'I',
                         'J',
                         '(',
                         '[',
                         ']',
                         ')',
                         'K',
                         'L',
                         'M',
                         'N',
                         'O',
                         'Q',
                         'T',
                         'U',
                         'W',
                         'Y',
                         '1',
                         '"',
                         "'"], 4, drops)
        for d in drops:
            self._downsize(objs, d, basis, drops[d])
        # new definitions
        objs[')'] = self._build_character("""
|0.33|1.00|0.1024|
|    |0.1024|0.8192|
|    |0.4096|0.2048|
|0.18|1.00|0.4096|
|    |    |    |
""")

        objs['('] = self._build_character("""
|0.2048|1.00|0.17|
|0.4096|0.2048|    |
|0.1024|0.8192|    |
|0.8192|1.00|0.34|
|    |    |    |
""")

        objs['0'] = self._build_character("""
|    |1.00|    |
|1.00|0.16|1.00|
|1.00|0.16|1.00|
|    |1.00|    |
|    |    |    |
""")

        objs['B'] = self._build_character("""
|1.00|1.00|0.32|
|1.00|0.02|1.00|
|1.00|    |0.32|
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['C'] = self._build_character("""
|    |1.00|0.34|
|1.00|    |    |
|1.00|    |    |
|    |1.00|0.17|
|    |    |    |
""")
        objs['E'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|0.02|0.02|
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['F'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|0.02|0.02|
|1.00|    |    |
|1.00|    |    |
|    |    |    |
""")
        objs['H'] = self._build_character("""
|1.00|    |1.00|
|1.00|0.02|1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
""")
        objs['S'] = self._build_character("""
|    |1.00|1.00|
|1.00|0.02|    |
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
""")
        objs['X'] = self._build_character("""
|1.00|    |1.00|
|    |1.00|    |
|    |1.00|    |
|1.00|    |1.00|
|    |    |    |
""")
        objs['2'] = self._build_character("""
|1.00|1.00|    |
|    |    |1.00|
|1.00|0.01|    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['5'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|0.02|    |
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
""")
        objs['#'] = self._build_character("""
|    |0.16|0.16|
|0.01|1.00|0.01|
|0.02|1.00|0.02|
|0.16|0.16|    |
|    |    |    |
""")
        objs['g'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|0.02|0.02|1.00|
""")

        objs['}'] = self._build_character("""
|1.00|1.00|    |
|    |1.00|0.02|
|    |1.00|    |
|1.00|1.00|    |
|    |    |    |
""")
        objs['>'] = self._build_character("""
|1.00|0.32|    |
|    |0.32|0.32|
|    |0.16|0.16|
|1.00|0.16|    |
|    |    |    |
""")
        objs['<'] = self._build_character("""
|    |0.16|1.00|
|0.16|0.16|    |
|0.32|0.32|    |
|    |0.32|1.00|
|    |    |    |
""")
        objs['{'] = self._build_character("""
|    |1.00|1.00|
|0.02|1.00|    |
|    |1.00|    |
|    |1.00|1.00|
|    |    |    |
""")
        objs['3'] = self._build_character("""
|1.00|1.00|    |
|0.02|0.02|1.00|
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
""")
        objs['9'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|    |0.01|1.00|
|1.00|1.00|    |
|    |    |    |
""")
        objs['6'] = self._build_character("""
|    |1.00|1.00|
|1.00|0.02|    |
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['8'] = self._build_character("""
|    |1.00|    |
|1.00|0.02|1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['y'] = self._build_character("""
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|1.00|
|0.02|0.02|1.00|
""")
        objs['Z'] = self._build_character("""
|1.00|1.00|1.00|
|    |0.2050|  |
|    |0.4096|    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['%'] = self._build_character("""
|1.00|    |    |
|    |0.2048|    |
|    |0.4096|    |
|    |    |1.00|
|    |    |    |
""")
        objs['$'] = self._build_character("""
|    |1.00|    |
|0.18|1.00|0.03|
|0.02|1.00|0.16|
|    |1.00|    |
|    |    |    |
""")
        objs['&'] = self._build_character("""
|0.2048|0.01|0.1024|
|0.8192|0.02|0.4096|
|1.00|0.32|1.00|
|    |1.00|0.32|
|    |    |    |
""")
        objs['?'] = self._build_character("""
|1.00|1.00|    |
|    |0.02|1.00|
|    |    |    |
|    |1.00|    |
|    |    |    |
""")
        objs['\\'] = self._build_character("""
|1.00|    |    |
|    |1.00|    |
|    |1.00|    |
|    |    |1.00|
|    |    |    |
""")
        objs['/'] = self._build_character("""
|    |    |1.00|
|    |1.00|    |
|    |1.00|    |
|1.00|    |    |
|    |    |    |
""")
        return objs
