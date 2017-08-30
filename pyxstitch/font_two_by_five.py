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
|    |0.08|
|    |0.08|
|    |0.08|
|0.32|0.16|
|    |    |
""")
        objs['K'] = self._build_character("""
|0.04|0.16|
|0.20|    |
|0.36|    |
|0.04|0.32|
|    |    |
""")
        objs['L'] = self._build_character("""
|0.04|    |
|0.04|    |
|0.04|    |
|0.06|0.02|
|    |    |
""")
        objs['M'] = self._build_character("""
|0.36|0.24|
|0.12|0.08|
|0.04|0.08|
|0.04|0.08|
|    |    |
""")
        objs['N'] = self._build_character("""
|0.04|0.08|
|0.36|0.08|
|0.04|0.40|
|0.04|0.08|
|    |    |
""")
        objs['O'] = self._build_character("""
|0.16|0.32|
|0.04|0.08|
|0.04|0.08|
|0.32|0.16|
|    |    |
""")
        objs['P'] = self._build_character("""
|0.05|0.32|
|0.06|0.16|
|0.04|    |
|0.04|    |
|    |    |
""")
        objs['Q'] = self._build_character("""
|0.16|0.32|
|0.04|0.08|
|0.04|0.08|
|0.32|1.00|
|    |    |
""")
        objs['R'] = self._build_character("""
|0.05|0.32|
|0.06|0.16|
|0.36|    |
|0.04|0.32|
|    |    |
""")
        objs['S'] = self._build_character("""
|0.05|0.01|
|0.06|0.02|
|    |0.08|
|0.02|0.10|
|    |    |
""")
        objs['T'] = self._build_character("""
|0.01|0.05|
|    |0.04|
|    |0.04|
|    |0.04|
|    |    |
""")
        objs['U'] = self._build_character("""
|0.04|0.08|
|0.04|0.08|
|0.04|0.08|
|0.32|0.16|
|    |    |
""")
        objs['V'] = self._build_character("""
|0.04|0.08|
|0.04|0.08|
|0.1024|0.2048|
|0.8192|0.4096|
|    |    |
""")
        objs['W'] = self._build_character("""
|0.04|0.08|
|0.04|0.08|
|0.12|0.08|
|0.20|0.40|
|    |    |
""")
        objs['X'] = self._build_character("""
|0.1024|0.2048|
|0.8192|0.4096|
|0.2048|0.1024|
|0.4096|0.8192|
|    |    |
""")
        objs['Y'] = self._build_character("""
|0.1024|0.2048|
|0.8192|0.4096|
|0.08|    |
|0.08|    |
|    |    |
""")
        objs['0'] = self._build_character("""
|0.16|0.32|
|0.04|0.24|
|0.20|0.08|
|0.32|0.16|
|    |    |
""")
        objs['1'] = self._build_character("""
|0.24|    |
|0.08|    |
|0.08|    |
|0.10|0.02|
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
