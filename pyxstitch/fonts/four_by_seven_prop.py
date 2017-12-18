#!/usr/bin/python
"""An ASCII 4x7 proportional) pattern."""
from pyxstitch.font import BaseFontFactory
from pyxstitch.fonts.three_by_seven_mono import ThreeBySevenMono


class FourBySevenProp(BaseFontFactory):
    """Font factory definition."""

    def _display(self):
        """Display name."""
        return self._proportional_ascii()

    def _height_width(self):
        """Height and width of font."""
        return (7, 4)

    def _initialize_characters(self):
        """Initialize default characters."""
        self._can_strip = True
        objs = {}
        objs['A'] = self._build_character("""
|    |1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['B'] = self._build_character("""
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['C'] = self._build_character("""
|    |1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|    |    |    |
|1.00|    |    |1.00|
|    |1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['D'] = self._build_character("""
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['E'] = self._build_character("""
|1.00|1.00|1.00|1.00|
|1.00|    |    |    |
|1.00|1.00|1.00|    |
|1.00|    |    |    |
|1.00|1.00|1.00|1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['F'] = self._build_character("""
|1.00|1.00|1.00|1.00|
|1.00|    |    |    |
|1.00|1.00|1.00|    |
|1.00|    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['G'] = self._build_character("""
|    |1.00|1.00|1.00|
|1.00|    |    |    |
|1.00|    |1.00|1.00|
|1.00|    |    |1.00|
|    |1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['H'] = self._build_character("""
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|1.00|1.00|1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['J'] = self._build_character("""
|    |    |    |1.00|
|    |    |    |1.00|
|    |    |    |1.00|
|1.00|    |    |1.00|
|    |1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['K'] = self._build_character("""
|1.00|    |    |1.00|
|1.00|    |1.00|    |
|1.00|1.00|    |    |
|1.00|    |1.00|    |
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['L'] = self._build_character("""
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|1.00|1.00|1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['m'] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|1.00|    |    |1.00|
|1.00|0.32|0.16|1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['M'] = self._build_character("""
|1.00|    |    |1.00|
|1.00|0.32|0.16|1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['N'] = self._build_character("""
|1.00|    |1.00|    |
|1.00|0.32|1.00|    |
|1.00|1.00|1.00|    |
|1.00|0.32|1.00|    |
|1.00|    |1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['O'] = self._build_character("""
|    |1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|    |1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['P'] = self._build_character("""
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|1.00|    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['Q'] = self._build_character("""
|    |1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |0.32|1.00|
|    |1.00|1.00|0.32|
|    |    |    |    |
|    |    |    |    |
""")
        objs['R'] = self._build_character("""
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|1.00|    |1.00|    |
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['S'] = self._build_character("""
|    |1.00|1.00|1.00|
|1.00|    |    |    |
|    |1.00|1.00|    |
|    |    |    |1.00|
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['U'] = self._build_character("""
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|    |1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['V'] = self._build_character("""
|1.00|    |1.00|    |
|1.00|    |1.00|    |
|1.00|    |1.00|    |
|0.32|    |0.16|    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['w'] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|1.00|    |    |1.00|
|1.00|0.16|0.32|1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['W'] = self._build_character("""
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|1.00|0.16|0.32|1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['0'] = self._build_character("""
|    |1.00|    |    |
|1.00|    |1.00|    |
|1.00|0.16|1.00|    |
|1.00|    |1.00|    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['1'] = self._build_character("""
|0.18|1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['2'] = self._build_character("""
|1.00|1.00|    |    |
|    |    |1.00|    |
|1.00|1.00|    |    |
|1.00|    |    |    |
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['5'] = self._build_character("""
|1.00|1.00|1.00|    |
|1.00|    |    |    |
|    |1.00|1.00|    |
|    |    |1.00|    |
|1.00|1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['k'] = self._build_character("""
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |1.00|    |
|1.00|1.00|    |    |
|1.00|    |1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['h'] = self._build_character("""
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|    |    |1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['d'] = self._build_character("""
|    |    |    |1.00|
|    |    |    |1.00|
|    |1.00|1.00|1.00|
|1.00|    |    |1.00|
|    |1.00|1.00|1.00|
|    |    |    |    |
|    |    |    |    |
""")
        objs['f'] = self._build_character("""
|    |1.00|1.00|    |
|    |1.00|    |    |
|1.00|1.00|1.00|    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['t'] = self._build_character("""
|    |1.00|    |    |
|    |1.00|    |    |
|1.00|1.00|1.00|    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['l'] = self._build_character("""
|    |1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['i'] = self._build_character("""
|    |    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['p'] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|1.00|    |    |    |
|1.00|    |    |    |
""")
        objs[':'] = self._build_character("""
|    |    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs[';'] = self._build_character("""
|    |    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|1.00|    |    |    |
|0.20|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs[')'] = self._build_character("""
|1.00|    |    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['('] = self._build_character("""
|    |1.00|    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['!'] = self._build_character("""
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['.'] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs[','] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|1.00|    |    |    |
|0.20|    |    |    |
|    |    |    |    |
""")
        objs[']'] = self._build_character("""
|1.00|1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |1.00|    |    |
|1.00|1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['['] = self._build_character("""
|1.00|1.00|    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['3'] = self._build_character("""
|1.00|1.00|    |    |
|    |    |1.00|    |
|    |1.00|    |    |
|    |    |1.00|    |
|1.00|1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['4'] = self._build_character("""
|1.00|    |1.00|    |
|1.00|    |1.00|    |
|1.00|1.00|1.00|    |
|    |    |1.00|    |
|    |    |1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['9'] = self._build_character("""
|    |1.00|    |    |
|1.00|    |1.00|    |
|1.00|1.00|1.00|    |
|    |    |1.00|    |
|1.00|1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['6'] = self._build_character("""
|    |1.00|1.00|    |
|1.00|    |    |    |
|1.00|1.00|1.00|    |
|1.00|    |1.00|    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['7'] = self._build_character("""
|1.00|1.00|1.00|1.00|
|    |    |    |1.00|
|    |    |1.00|    |
|    |1.00|    |    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['8'] = self._build_character("""
|1.00|1.00|1.00|    |
|1.00|    |1.00|    |
|1.00|1.00|1.00|    |
|1.00|    |1.00|    |
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['q'] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|    |1.00|1.00|    |
|1.00|    |    |1.00|
|    |1.00|1.00|1.00|
|    |    |    |1.00|
|    |    |    |1.00|
""")
        objs['j'] = self._build_character("""
|    |    |    |    |
|    |    |1.00|    |
|    |    |    |    |
|    |    |1.00|    |
|    |    |1.00|    |
|1.00|    |1.00|    |
|    |1.00|    |    |
""")
        objs['b'] = self._build_character("""
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|1.00|1.00|    |
|1.00|    |    |1.00|
|1.00|1.00|1.00|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['$'] = self._build_character("""
|    |1.00|    |    |
|0.16|1.00|1.00|    |
|0.32|1.00|0.32|    |
|1.00|1.00|0.16|    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['@'] = self._build_character("""
|    |    |    |    |
|0.16|0.01|0.32|    |
|0.04|1.00|0.08|    |
|0.32|0.02|0.40|    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['&'] = self._build_character("""
|    |1.00|    |    |
|1.00|    |1.00|    |
|    |1.00|    |    |
|1.00|    |0.1024|    |
|    |1.00|0.8192|    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['|'] = self._build_character("""
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|1.00|    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['~'] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|1.00|    |1.00|    |
|    |1.00|    |1.00|
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        objs['`'] = self._build_character("""
|1.00|    |    |    |
|    |1.00|    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
""")
        basis = ThreeBySevenMono()._initialize_characters()
        for k in basis.keys():
            if k in objs:
                continue
            old = basis[k].raw
            parts = old.split("\n")
            parts = ["{}    |".format(x) for x in parts if len(x) != 0]
            objs[k] = self._build_character("\n".join(parts))
        return objs
