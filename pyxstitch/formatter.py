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

_BLTR_BS = "bltr-bs"
_TLBR_BS = "tlbr-bs"
_BS_STYLE = """
.STYLE:after{
    content:"";
    position:absolute;
    border-top:1px solid black;
    width:13px;
    ATTRS
}"""
_BLTR_BS_CSS = _BS_STYLE.replace("STYLE", _BLTR_BS).replace("ATTRS", """
    transform: rotate(135deg);
    transform-origin: 3px -1px;
""")
_TLBR_BS_CSS = _BS_STYLE.replace("STYLE", _TLBR_BS).replace("ATTRS", """
    transform: rotate(45deg);
    transform-origin: 5px -7px;
""")
_IMG = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUAQMAAAC3R49OAAAABlBMVEXv7+/v7+8tAJavAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAADElEQVQImWNgoC4AAABQAAGmLdqcAAAAAElFTkSuQmCC'
_HTML_STYLE = """
<style>
table {
    text-align: center;
}
tr {
    padding: 0px 0px 0px 0px;
}
td {
    background: url(IMG);
    width: 10px;
    height: 10px;
    font-size: 8px;
}

STYLE
</style>""".replace("STYLE", _BLTR_BS_CSS + _TLBR_BS_CSS).replace("IMG", _IMG)

_BORDER = "border-{}: 1px solid black"

_TABLE = "<table cellspacing='1'>"
_TABLE_END = "</table>"
_TD = '<td class="{}" style="{}">'
_TD_END = "</td>"
_TR = "<tr>" + _TD.format("", "") + "{}" + _TD_END + _TD.format("", "") + _TD_END
_TR_END = "</tr>"
_LEGEND = "<div class='legend'><p>{} => {}</p></div>"
_COLOR = "color: {}"

_DEFAULT_COLOR = "000000"


class Mode(Enum):
    HTML = 1
    Image = 2


class CrossStitchFormatter(Formatter):
    """Formats output as a cross stitch pattern."""

    _HEX = '0123456789abcdefABCDEF'

    def __init__(self, **options):
        """Initialize the instance."""
        Formatter.__init__(self, **options)
        self._hex = {x: int(x, 16) for x in
                     (y + z for y in self._HEX for z in self._HEX)}
        self._colors = {}

        self.default = _DEFAULT_COLOR
        self.symbol_generator = sym.DefaultSymbolGenerator()
        self.font_factory = ft.DefaultFontFactory()
        self.colorize = False
        self.mode = Mode.Image

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
        use_color = self.default
        if token in self._colors:
            use_color = self._colors[token]
        return (self._get_color(self._to_hex(use_color)),
                self.symbol_generator.next(use_color))

    def _new_entry(self, ch, style):
        """new entry to process."""
        return (self.font_factory.get(ch), style)

    def _output(self, out_file, value, mode):
        """Perform output step."""
        # TODO: need to write to outfile...probably.
        if mode == self.mode:
            print(value)

    def format(self, tokensource, outfile):
        """Override to format."""
        entries = []
        current = []
        for ttype, value in tokensource:
            while ttype not in self._colors:
                if ttype.parent is not None:
                    ttype = ttype.parent
                else:
                    break
            styles = self._token_color(ttype)
            if value == "\n":
                entries.append(current)
                if len(current) == 0:
                    entries.append([self._new_entry(' ', styles)])
                current = []
            else:
                for ch in value:
                    current.append(self._new_entry(ch, styles))
        if len(current) > 0:
            entries.append(current)
        self._output(outfile, _HTML_STYLE, Mode.HTML)
        self._output(outfile, _TABLE, Mode.HTML)
        tr_idx = 1
        self._output(outfile, _TR.format(tr_idx), Mode.HTML)
        tr_idx += 1
        last = False
        max_width = 0
        legend = []
        total_height = 0
        griding = []
        for entry in entries:
            cur_width = 0
            for height in self.font_factory.height():
                grid = []
                for cur, style in entry:
                    coloring = style[0]
                    symb = style[1]
                    for cell in cur.cells(height):
                        if height == 0:
                            cur_width += 1
                        classes = []
                        is_stitch = False
                        styles = []
                        for stitch in cell:
                            if isinstance(stitch, ft.Stitch):
                                if stitch == ft.Stitch.CrossStitch:
                                    is_stitch = True
                                    if self.colorize:
                                        styles.append(_COLOR.format(coloring))
                            if isinstance(stitch, ft.BackStitch):
                                if stitch == ft.BackStitch.TopLeftBottomRight:
                                    classes.append(_TLBR_BS)
                                if stitch == ft.BackStitch.BottomLeftTopRight:
                                    classes.append(_BLTR_BS)
                                if stitch == ft.BackStitch.Top:
                                    styles.append(_BORDER.format("top"))
                                if stitch == ft.BackStitch.Left:
                                    styles.append(_BORDER.format("left"))
                                if stitch == ft.BackStitch.Right:
                                    styles.append(_BORDER.format("right"))
                                if stitch == ft.BackStitch.Bottom:
                                    styles.append(_BORDER.format("bottom"))
                        self._output(outfile,
                                     _TD.format(" ".join(classes),
                                                ";".join(styles)), Mode.HTML)
#                        if len(classes) > 0 or is_stitch:
                        grid.append((is_stitch, classes, coloring, symb))
                        if is_stitch:
                            legend.append(style)
                            self._output(outfile, symb, Mode.HTML)
                        self._output(outfile, _TD_END, Mode.HTML)
                        last = False
                if not last:
                    self._output(outfile, _TR_END, Mode.HTML)
                    self._output(outfile, _TR.format(tr_idx), Mode.HTML)
                    tr_idx += 1
                    last = True
                    total_height += 1
                    griding.append(grid)
            if cur_width > max_width:
                max_width = cur_width
        mid = int(floor(max_width / 2))
        im = Image.new('RGB', (max_width * 10, total_height * 10), (0, 0, 0))
        dr = ImageDraw.Draw(im)
        for y in range(len(griding)):
            for x in range(len(griding[y])):
                print((0+x*10, 0+y*10))
                print(griding[y][x])
                dr.rectangle([(0+x*10,0+y*10),(10+x*10,10+y*10)], fill=griding[y][x][2])
                if griding[y][x][0]:
                    dr.text((0+x*10,0+y*10), griding[y][x][3], (0, 0, 0))
        im.save('test.png')

        for x in range(max_width):
            val = 'X'
            if mid != x:
                val = str(x + 1)
            self._output(outfile, _TD.format("", "") + val + _TD_END, Mode.HTML)
        self._output(outfile, _TR_END, Mode.HTML)
        self._output(outfile, _TABLE_END, Mode.HTML)
        for l in sorted(set(legend)):
            self._output(outfile, _LEGEND.format(l[1], l[0]), Mode.HTML)
