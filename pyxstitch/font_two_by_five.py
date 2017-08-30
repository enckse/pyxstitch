#!/usr/bin/python
"""An ASCII 2x5 (monospace) backstitch pattern"""
from pyxstitch.font import BaseFontFactory


class TwoByFive(BaseFontFactory):
    """Font factory definition."""

    def _height_width(self):
        """Height and width of font."""
        return (5, 2)

    def _initialize_characters(self):
        """Initializedefaultcharacters"""
        objs = {}
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
|0.16|0.32|
|0.32|    |
|    |0.32|
|0.32|0.16|
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
|0.16|0.32|
|    |0.08|
|    |0.16|
|0.18|0.02|
|    |    |
""")
        objs['3'] = self._build_character("""
|0.01|0.32|
|    |0.16|
|0.01|0.32|
|0.02|0.16|
|    |    |
""")
        objs['u'] = self._build_character("""
|    |    |
|    |    |
|0.04|0.08|
|0.32|0.10|
|    |    |
""")
        objs['a'] = self._build_character("""
|    |    |
|    |    |
|0.16|0.32|
|0.32|0.24|
|    |    |
""")
        objs['c'] = self._build_character("""
|    |    |
|    |    |
|0.16|0.01|
|0.32|0.02|
|    |    |
""")
        objs['k'] = self._build_character("""
|0.04|    |
|0.04|    |
|0.04|0.16|
|0.05|0.32|
|    |    |
""")
        objs['h'] = self._build_character("""
|0.04|    |
|0.04|    |
|0.05|0.32|
|0.04|0.08|
|    |    |
""")
        objs['d'] = self._build_character("""
|    |0.08|
|    |0.10|
|0.16|0.08|
|0.32|0.10|
|    |    |
""")
        objs['e'] = self._build_character("""
|    |    |
|    |    |
|0.18|0.34|
|0.32|0.02|
|    |    |
""")
        objs['f'] = self._build_character("""
|    |0.05|
|0.02|0.06|
|    |0.04|
|    |0.04|
|    |    |
""")
        objs['t'] = self._build_character("""
|    |0.04|
|0.02|0.06|
|    |0.04|
|    |0.04|
|    |    |
""")
        objs['#'] = self._build_character("""
|0.2048|0.2048|
|0.16385|0.16385|
|0.16386|0.16386|
|0.2048|0.2048|
|    |    |
""")
        objs['"'] = self._build_character("""
|0.04|0.08|
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs["'"] = self._build_character("""
|0.08|    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['g'] = self._build_character("""
|    |    |
|    |    |
|0.16|0.32|
|0.32|0.10|
|0.02|0.10|
""")
        objs['l'] = self._build_character("""
|    |0.04|
|    |0.04|
|    |0.04|
|0.10|0.02|
|    |    |
""")
        objs['i'] = self._build_character("""
|    |    |
|    |0.04|
|    |    |
|0.10|0.02|
|    |    |
""")
        objs['n'] = self._build_character("""
|    |    |
|    |    |
|0.05|0.32|
|0.04|0.08|
|    |    |
""")
        objs['m'] = self._build_character("""
|    |    |
|    |    |
|0.36|0.24|
|0.04|0.08|
|    |    |
""")
        objs['w'] = self._build_character("""
|    |    |
|    |    |
|0.04|0.08|
|0.20|0.40|
|    |    |
""")
        objs['o'] = self._build_character("""
|    |    |
|    |    |
|0.16|0.32|
|0.32|0.16|
|    |    |
""")
        objs['p'] = self._build_character("""
|    |    |
|    |    |
|0.05|0.32|
|0.06|0.16|
|0.04|    |
""")

        objs[':'] = self._build_character("""
|    |    |
|0.08|    |
|    |    |
|0.08|    |
|    |    |
""")
        objs[';'] = self._build_character("""
|    |    |
|0.08|    |
|    |    |
|0.08|    |
|0.08|    |
""")
        objs['}'] = self._build_character("""
|0.09|    |
|0.08|0.02|
|0.08|    |
|0.10|    |
|    |    |
""")
        objs[')'] = self._build_character("""
|0.01|0.1024|
|    |0.8192|
|    |0.2048|
|0.02|0.4096|
|    |    |
""")
        objs['s'] = self._build_character("""
|    |    |
|    |    |
|0.18|0.03|
|0.02|0.16|
|    |    |
""")
        objs['>'] = self._build_character("""
|0.32|    |
|    |0.32|
|    |0.16|
|0.16|    |
|    |    |
""")
        objs['<'] = self._build_character("""
|    |0.16|
|0.16|    |
|0.32|    |
|    |0.32|
|    |    |
""")
        objs['{'] = self._build_character("""
|    |0.05|
|0.02|0.04|
|    |0.04|
|    |0.06|
|    |    |
""")
        objs['('] = self._build_character("""
|0.2048|0.01|
|0.4096|    |
|0.1024|    |
|0.8192|0.02|
|    |    |
""")
        objs['r'] = self._build_character("""
|    |    |
|    |0.02|
|0.16|    |
|0.04|    |
|    |    |
""")
        objs['!'] = self._build_character("""
|0.08|    |
|0.08|    |
|    |    |
|0.08|    |
|    |    |
""")
        objs['4'] = self._build_character("""
|0.04|0.08|
|0.06|0.10|
|    |0.08|
|    |0.08|
|    |    |
""")
        objs[','] = self._build_character("""
|    |    |
|    |    |
|    |    |
|0.08|    |
|0.08|    |
""")
        objs['_'] = self._build_character("""
|    |    |
|    |    |
|0.02|0.02|
|    |    |
|    |    |
""")
        objs['='] = self._build_character("""
|0.02|0.02|
|    |    |
|0.02|0.02|
|    |    |
|    |    |
""")
        objs['5'] = self._build_character("""
|0.05|0.01|
|0.06|0.02|
|    |0.08|
|0.32|0.16|
|    |    |
""")
        objs[']'] = self._build_character("""
|0.01|0.09|
|    |0.08|
|    |0.08|
|0.02|0.10|
|    |    |
""")
        objs['['] = self._build_character("""
|0.05|0.01|
|0.04|    |
|0.04|    |
|0.06|0.02|
|    |    |
""")
        objs['6'] = self._build_character("""
|0.16|    |
|0.04|    |
|0.20|0.32|
|0.32|0.16|
|    |    |
""")
        objs['7'] = self._build_character("""
|0.05|0.2049|
|    |0.4096|
|0.2048|    |
|0.4096|    |
|    |    |
""")
        objs['8'] = self._build_character("""
|0.16|0.32|
|0.32|0.16|
|0.16|0.32|
|0.32|0.16|
|    |    |
""")
        objs['9'] = self._build_character("""
|0.16|0.32|
|0.32|0.24|
|    |0.08|
|    |0.16|
|    |    |
""")
        objs['.'] = self._build_character("""
|    |    |
|    |    |
|    |    |
|0.08|    |
|    |    |
""")
        objs['|'] = self._build_character("""
|0.08|    |
|0.08|    |
|0.08|    |
|0.08|    |
|    |    |
""")
        objs['q'] = self._build_character("""
|    |    |
|    |    |
|0.16|0.32|
|0.32|0.10|
|    |0.08|
""")
        objs['j'] = self._build_character("""
|    |    |
|    |0.08|
|    |    |
|    |0.08|
|0.32|0.16|
""")
        objs['v'] = self._build_character("""
|    |    |
|    |    |
|0.1024|0.2048|
|0.8192|0.4096|
|    |    |
""")
        objs['x'] = self._build_character("""
|    |    |
|    |    |
|0.32|0.16|
|0.16|0.32|
|    |    |
""")
        objs['y'] = self._build_character("""
|    |    |
|    |    |
|0.04|0.08|
|0.32|0.10|
|0.02|0.16|
""")
        objs['Z'] = self._build_character("""
|0.01|0.2049|
|    |0.4096|
|0.2049|0.01|
|0.4098|0.02|
|    |    |
""")
        objs['z'] = self._build_character("""
|    |    |
|    |    |
|0.01|0.17|
|0.18|0.02|
|    |    |
""")
        objs['b'] = self._build_character("""
|0.04|    |
|0.06|    |
|0.04|0.32|
|0.06|0.16|
|    |    |
""")
        objs['%'] = self._build_character("""
|1.00|    |
|    |0.16|
|0.16|    |
|    |1.00|
|    |    |
""")
        objs['$'] = self._build_character("""
|0.24|0.32|
|0.40|    |
|0.08|0.32|
|0.40|0.16|
|    |    |
""")
        objs['@'] = self._build_character("""
|0.16|0.32|
|0.04|0.08|
|0.04|0.40|
|0.32|0.02|
|    |    |
""")
        objs['*'] = self._build_character("""
|    |    |
|0.42|0.18|
|0.24|0.32|
|    |    |
|    |    |
""")
        objs['&'] = self._build_character("""
|0.16|0.32|
|0.32|0.16|
|0.24|0.16|
|0.40|0.32|
|    |    |
""")
        objs['+'] = self._build_character("""
|    |    |
|0.10|0.02|
|    |0.04|
|    |    |
|    |    |
""")
        objs['-'] = self._build_character("""
|    |    |
|0.02|0.02|
|    |    |
|    |    |
|    |    |
""")
        objs['^'] = self._build_character("""
|0.16|0.32|
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['?'] = self._build_character("""
|0.16|0.32|
|    |0.16|
|    |    |
|    |0.04|
|    |    |
""")
        objs['\\'] = self._build_character("""
|0.1024|    |
|0.8192|    |
|    |0.1024|
|    |0.8192|
|    |    |
""")
        objs['/'] = self._build_character("""
|    |0.2048|
|    |0.4096|
|0.2048|    |
|0.4096|    |
|    |    |
""")
        objs[' '] = self._build_character("""
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
""")
        objs['~'] = self._build_character("""
|    |    |
|0.12288|    |
|    |0.3072|
|    |    |
|    |    |
""")
        objs['`'] = self._build_character("""
|0.01|0.32|
|    |    |
|    |    |
|    |    |
|    |    |
""")
        return objs
