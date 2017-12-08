#!/usr/bin/python
"""An ASCII 3x6 proportional) pattern."""
from pyxstitch.font import BaseFontFactory
from pyxstitch.fonts.three_by_seven_mono import ThreeBySevenMono


class ThreeBySixProp(BaseFontFactory):
    """Font factory definition."""

    def _display(self):
        """Display name."""
        return self._proportional_ascii()

    def _height_width(self):
        """Height and width of font."""
        return (6, 3)

    def _initialize_characters(self):
        """Initialize default characters."""
        self._can_strip = True
        objs = {}
        basis = ThreeBySevenMono()._initialize_characters()
        for k in basis.keys():
            old = basis[k].raw
            parts = old.split("\n")
            parts = parts[:len(parts) - 2]
            objs[k] = self._build_character("\n".join(parts))
        objs[")"] = self._build_character("""
|1.00|    |    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|    |    |
|    |    |    |
""")
        objs["("] = self._build_character("""
|    |1.00|    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|    |1.00|    |
|    |    |    |
""")
        objs["|"] = self._build_character("""
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|    |    |    |
""")
        objs["`"] = self._build_character("""
|1.00|    |    |
|    |1.00|    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs[":"] = self._build_character("""
|    |    |    |
|1.00|    |    |
|    |    |    |
|1.00|    |    |
|    |    |    |
|    |    |    |
""")
        objs[";"] = self._build_character("""
|    |    |    |
|1.00|    |    |
|    |    |    |
|1.00|    |    |
|0.20|    |    |
|    |    |    |
""")
        objs["'"] = self._build_character("""
|1.00|    |    |
|0.40|    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""")
        objs["."] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|1.00|    |    |
|    |    |    |
""")
        objs[","] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|1.00|    |    |
|0.20|    |    |
""")
        objs["!"] = self._build_character("""
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|    |    |    |
|1.00|    |    |
|    |    |    |
""")
        objs["]"] = self._build_character("""
|1.00|1.00|    |
|    |1.00|    |
|    |1.00|    |
|    |1.00|    |
|1.00|1.00|    |
|    |    |    |
""")
        objs["["] = self._build_character("""
|1.00|1.00|    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|1.00|    |
|    |    |    |
""")
        objs["c"] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|    |    |
|    |1.00|    |
|    |    |    |
""")
        objs["l"] = self._build_character("""
|    |    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|1.00|    |    |
|    |    |    |
""")
        objs["j"] = self._build_character("""
|    |    |    |
|    |    |1.00|
|    |    |    |
|    |    |1.00|
|    |    |1.00|
|1.00|1.00|    |
""")
        objs["y"] = self._build_character("""
|    |    |    |
|    |    |    |
|1.00|    |1.00|
|1.00|    |1.00|
|    |1.00|1.00|
|0.02|0.02|1.00|
""")
        objs["g"] = self._build_character("""
|    |    |    |
|    |    |    |
|    |1.00|    |
|1.00|    |1.00|
|    |1.00|1.00|
|0.02|0.02|1.00|
""")
        objs["i"] = self._build_character("""
|    |    |    |
|1.00|    |    |
|    |    |    |
|1.00|    |    |
|1.00|    |    |
|    |    |    |
""")
        objs[" "] = self._build_character("""
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
|    |    |    |
""", char_strip=False)
        return objs
