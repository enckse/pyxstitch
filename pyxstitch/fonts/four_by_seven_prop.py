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
        basis = ThreeBySevenMono()._initialize_characters()
        for k in basis.keys():
            old = basis[k].raw
            parts = old.split("\n")
            parts = [x + "    |" for x in parts if len(x.strip()) != 0]
            objs[k] = self._build_character("\n".join(parts))
        return objs
