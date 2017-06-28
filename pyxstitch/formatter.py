from pygments.formatter import Formatter
import webcolors as wc
import pyxstitch.font as font
import string

class CrossStitchFormatter(Formatter):
    """Formats output as a cross stitch pattern."""

    _HEX = '0123456789abcdefABCDEF'

    def __init__(self, **options):
        """Initialize the instance."""
        Formatter.__init__(self, **options)
        self._hex = {x: int(x, 16) for x in
                     (y + z for y in self._HEX for z in self._HEX)}
        self.font_factory = font.FontFactory()
        self.colors = {}
        # TODO: Styling selection should impact default color (or is a noop?)
        self.default = "000000"
        self.keying = sorted(string.printable)
        idx = 0
        for token, style in self.style:
            if style['color']:
                self.colors[token] = (style['color'], self.keying[idx])
                idx += 1

    def _closest(self, rgb):
        """ We need to find a color approximation."""
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
        if token in self.colors:
            use_color = self.colors[token]
        return (self._get_color(self._to_hex(use_color[0])), "#" + use_color[0], use_color[1])

    def format(self, tokensource, outfile):
        """Override to format."""
        # TODO: need to write to outfile...probably.
        print("""
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

  .bltr-bs:after{
    content:"";
    position:absolute;
    border-top:1px solid black;
    width:13px;
    transform: rotate(135deg);
    transform-origin: 3px -1px;
  }

  .tlbr-bs:after {
    content:"";
    position:absolute;
    border-top:1px solid black;
    width:13px;
    transform: rotate(45deg);
    transform-origin: 5px -7px;
  }
  </style>""")
        print("<table cellspacing='1'>")
        print('<tr>')
        entries = []
        current = []
        for ttype, value in tokensource:
            while ttype not in self.colors:
                if ttype.parent is not None:
                    ttype = ttype.parent
                else:
                    break
            styles = self._token_color(ttype)
            if value == "\n":
                entries.append(current)
                current = []
            else:
                for ch in value:
                    current.append((self.font_factory.get(ch), styles))
        if len(current) > 0:
            entries.append(current)

        output = []
        for entry in entries:
            for height in range(self.font_factory._height):
                for cur, style in entry:
                    for cell in cur.cells(height):
                        classes = []
                        is_stitch = False
                        styles = ["background-color: #e6e6e6"]
                        for stitch in cell:
                            if isinstance(stitch, font.Stitch):
                                if stitch == font.Stitch.CrossStitch:
                                    is_stitch = True
                            if isinstance(stitch, font.BackStitch):
                                if stitch == font.BackStitch.TopLeftBottomRight:
                                    classes.append("tlbr-bs")
                                if stitch == font.BackStitch.BottomLeftTopRight:
                                    classes.append("bltr-bs")
                                if stitch == font.BackStitch.Top:
                                    styles.append("border-top: 1px solid black")
                                if stitch == font.BackStitch.Left:
                                    styles.append("border-left: 1px solid black")
                                if stitch == font.BackStitch.Right:
                                    styles.append("border-right: 1px solid black")
                                if stitch == font.BackStitch.Bottom:
                                    styles.append("border-bottom: 1px solid black")
                        output.append('<td class="{}" style="{}">'.format(" ".join(classes), ";".join(styles)))
                        if is_stitch:
                            output.append(style[2])
                        output.append('</td>')
                output.append('</tr>')
                output.append('<tr>')
        last = None
        for out in output:
            if last is not None:
                if last == "<tr>" and out == "</tr>" or out == "<tr>":
                    continue
            print(out)
            last = out
        print('</tr>')
        print("</table>")
