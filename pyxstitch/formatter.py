from pygments.formatter import Formatter
import webcolors as wc
import pyxstitch.font as font


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
        for token, style in self.style:
            if style['color']:
                self.colors[token] = style['color']

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
        return (self._get_color(self._to_hex(use_color)), "#" + use_color)

    def format(self, tokensource, outfile):
        """Override to format."""
        # TODO: need to write to outfile...probably.
        print("""
  <style> 
  table.grid {
    border-collapse:collapse;
    font-size: 20px;
    font-weight: bold;
  }
  .grid td {
    border:solid 0.25px #888;
  }
  .grid  {
    overflow: hidden;
    width: 6px;
    height: 6px;
    text-align: center;
  }
  .bs-toplbotr {
    background-color: #000;
    transform: rotate(45deg);
  }
  .bs-botltopr {
  }
  </style>""")
        print("<table class='grid'>")
        print('<tr>')
        for ttype, value in tokensource:
            while ttype not in self.colors:
                if ttype.parent is not None:
                    ttype = ttype.parent
                else:
                    break
            color_name, rgb = self._token_color(ttype)
            if value == "\n":
                print('</tr>')
                print('<!--newline-->')
                print('<tr>')
            else:
                for height in range(font.SIZE):
                    for ch in value:
                        letter = self.font_factory.get(ch)
                        for cell in letter.cells(height):
                            color = "background-color: {}".format(rgb)
                            classes = []
                            #for stitch in cell:
                                #if stitch == font.BackStitch.TopLeftBottomRight:
                                  #  classes.append("bs-toplbotr")
                            print('<td class="{}" style="{}">'.format(" ".join(classes), color))
                            print('[]')
                            print('</td>')
                    print('</tr>')
                    print('<tr>')
#                    if ch.isspace():
#                        print('<!--space-->')
#                    else:
#
#                        print(ch)
                    #print('</td>')
        print('</tr>')
        print("</table>")
