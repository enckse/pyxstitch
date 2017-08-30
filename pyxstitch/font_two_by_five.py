#!/usr/bin/python
"""An ASCII 2x5 (monospace) backstitch pattern"""
from pyxstitch.font import BaseFontFactory


class TwoByFive(BaseFontFactory):
    """Font factory definition."""

    def _height_width(self):
        """Height and width of font."""
        return(5,2)

    def _initialize_characters(self):
        """Initializedefaultcharacters"""
        objs={}
        objs['A'] = self._build_character("""
|0.16|0.32|
|0.06|0.10|
|0.04|0.08|
|0.04|0.08|
|    |    |
""")
        objs['B'] = self._build_character("""
|0.05|0.32|
|0.06|0.16|
|0.04|0.32|
|0.06|0.16|
|    |    |
""")
        objs['C'] = self._build_character("""
|0.16|0.32|
|0.04|    |
|0.04|    |
|0.32|0.16|
|    |    |
""")
        objs['D'] = self._build_character("""
|0.05|0.32|
|0.04|0.08|
|0.04|0.08|
|0.06|0.16|
|    |    |
""")
        objs['E'] = self._build_character("""
|0.05|0.01|
|0.06|0.02|
|0.04|    |
|0.06|0.02|
|    |    |
""")
        objs['F'] = self._build_character("""
|0.05|0.01|
|0.06|0.02|
|0.04|    |
|0.04|    |
|    |    |
""")
        objs['G'] = self._build_character("""
|0.16|0.32|
|0.04|    |
|0.04|0.09|
|0.32|0.16|
|    |    |
""")
        objs['H'] = self._build_character("""
|0.04|0.08|
|0.06|0.10|
|0.04|0.08|
|0.04|0.08|
|    |    |
""")
        objs['I'] = self._build_character("""
|0.01|0.05|
|    |0.04|
|    |0.04|
|0.02|0.06|
|    |    |
""")
        objs['J'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['K'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['L'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['M'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['N'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['O'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['P'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['Q'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['R'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['S'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['T'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['U'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['V'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['W'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['X'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['Y'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['0'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['1'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['2'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['3'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['u'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['a'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['c'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['k'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['h'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['d'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['e'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['f'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['t'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['#'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['"'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs["'"] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['g'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['l'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['i'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['n'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['m'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['w'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['o'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['p'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")

        objs[':'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs[';'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['}'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs[')'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['s'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['>'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['<'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['{'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['('] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['r'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['!'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['4'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs[','] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['_'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['='] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['5'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs[']'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['['] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['6'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['7'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['8'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['9'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['.'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['|'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['q'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['j'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['v'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['x'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['y'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['Z'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['z'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['b'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['%'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['$'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['@'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['*'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['&'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['+'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['-'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['^'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['?'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['\\'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['/'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs[' '] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['~'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['`'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        return objs
