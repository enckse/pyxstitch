#!/usr/bin/python3
"""An ASCII 3x7 (monospace) pattern."""
from pyxstitch.font import BaseFontFactory


class ThreeBySevenMono(BaseFontFactory):
    """Font factory definition."""

    def _display(self):
        """Display name."""
        return self._monospace_ascii()

    def _height_width(self):
        """Height and width of font."""
        return (7, 3)

    def _initialize_characters(self):
        """Initialize default characters."""
        objs = {}
        objs['A'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|1.00|1.00|1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['B'] = self._build_character("""
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['C'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|1.00|    |    |
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['D'] = self._build_character("""
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['E'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|    |    |
|1.00|1.00|1.00|
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['F'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|    |    |
|1.00|1.00|1.00|
|1.00|    |    |
|1.00|    |    |
|    |    |    |
|    |    |    |
""")
        objs['G'] = self._build_character("""
|    |1.00|1.00|
|1.00|    |    |
|1.00|    |    |
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['H'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['I'] = self._build_character("""
|1.00|1.00|1.00|
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['J'] = self._build_character("""
|    |    |1.00|
|    |    |1.00|
|    |    |1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['K'] = self._build_character("""
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['L'] = self._build_character("""
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['M'] = self._build_character("""
|1.00|    |1.00|
|1.00|0.3072|1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['N'] = self._build_character("""
|1.00|    |1.00|
|1.00|0.32|1.00|
|1.00|1.00|1.00|
|1.00|0.32|1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['O'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['P'] = self._build_character("""
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |    |
|1.00|    |    |
|    |    |    |
|    |    |    |
""")
        objs['Q'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|0.32|
|    |    |    |
|    |    |    |
""")
        objs['R'] = self._build_character("""
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['S'] = self._build_character("""
|    |1.00|1.00|
|1.00|    |    |
|    |1.00|    |
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['T'] = self._build_character("""
|1.00|1.00|1.00|
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['U'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['V'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|0.32|    |0.16|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['W'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|0.12288|1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['X'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['Y'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['0'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|1.00|0.16|1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['1'] = self._build_character("""
|0.18|1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['2'] = self._build_character("""
|1.00|1.00|    |
|    |    |1.00|
|1.00|1.00|    |
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['5'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|    |    |
|    |1.00|1.00|
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['u'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['a'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['c'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|1.00|
|1.00|    |    |
|    |1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['k'] = self._build_character("""
|    |    |    |
|1.00|    |    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['h'] = self._build_character("""
|    |    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|1.00|1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['d'] = self._build_character("""
|    |    |    |
|    |    |1.00|
|    |1.00|1.00|
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['e'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|0.02|1.00|
|1.00|0.02|0.02|
|    |    |    |
|    |    |    |
""")
        objs['f'] = self._build_character("""
|    |    |    |
|    |1.00|1.00|
|    |1.00|    |
|1.00|1.00|1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['t'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['#'] = self._build_character("""
|    |0.16|0.16|
|1.00|1.00|1.00|
|    |1.00|    |
|1.00|1.00|1.00|
|0.16|0.16|    |
|    |    |    |
|    |    |    |
""")
        objs['"'] = self._build_character("""
|1.00|    |1.00|
|0.40|    |0.40|
|    |    |    |
|    |    |    |
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
|    |    |    |
|    |    |    |
""")
        objs['g'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |1.00|
|1.00|1.00|    |
""")
        objs['l'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['i'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['n'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['m'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|0.04|1.00|0.08|
|0.04|    |0.08|
|    |    |    |
|    |    |    |
""")
        objs['w'] = self._build_character("""
|    |    |    |
|    |    |    |
|0.04|    |0.08|
|0.04|1.00|0.08|
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['o'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['p'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|1.00|    |    |
|1.00|    |    |
""")

        objs[':'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs[';'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |0.20|    |
|    |    |    |
|    |    |    |
""")
        objs['}'] = self._build_character("""
|1.00|1.00|    |
|    |1.00|    |
|    |    |1.00|
|    |1.00|    |
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs[')'] = self._build_character("""
|0.33|1.00|0.1024|
|    |0.32|0.8192|
|    |    |1.00|
|    |0.16|0.2048|
|0.18|1.00|0.4096|
|    |    |    |
|    |    |    |
""")
        objs['s'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|1.00|
|    |1.00|    |
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['>'] = self._build_character("""
|1.00|    |    |
|    |1.00|    |
|    |    |1.00|
|    |1.00|    |
|1.00|    |    |
|    |    |    |
|    |    |    |
""")
        objs['<'] = self._build_character("""
|    |    |1.00|
|    |1.00|    |
|1.00|    |    |
|    |1.00|    |
|    |    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['{'] = self._build_character("""
|    |1.00|1.00|
|    |1.00|    |
|1.00|    |    |
|    |1.00|    |
|    |1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['('] = self._build_character("""
|0.2048|1.00|0.17|
|0.4096|0.16|    |
|1.00|    |    |
|0.1024|0.32|    |
|0.8192|1.00|0.34|
|    |    |    |
|    |    |    |
""")
        objs['r'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|1.00|
|1.00|    |    |
|1.00|    |    |
|    |    |    |
|    |    |    |
""")
        objs['!'] = self._build_character("""
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['.'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs[','] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |1.00|    |
|    |0.20|    |
|    |    |    |
""")
        objs['_'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['='] = self._build_character("""
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs[' '] = self._build_character("""
|    |    |    |
|    |    |    |
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
|    |    |1.00|
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['['] = self._build_character("""
|1.00|1.00|1.00|
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['3'] = self._build_character("""
|1.00|1.00|    |
|    |    |1.00|
|    |1.00|    |
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['4'] = self._build_character("""
|1.00|    |1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |1.00|
|    |    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['9'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['6'] = self._build_character("""
|    |1.00|1.00|
|1.00|    |    |
|1.00|1.00|1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['7'] = self._build_character("""
|1.00|1.00|1.00|
|    |    |1.00|
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['8'] = self._build_character("""
|1.00|1.00|1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|1.00|    |1.00|
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['q'] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |1.00|
|    |    |1.00|
""")
        objs['j'] = self._build_character("""
|    |    |    |
|    |    |1.00|
|    |    |    |
|    |    |1.00|
|    |    |1.00|
|    |    |1.00|
|1.00|1.00|    |
""")
        objs['v'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['x'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|    |1.00|    |
|1.00|    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['y'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|1.00|
|    |    |1.00|
|1.00|1.00|    |
""")
        objs['Z'] = self._build_character("""
|1.00|1.00|1.00|
|    |    |1.00|
|    |1.00|    |
|1.00|    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['z'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|1.00|1.00|
|    |0.16|    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
""")
        objs['b'] = self._build_character("""
|    |    |    |
|1.00|    |    |
|1.00|1.00|    |
|1.00|    |1.00|
|1.00|1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['%'] = self._build_character("""
|1.00|    |    |
|    |    |1.00|
|    |1.00|    |
|1.00|    |    |
|    |    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['$'] = self._build_character("""
|    |1.00|    |
|0.16|1.00|1.00|
|0.32|1.00|0.32|
|1.00|1.00|0.16|
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['@'] = self._build_character("""
|    |    |    |
|0.16|0.01|0.32|
|0.04|1.00|0.08|
|0.32|0.02|0.40|
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['*'] = self._build_character("""
|    |    |    |
|0.32|1.00|0.16|
|0.03|1.00|0.03|
|0.16|1.00|0.32|
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['&'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|    |
|1.00|    |0.1024|
|    |1.00|0.8192|
|    |    |    |
|    |    |    |
""")
        objs['+'] = self._build_character("""
|    |    |    |
|    |1.00|    |
|1.00|1.00|1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['-'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|1.00|1.00|
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['^'] = self._build_character("""
|    |1.00|    |
|1.00|    |1.00|
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['?'] = self._build_character("""
|1.00|1.00|    |
|    |    |1.00|
|    |1.00|    |
|    |    |    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['\\'] = self._build_character("""
|1.00|    |    |
|0.32|0.32|    |
|    |1.00|    |
|    |0.32|0.32|
|    |    |1.00|
|    |    |    |
|    |    |    |
""")
        objs['/'] = self._build_character("""
|    |    |1.00|
|    |0.16|0.16|
|    |1.00|    |
|0.16|0.16|    |
|1.00|    |    |
|    |    |    |
|    |    |    |
""")
        objs['|'] = self._build_character("""
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |    |    |
|    |    |    |
""")
        objs['~'] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|    |1.00|    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs['`'] = self._build_character("""
|1.00|1.00|    |
|    |    |0.32|
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        return objs
