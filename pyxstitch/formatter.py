#!/usr/bin/python
"""
A formatter implementation for pygments.

Takes a text stream and converts to a cross stitch output (HTML).
"""

from pygments.formatter import Formatter
import webcolors as wc
import pyxstitch.font as ft
import string

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
_HTML_STYLE = """
<style>
table {
    text-align: center;
}
tr {
    padding: 0px 0px 0px 0px;
}
td {
    width: 10px;
    height: 10px;
    font-size: 8px;
}

STYLE
</style>""".replace("STYLE", _BLTR_BS_CSS + _TLBR_BS_CSS)

_BORDER = "border-{}: 1px solid black"
_BACKGROUND = "background-color: #{}"

_TR = "<tr>"
_TABLE = "<table cellspacing='1'>"
_TABLE_END = "</table>"
_IMG = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUAQMAAAC3R49OAAAABlBMVEXv7+/v7+8tAJavAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAADElEQVQImWNgoC4AAABQAAGmLdqcAAAAAElFTkSuQmCC'
_TD = '<td background="IMG" class="{}" style="{}">'.replace("IMG", _IMG)
_TD_END = "</td>"
_TR_END = "</tr>"


class CrossStitchFormatter(Formatter):
    """Formats output as a cross stitch pattern."""

    _HEX = '0123456789abcdefABCDEF'

    def __init__(self, **options):
        """Initialize the instance."""
        Formatter.__init__(self, **options)
        self._hex = {x: int(x, 16) for x in
                     (y + z for y in self._HEX for z in self._HEX)}
        self._colors = {}

        # TODO: these components should be set or defaulted
        self.default = "000000"
        self.background = "e6e6e6"
        self.font_factory = ft.DefaultFontFactory()
        self.keying = sorted(string.printable)

        idx = 0
        for token, style in self.style:
            if style['color']:
                self._colors[token] = (style['color'], self.keying[idx])
                idx += 1

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
        return (self._get_color(self._to_hex(use_color[0])),
                "#" + use_color[0],
                use_color[1])

    def _new_entry(self, ch, style):
        return (self.font_factory.get(ch), style)

    def _output(self, out_file, value):
        """Perform output step."""
        # TODO: need to write to outfile...probably.
        print(value)

    def format(self, tokensource, outfile):
        """Override to format."""
        self._output(outfile, _HTML_STYLE)
        self._output(outfile, _TABLE)
        self._output(outfile, _TR)
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

        last = False
        for entry in entries:
            for height in self.font_factory.height():
                for cur, style in entry:
                    for cell in cur.cells(height):
                        classes = []
                        is_stitch = False
                        styles = [_BACKGROUND.format(self.background)]
                        for stitch in cell:
                            if isinstance(stitch, ft.Stitch):
                                if stitch == ft.Stitch.CrossStitch:
                                    is_stitch = True
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
                                                ";".join(styles)))
                        if is_stitch:
                            self._output(outfile, style[2])
                        self._output(outfile, _TD_END)
                        last = False
                if not last:
                    self._output(outfile, _TR_END)
                    self._output(outfile, _TR)
                    last = True
        self._output(outfile, _TR_END)
        self._output(outfile, _TABLE_END)
