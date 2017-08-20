#!/usr/bin/python
"""
A formatter implementation for pygments.

Takes a text stream and converts to a cross stitch output (HTML).
"""

from pygments.formatter import Formatter
import webcolors as wc
import pyxstitch.font as ft
import pyxstitch.symbols as sym
from pyxstitch.output import PILFormat, TextFormat, MULTI_PAGE_OFF
from pyxstitch.config import Config
from pyxstitch.floss import Floss
from math import floor
from enum import Enum


class Style(object):
    """Output/legend formatting."""

    def __init__(self, name, symbol, color, hex_vals):
        """Init the instance."""
        self.name = name
        self.symbol = symbol
        self.color = color
        self.hex = hex_vals

    def save(self):
        """Save to metadata format."""
        return [self.name, self.symbol, self.color]


class Legend(object):
    """Legend object."""

    def __init__(self):
        """Init the instance."""
        self._stitches = {}
        self._entries = []

    def add_raw_stitch(self, raw_color):
        """Add raw stitch edge."""
        if raw_color not in self._stitches:
            self._stitches[raw_color] = 0
        self._stitches[raw_color] += 1

    def add(self, dmc, raw_color, style):
        """New legend entry."""
        self._entries.append((dmc, raw_color, style.symbol, style.color))

    def build(self):
        """Build output legend."""
        headers = []
        cols = ("dmc", "color", "symbol", "edges", "floss")
        delim = []
        for col in cols:
            delim.append("---")
        headers.append(cols)
        headers.append(tuple(delim))
        output = []
        for item in self._entries:
            raw = item[1]
            dmc = item[0]
            output.append(("{} ({})".format(dmc.name, dmc.rgb),
                           "{} ({})".format(raw, item[3]),
                           item[2],
                           self._stitches[raw],
                           dmc.floss_number))
        return ["{:>40} {:>20} {:>7} {:>6} {:>6}".format(x[0],
                                                         x[1],
                                                         x[2],
                                                         x[3],
                                                         x[4])
                for x in headers + sorted(set(output))]


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
        self.font_factory = ft.Font().new_font_object()
        self.colorize = False
        self.dark = False
        self._lines = 'lightgrey'
        self._symbols = 'black'
        self.file_name = None
        self.is_raw = False
        self._writer = None
        self.as_dmc = True
        self.is_multipage = None
        self.config = None
        for token, style in self.style:
            if style['color']:
                self._colors[token] = style['color']

    def preprocess(self, text):
        """Process text before lexer."""
        return self.font_factory.process(text)

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
        use_hex = self._to_hex(use_color)
        return Style(self._get_color(use_hex),
                     self.symbol_generator.next(use_color),
                     use_color,
                     use_hex)

    def _new_entry(self, ch, style):
        """new entry to process."""
        char = self.font_factory.get(ch)
        return (char, style, ch)

    def _legend(self, items, size):
        """Create legend chunk."""
        for i in range(0, len(items), size):
            yield items[i:i + size]

    def _init_output(self, outfile):
        """Init output."""

    def format(self, tokensource, outfile):
        """Override to format."""
        if self.dark:
            self._symbols = 'white'
            self._default_color = '000000'
        if self.is_raw:
            self._writer = TextFormat()
        else:
            self._writer = PILFormat()
        entries = []
        current = []
        calc_height = 0
        calc_width = 0

        def _line(cur_height, cur_width, cur, entries):
            """Create a new line."""
            use_width = cur_width
            if len(cur) > use_width:
                use_width = len(cur)
            entries.append(cur)
            if len(cur) == 0:
                entries.append([self._new_entry(' ', styles)])
            return (cur_height + 1, use_width, [])

        for ttype, value in tokensource:
            while ttype not in self._colors:
                if ttype.parent is not None:
                    ttype = ttype.parent
                else:
                    break
            styles = self._token_color(ttype)
            if value is not None and '\n' in value and len(value) == 0:
                calc_height, calc_width, current = _line(calc_height,
                                                         calc_width,
                                                         current,
                                                         entries)
            else:
                for ch in value:
                    if ch == '\n':
                        calc_height, calc_width, current = _line(calc_height,
                                                                 calc_width,
                                                                 current,
                                                                 entries)
                    else:
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
        legend_min = 500
        top_pad = 50
        left_pad = 50
        legend_req = legend_min + left_pad
        width_size = (calc_width * offset + left_pad)
        if width_size < legend_req:
            width_size = legend_req
        self._writer.init('RGB',
                          (width_size,
                           (calc_height * offset) + top_pad + legend),
                          default_rgb,
                          self.is_multipage,
                          Config(self.config))
        y = -1
        lines = []
        lgd = Legend()
        floss = Floss()
        for entry in entries:
            for height in self.font_factory.height():
                y += 1
                x = -1
                grid = []
                has = False
                for cur, style, ch in entry:
                    coloring = style.name
                    color = self._symbols
                    self._writer.meta(cur.metadata(), style.save(), ch)
                    if self.colorize:
                        color = coloring
                    for cell in cur.cells(height):
                        x += 1
                        x_start = left_pad + offset + 0 + x * offset
                        y_start = top_pad + offset + 0 + y * offset
                        x_end = left_pad + offset + offset + x * offset
                        y_end = top_pad + offset + offset + y * offset
                        self._writer.rect([(x_start, y_start), (x_end, y_end)],
                                          outline=self._lines)
                        for stitch in cell:
                            lgd.add_raw_stitch(coloring)
                            dmc = floss.lookup(style.color, style.hex)
                            if self.colorize and self.as_dmc:
                                color = '#' + dmc.rgb
                            lgd.add(dmc, coloring, style)
                            if isinstance(stitch, ft.BackStitch):
                                if stitch in [ft.BackStitch.TopLeftBottomRight,
                                              ft.BackStitch.TopLeft,
                                              ft.BackStitch.BottomRight]:
                                    x_st = x_start
                                    y_st = y_start
                                    x_en = x_end
                                    y_en = y_end
                                    if stitch == ft.BackStitch.TopLeft:
                                        y_en = y_en - (offset / 2)
                                        x_en = x_en - (offset / 2)
                                    if stitch == ft.BackStitch.BottomRight:
                                        y_st = y_st + (offset / 2)
                                        x_st = x_st + (offset / 2)
                                    lines.append((x_st,
                                                  y_st,
                                                  x_en,
                                                  y_en,
                                                  color))
                                if stitch in [ft.BackStitch.BottomLeftTopRight,
                                              ft.BackStitch.BottomLeft,
                                              ft.BackStitch.TopRight]:
                                    x_st = x_start
                                    y_st = y_start
                                    x_en = x_end
                                    y_en = y_end
                                    if stitch == ft.BackStitch.BottomLeft:
                                        y_st = y_st + (offset / 2)
                                        x_en = x_en - (offset / 2)
                                    if stitch == ft.BackStitch.TopRight:
                                        y_en = y_en - (offset / 2)
                                        x_st = x_st + (offset / 2)
                                    lines.append((x_st,
                                                  y_en,
                                                  x_en,
                                                  y_st,
                                                  color))
                                if stitch == ft.BackStitch.TopLeftMid:
                                    lines.append((x_start,
                                                  y_start,
                                                  x_start + (offset / 2),
                                                  y_end,
                                                  color))
                                if stitch == ft.BackStitch.TopRightMid:
                                    lines.append((x_end,
                                                  y_start,
                                                  x_end - (offset / 2),
                                                  y_end,
                                                  color))
                                if stitch == ft.BackStitch.Left:
                                    lines.append((x_start,
                                                  y_start,
                                                  x_start,
                                                  y_end,
                                                  color))
                                if stitch == ft.BackStitch.Right:
                                    lines.append((x_end,
                                                  y_start,
                                                  x_end,
                                                  y_end,
                                                  color))
                                if stitch == ft.BackStitch.Top:
                                    lines.append((x_start,
                                                  y_start,
                                                  x_end,
                                                  y_start,
                                                  color))
                                if stitch == ft.BackStitch.Bottom:
                                    lines.append((x_start,
                                                  y_end,
                                                  x_end,
                                                  y_end,
                                                  color))
                            if isinstance(stitch, ft.Stitch):
                                if stitch == ft.Stitch.CrossStitch:
                                    lgd.add_raw_stitch(coloring)
                                    x_pos = left_pad + offset + 2 + x * offset
                                    self._writer.text((x_pos, y_start),
                                                      style.symbol,
                                                      color)
                        has = True
                if not has:
                    y -= 1
        # NOTE: we draw backstitch lines LAST to prevent overwrite
        for l in lines:
            self._writer.line((l[0], l[1], l[2], l[3]), fill=l[4])
        # add labels
        for h in range(calc_height):
            if h == 0:
                for w in range(calc_width):
                    if w % 10 == 0 or w == mid_width:
                        char = str(w)
                        if w == mid_width:
                            char = "X"
                        self._writer.text((left_pad + w * offset, top_pad - 5),
                                          char,
                                          self._symbols)
            if h % 10 == 0 or h == mid_height:
                char = str(h)
                if h == mid_height:
                    char = 'X'
                self._writer.text((left_pad - 5, top_pad + h * offset),
                                  char,
                                  self._symbols)
        chunk_idx = 0
        legend_tab = lgd.build()
        leg_height = (calc_height * offset) - (legend / 4)
        chunks = 8
        if self.is_multipage != MULTI_PAGE_OFF:
            chunks = 100
        for chunk in self._legend(legend_tab, chunks):
            self._writer.legend((offset * 2 + (chunk_idx * legend_min),
                                 leg_height),
                                "\n".join(chunk),
                                self._symbols)
            chunk_idx += 1
        self._writer.save(self.file_name)
