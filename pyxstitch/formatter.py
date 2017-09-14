#!/usr/bin/python
"""
A formatter implementation for pygments.

Takes a text stream and converts to a cross stitch output (HTML).
"""

from pygments.formatter import Formatter
import pyxstitch.font as ft
import pyxstitch.symbols as sym
import pyxstitch.version as vers
from pyxstitch.output import PILFormat, TextFormat, MULTI_PAGE_OFF
from pyxstitch.config import Config
from pyxstitch.floss import Floss
from math import floor
from enum import Enum


class Style(object):
    """Output/legend formatting."""

    def __init__(self, dmc, symbol, color):
        """Init the instance."""
        self.dmc = dmc
        self.symbol = symbol
        self.color = color

    def save(self):
        """Save to metadata format."""
        return [self.dmc.name, self.symbol, self.color]


class Legend(object):
    """Legend object."""

    def __init__(self):
        """Init the instance."""
        self._stitches = {}
        self._entries = []

    def add_raw_stitch(self, dmc):
        """Add raw stitch edge."""
        raw_color = dmc.name
        if raw_color not in self._stitches:
            self._stitches[raw_color] = 0
        self._stitches[raw_color] += 1

    def add(self, style):
        """New legend entry."""
        self._entries.append(style)

    def build(self):
        """Build output legend."""
        headers = []
        cols = ("dmc", "symbol", "edges", "floss")
        delim = []
        for col in cols:
            delim.append("---")
        headers.append(cols)
        headers.append(tuple(delim))
        output = []
        for item in self._entries:
            output.append(("{} ({})".format(item.dmc.name, item.dmc.rgb),
                           item.symbol,
                           self._stitches[item.dmc.name],
                           item.dmc.floss_number))
        return ["{:>40} {:>7} {:>6} {:>6}".format(x[0],
                                                  x[1],
                                                  x[2],
                                                  x[3])
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
        self._light_symbol = 'lightgrey'
        self.file_name = None
        self.is_raw = False
        self._writer = None
        self.is_multipage = None
        self.config = None
        self.is_bw = False
        self.floss = Floss()
        for token, style in self.style:
            if style['color']:
                self._colors[token] = style['color']

    def preprocess(self, text):
        """Process text before lexer."""
        return self.font_factory.process(text)

    def _to_hex(self, rgb):
        """Convert a hex string 001122 -> tuple (0, 1, 2)."""
        return (self._hex[rgb[0:2]], self._hex[rgb[2:4]], self._hex[rgb[4:6]])

    def _token_color(self, token):
        """We need to get the color for a token."""
        use_color = self._default_color
        if self.is_bw:
            use_color = "000000"
        if token in self._colors:
            use_color = self._colors[token]
        use_hex = self._to_hex(use_color)
        dmc = self.floss.lookup(use_hex)
        return Style(dmc,
                     self.symbol_generator.next(dmc.name),
                     use_color)

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
            self._light_symbol = 'darkgrey'
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
        mid_height = int(floor(calc_height / 2))
        offset = 10
        cfg = Config(self.config)
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
                          self._to_hex(self._default_color),
                          self.is_multipage,
                          cfg)
        self._writer.extras(cfg.dump())
        self._writer.text((offset, offset), vers.__version__, self._symbols)
        y = -1
        lines = []
        lgd = Legend()
        for entry in entries:
            for height in self.font_factory.height():
                y += 1
                x = -1
                grid = []
                has = False
                for cur, style, ch in entry:
                    dmc = style.dmc
                    color = self._symbols
                    self._writer.meta(cur.metadata(), style.save(), ch)
                    if self.colorize:
                        color = dmc.name
                    for cell in cur.cells(height):
                        x += 1
                        x_start = left_pad + offset + 0 + x * offset
                        y_start = top_pad + offset + 0 + y * offset
                        x_end = left_pad + offset + offset + x * offset
                        y_end = top_pad + offset + offset + y * offset
                        self._writer.rect([(x_start, y_start), (x_end, y_end)],
                                          outline=self._lines)
                        for stitch in cell:
                            lgd.add_raw_stitch(dmc)
                            if self.colorize:
                                color = '#' + dmc.rgb
                            lgd.add(style)
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
                                if stitch in [ft.BackStitch.Left,
                                              ft.BackStitch.TopLeftMid,
                                              ft.BackStitch.BottomLeftMid,
                                              ft.BackStitch.TopBottomMid]:
                                    x_en = x_start
                                    x_st = x_start
                                    if stitch in [ft.BackStitch.TopLeftMid,
                                                  ft.BackStitch.TopBottomMid]:
                                        x_en = x_en + (offset / 2)
                                    if stitch in [ft.BackStitch.BottomLeftMid,
                                                  ft.BackStitch.TopBottomMid]:
                                        x_st = x_st + (offset / 2)
                                    lines.append((x_st,
                                                  y_start,
                                                  x_en,
                                                  y_end,
                                                  color))
                                if stitch in [ft.BackStitch.Right,
                                              ft.BackStitch.TopRightMid,
                                              ft.BackStitch.BottomRightMid]:
                                    x_en = x_end
                                    x_st = x_end
                                    if stitch == ft.BackStitch.TopRightMid:
                                        x_en = x_en - (offset / 2)
                                    if stitch == ft.BackStitch.BottomRightMid:
                                        x_st = x_st - (offset / 2)
                                    lines.append((x_st,
                                                  y_start,
                                                  x_en,
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
                            if isinstance(stitch, ft.Stitch) or \
                               self.font_factory.is_backstitched:
                                if stitch == ft.Stitch.CrossStitch or \
                                   self.font_factory.is_backstitched:
                                    stitch_color = color
                                    if self.font_factory.is_backstitched:
                                        stitch_color = self._light_symbol
                                    lgd.add_raw_stitch(dmc)
                                    x_pos = left_pad + offset + 2 + x * offset
                                    self._writer.text((x_pos, y_start),
                                                      style.symbol,
                                                      stitch_color)
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
        leg_height = leg_height + cfg.legend_hoff
        chunks = 8
        if self.is_multipage != MULTI_PAGE_OFF:
            chunks = 100
        for chunk in self._legend(legend_tab, chunks):
            leg_width = offset * 2 + (chunk_idx * legend_min)
            self._writer.legend((leg_width + cfg.legend_woff,
                                 leg_height),
                                "\n".join(chunk),
                                self._symbols)
            chunk_idx += 1
        self._writer.save(self.file_name)
