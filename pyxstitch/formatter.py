#!/usr/bin/python
"""
A formatter implementation for pygments.

Takes a text stream and converts to a cross stitch output (HTML).
"""

from pygments.formatter import Formatter
import webcolors as wc
import pyxstitch.font as ft
import pyxstitch.symbols as sym
from math import floor
from enum import Enum
from PIL import Image, ImageFont, ImageDraw


class CrossStitchFormatter(Formatter):
    """Formats output as a cross stitch pattern."""

    _HEX = '0123456789abcdefABCDEF'

    def __init__(self, **options):
        """Initialize the instance."""
        Formatter.__init__(self, **options)
        self._hex = {x: int(x, 16) for x in
                     (y + z for y in self._HEX for z in self._HEX)}
        self._colors = {}
        self._default_color = "ffffff"
        self.symbol_generator = sym.DefaultSymbolGenerator()
        self.font_factory = ft.DefaultFontFactory()
        self.colorize = False
        self.dark = False
        self._lines = 'lightgrey'
        self._symbols = 'black'

        for token, style in self.style:
            if style['color']:
                self._colors[token] = style['color']

    def _closest(self, rgb):
        """We need to find a color approximation."""
        min_col = {}
        for key, name in wc.css3_hex_to_names.items():
            r, g, b = wc.hex_to_rgb(key)
            r_conv = (r - rgb[0]) ** 2
            g_conv = (g - rgb[1]) ** 2
            b_conv = (b - rgb[2]) ** 2
            min_col[(r_conv + g_conv + b_conv)] = name
        return min_col[min(min_col.keys())]

    def _get_color(self, rgb):
        """Get the color name from rgb or the closest name...please."""
        actua = None
        try:
            actual = wc.rgb_to_name(rgb)
        except ValueError:
            actual = None
        if actual is None:
            return self._closest(rgb)
        return actual

    def _to_hex(self, rgb):
        """Convert a hex string 001122 -> tuple (0, 1, 2)."""
        return (self._hex[rgb[0:2]], self._hex[rgb[2:4]], self._hex[rgb[4:6]])

    def _token_color(self, token):
        """We need to get the color for a token."""
        use_color = self._default_color
        if token in self._colors:
            use_color = self._colors[token]
        return (self._get_color(self._to_hex(use_color)),
                self.symbol_generator.next(use_color))

    def _new_entry(self, ch, style):
        """new entry to process."""
        char = self.font_factory.get(ch)
        return (char, style)

    def format(self, tokensource, outfile):
        """Override to format."""
        if self.dark:
            self._symbols = 'white'
            self._default_color = '000000'
        entries = []
        current = []
        calc_height = 0
        calc_width = 0
        for ttype, value in tokensource:
            while ttype not in self._colors:
                if ttype.parent is not None:
                    ttype = ttype.parent
                else:
                    break
            styles = self._token_color(ttype)
            if value == "\n":
                calc_height += 1
                if len(current) > calc_width:
                    calc_width = len(current)
                entries.append(current)
                if len(current) == 0:
                    entries.append([self._new_entry(' ', styles)])
                current = []
            else:
                for ch in value:
                    current.append(self._new_entry(ch, styles))
        if len(current) > 0:
            calc_height += 1
            if len(current) > calc_width:
                calc_width = len(current)
            entries.append(current)
        calc_width += 1
        calc_width = ((calc_width * 2) +
                      (calc_width * max(self.font_factory.width())))
        mid_width = int(floor(calc_width / 2))
        calc_height += 1
        calc_height = (calc_height +
                       (calc_height * max(self.font_factory.height())))
        default_rgb = self._to_hex(self._default_color)
        mid_height = int(floor(calc_height / 2))
        offset = 10
        legend = 100
        im = Image.new('RGB',
                       (calc_width * offset,
                        (calc_height * offset) + legend),
                       default_rgb)
        dr = ImageDraw.Draw(im)
        y = -1
        lines = []
        legends = []
        for entry in entries:
            for height in self.font_factory.height():
                y += 1
                x = -1
                grid = []
                has = False
                for cur, style in entry:
                    symb = style[1]
                    coloring = style[0]
                    for cell in cur.cells(height):
                        x += 1
                        fill = None
                        if self.colorize and len(cell) > 0:
                            fill = coloring
                        x_start = offset + 0 + x * offset
                        y_start = offset + 0 + y * offset
                        x_end = offset + offset + x * offset
                        y_end = offset + offset + y * offset
                        dr.rectangle([(x_start, y_start), (x_end, y_end)],
                                     outline=self._lines,
                                     fill=fill)
                        for stitch in cell:
                            legends.append((coloring, symb))
                            if isinstance(stitch, ft.BackStitch):
                                if stitch == ft.BackStitch.TopLeftBottomRight:
                                    lines.append((x_start,
                                                  y_start,
                                                  x_end,
                                                  y_end))
                                if stitch == ft.BackStitch.BottomLeftTopRight:
                                    lines.append((x_start,
                                                  y_end,
                                                  x_end,
                                                  y_start))
                                if stitch == ft.BackStitch.Left:
                                    lines.append((x_start,
                                                  y_start,
                                                  x_start,
                                                  y_end))
                                if stitch == ft.BackStitch.Right:
                                    lines.append((x_end,
                                                  y_start,
                                                  x_end,
                                                  y_end))
                                if stitch == ft.BackStitch.Top:
                                    lines.append((x_start,
                                                  y_start,
                                                  x_end,
                                                  y_start))
                                if stitch == ft.BackStitch.Bottom:
                                    lines.append((x_start,
                                                  y_end,
                                                  x_end,
                                                  y_end))
                            if isinstance(stitch, ft.Stitch):
                                if stitch == ft.Stitch.CrossStitch:
                                    dr.text((offset + 2 + x * offset, y_start),
                                            symb,
                                            self._symbols)
                        has = True
                if not has:
                    y -= 1
        # NOTE: we draw backstitch lines LAST to prevent overwrite
        for l in lines:
            dr.line(l, fill=self._symbols)
        # add lables
        for h in range(calc_height):
            if h == 0:
                for w in range(calc_width):
                    if w % 10 == 0 or w == mid_width:
                        char = str(w)
                        if w == mid_width:
                            char = "X"
                        dr.text((w * offset, 0),
                                char,
                                self._symbols)
            if h % 10 == 0 or h == mid_height:
                char = str(h)
                if h == mid_height:
                    char = 'X'
                dr.text((0, h * offset),
                        char,
                        self._symbols)
        # and legend
        str_leg = sorted(["{} => {}".format(x[0], x[1]) for x in set(legends)])
        dr.text((offset * 2, calc_height * (offset)),
                " , ".join(str_leg),
                self._symbols)
        im.save('test.png')
