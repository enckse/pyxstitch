#!/usr/bin/python
"""An ASCII 3x5 (monospace) pattern."""
from pyxstitch.font import BaseFontFactory
from pyxstitch.font_three_by_seven import ThreeBySeven


class ThreeByFive(BaseFontFactory):
    """Font factory definition."""

    def _height_width(self):
        """Height and width of font."""
        return (5, 3)

    def _downsize(self, write_to, ch, chars, mid):
        self._drop_lines(write_to, ch, chars, [mid, 7])

    def _initialize_characters(self):
        """Initialize default characters."""
        objs = {}
        basis = ThreeBySeven()._initialize_characters()
        # drop lines
        drops = {}
        drops['A'] = 5
        drops['G'] = 3
        drops['P'] = 5
        drops['R'] = 5
        drops['V'] = 3
        for c in ['D',
                  'I',
                  'J',
                  'K',
                  'L',
                  'M',
                  'N',
                  'O',
                  'Q',
                  'T',
                  'U',
                  'W',
                  'Y']:
            drops[c] = 4
        for d in drops:
            self._downsize(objs, d, basis, drops[d])
        # new definitions
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
|0.8192|0.02|0.4096|
|0.2048|    |0.1024|
|1.00|    |1.00|
|    |    |    |
""")
        objs['0'] = self._build_character("""
|    |1.00|    |
|1.00|0.16|1.00|
|1.00|0.16|1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['1'] = self._build_character("""
|1.00|1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
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
        objs['u'] = self._build_character("""
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['a'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |    |
""")
        objs['c'] = self._build_character("""
|    |    |    |
|    |1.00|1.00|
|1.00|    |    |
|    |1.00|1.00|
|    |    |    |
""")
        objs['k'] = self._build_character("""
|1.00|    |    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |1.00|
|    |    |    |
""")
        objs['h'] = self._build_character("""
|1.00|    |    |
|1.00|    |    |
|1.00|1.00|1.00|
|1.00|    |1.00|
|    |    |    |
""")
        objs['d'] = self._build_character("""
|    |    |1.00|
|    |1.00|1.00|
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |    |
""")
        objs['e'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|0.02|1.00|
|1.00|0.02|0.02|
|    |    |    |
""")
        objs['f'] = self._build_character("""
|    |1.00|1.00|
|    |1.00|    |
|1.00|1.00|1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['t'] = self._build_character("""
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['#'] = self._build_character("""
|    |0.16|0.16|
|0.01|1.00|0.01|
|0.02|1.00|0.02|
|0.16|0.16|    |
|    |    |    |
""")
        objs['"'] = self._build_character("""
|1.00|    |1.00|
|0.40|    |0.40|
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs["'"] = self._build_character("""
|    |1.00|    |
|    |0.40|    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['g'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|0.02|0.02|1.00|
""")
        objs['l'] = self._build_character("""
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['i'] = self._build_character("""
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['n'] = self._build_character("""
|    |    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
""")
        objs['m'] = self._build_character("""
|    |    |    |
|1.00|    |1.00|
|0.04|1.00|0.08|
|0.04|    |0.08|
|    |    |    |
""")
        objs['w'] = self._build_character("""
|    |    |    |
|0.04|    |0.08|
|0.04|1.00|0.08|
|1.00|    |1.00|
|    |    |    |
""")
        objs['o'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['p'] = self._build_character("""
|    |    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |    |
""")

        objs[':'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |    |    |
""")
        objs[';'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |0.20|    |
""")
        objs['}'] = self._build_character("""
|1.00|1.00|    |
|    |1.00|0.02|
|    |1.00|    |
|1.00|1.00|    |
|    |    |    |
""")
        objs[')'] = self._build_character("""
|0.33|1.00|0.1024|
|    |1.00|0.8192|
|    |1.00|0.2048|
|0.18|1.00|0.4096|
|    |    |    |
""")
        objs['s'] = self._build_character("""
|    |    |    |
|    |1.00|1.00|
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
        objs['('] = self._build_character("""
|0.2048|1.00|0.17|
|0.4096|1.00|    |
|0.1024|1.00|    |
|0.8192|1.00|0.34|
|    |    |    |
""")
        objs['r'] = self._build_character("""
|    |    |    |
|    |1.00|1.00|
|1.00|    |    |
|1.00|    |    |
|    |    |    |
""")
        objs['!'] = self._build_character("""
|    |1.00|    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |    |    |
""")
        objs['.'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |1.00|    |
|    |    |    |
""")
        objs[','] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |1.00|    |
|    |0.20|    |
""")
        objs['_'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['='] = self._build_character("""
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs[' '] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs[']'] = self._build_character("""
|1.00|1.00|1.00|
|    |    |1.00|
|    |    |1.00|
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['['] = self._build_character("""
|1.00|1.00|1.00|
|1.00|    |    |
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['3'] = self._build_character("""
|1.00|1.00|    |
|0.02|0.02|1.00|
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
""")
        objs['4'] = self._build_character("""
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |1.00|
|    |    |1.00|
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
        objs['7'] = self._build_character("""
|1.00|1.00|1.00|
|    |    |1.00|
|    |1.00|    |
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
        objs['q'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |1.00|
""")
        objs['j'] = self._build_character("""
|    |    |1.00|
|    |    |    |
|    |    |1.00|
|    |    |1.00|
|1.00|1.00|    |
""")
        objs['v'] = self._build_character("""
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['x'] = self._build_character("""
|    |    |    |
|1.00|    |1.00|
|    |1.00|    |
|1.00|    |1.00|
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
        objs['z'] = self._build_character("""
|    |    |    |
|1.00|1.00|1.00|
|    |0.16|    |
|1.00|1.00|1.00|
|    |    |    |
""")
        objs['b'] = self._build_character("""
|1.00|    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
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
        objs['@'] = self._build_character("""
|    |    |    |
|0.16|0.01|0.32|
|0.04|1.00|0.08|
|0.32|0.02|0.40|
|    |    |    |
""")
        objs['*'] = self._build_character("""
|    |    |    |
|0.32|1.00|0.16|
|0.03|1.00|0.03|
|0.16|1.00|0.32|
|    |    |    |
""")
        objs['&'] = self._build_character("""
|0.16|0.01|0.32|
|0.32|0.02|0.16|
|0.16|    |1.00|
|0.32|0.16|0.32|
|    |    |    |
""")
        objs['+'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |1.00|    |
|    |    |    |
""")
        objs['-'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['^'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|    |    |    |
|    |    |    |
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
        objs['|'] = self._build_character("""
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |    |    |
""")
        objs['~'] = self._build_character("""
|    |    |    |
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['`'] = self._build_character("""
|1.00|1.00|    |
|    |    |0.32|
|    |    |    |
|    |    |    |
|    |    |    |
""")
        return objs
