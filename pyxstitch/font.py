#!/usr/bin/python
"""Defines the default font functionality to get char -> stitch mappings."""
from pyxstitch.character import Character, BackStitch, Stitch, BadCharException


class FontException(Exception):
    """Font exceptions."""


class FontFactory(object):
    """Character stitching font creator."""

    def height(self):
        """Get the height of the font."""
        raise FontException("not implemented.")

    def get(self, character):
        """Get a character definition."""
        raise FontException("not implemented.")


def preprocess(content,
               replace={'\t': '    ', '\r': '\n', '\f': '\n', '\v': '\n'}):
    """Preprocess text/content before lexing."""
    val = content
    if replace is not None:
        for replacing in replace:
            val = val.replace(replacing, replace[replacing])
    parts = val.split("\n")
    cols = max([len(x) for x in parts])
    return (val, len(parts), cols)


class BaseFontFactory(FontFactory):
    """Base font factory."""

    def __init__(self):
        """Initialize the factory."""
        hw = self._height_width()
        self._height = hw[0] + 2
        self._width = hw[1]
        self._top_off = 1
        self._bot_off = 1
        self.is_backstitched = False
        self._characters = self._initialize_characters()
        self.display_name = None

    def _height_width(self):
        raise FontException("does not declare font height/width")

    def height(self):
        """get the font factory range of height for characters."""
        return range(self._height)

    def width(self):
        """get the font width."""
        return range(self._width)

    def get(self, ch):
        """Lookup a character in the font."""
        if ch in self._characters:
            return self._characters[ch]
        raise FontException("No font entry for character {}".format(ch))

    def _set_flags(self, val_str, enums, add_to):
        """Check which enum flags are set - append them to a list."""
        val = int(val_str)
        for e in enums:
            if e & val:
                for item in self._translate(e):
                    add_to.append(item)

    def _translate(self, enum_item):
        """Translate stitching types."""
        if isinstance(enum_item, Stitch):
            if enum_item == Stitch.BottomRight:
                return [BackStitch.BottomRight, BackStitch.BottomLeftTopRight]
            elif enum_item == Stitch.BottomLeft:
                return [BackStitch.BottomLeft, BackStitch.TopLeftBottomRight]
            elif enum_item == Stitch.TopLeft:
                return [BackStitch.TopLeft, BackStitch.BottomLeftTopRight]
            elif enum_item == Stitch.TopRight:
                return [BackStitch.TopRight, BackStitch.TopLeftBottomRight]
        return [enum_item]

    def _parse(self, definition, ch):
        """Parse a character definition."""
        if definition is None:
            raise BadCharException("Invalid character definition")
        stripped = definition.strip()
        if len(stripped) == 0:
            raise BadCharException("Empty definition for character")
        parts = stripped.split("\n")
        has_height = len(parts)
        if has_height != self._height:
            if has_height != self._height - self._top_off - self._bot_off:
                raise BadCharException("Definition has an improper height")
            add_line = "|" + " | ".join(["" for x in range(self._width)]) + "|"
            for x in range(self._top_off):
                parts.insert(0, add_line)
            for x in range(self._bot_off):
                parts.append(add_line)
        height = 0
        for part in parts:
            defined = [x for x in part.split("|") if x != '']
            if len(defined) != self._width:
                raise BadCharException("Definition has an improper width")
            width = 0
            for entry in defined:
                if len(entry.strip()) > 0:
                    section = entry.split(".")
                    adding = []
                    self._set_flags(section[0], Stitch, adding)
                    self._set_flags(section[1], BackStitch, adding)
                    ch[height][width].stitches = adding
                width += 1
            height += 1
        return ch

    def _drop_lines(self, write_to, ch, chars, lines):
        """Drop lines from an existing character."""
        raw = chars[ch].raw
        raw_lines = raw.split("\n")
        idx = 0
        conv = []
        for line in raw_lines:
            idx = idx + 1
            if idx in lines:
                continue
            conv.append(line)
        write_to[ch] = self._build_character("\n".join(conv))

    def _build_character(self, stitching):
        """Build a character into an object definition."""
        ch = Character(self._height, self._width)
        try:
            ch._pattern = self._parse(stitching, ch._pattern)
            ch.raw = stitching
        except BadCharException as e:
            raise BadCharException("{} -> {}".format(str(e), stitching))
        return ch

    def _initialize_characters(self):
        """Initialize char set."""
        raise FontException("characeter set not defined")


def get_all_fonts():
    """Get all fonts."""
    return Font().get_names()


class Font(object):
    """Create font instance."""

    detect = "detect"

    def __init__(self):
        """Init the font creation object."""
        from pyxstitch.fonts.five_by_nine import FiveByNine
        from pyxstitch.fonts.three_by_five import ThreeByFive
        from pyxstitch.fonts.three_by_seven import ThreeBySeven
        from pyxstitch.fonts.two_by_five import TwoByFive
        self._supported_types = [FiveByNine,
                                 ThreeBySeven,
                                 TwoByFive,
                                 ThreeByFive]
        self._names = {}
        # tuple is (index, column threshold, row threshold)
        self._names["monospace-ascii-5x9"] = (0, 31, 21)
        self._names["monospace-ascii-3x7"] = (1, 46, 26)
        self._names["monospace-ascii-2x5"] = (2, None, None)
        self._names["monospace-ascii-3x5"] = (3, 46, 31)

    def get_names(self):
        """Get font names."""
        return self._names.keys()

    def new_font_by_name(self, font_name, rows=None, columns=None):
        """Get a font by name."""
        use_name = font_name
        if font_name == self.detect:
            dflt = None
            if rows is not None and columns is not None:
                for detect in sorted(self._names.keys()):
                    vals = self._names[detect]
                    c = vals[1]
                    r = vals[2]
                    if c is None and r is None:
                        dflt = detect
                        continue
                    if rows < r and columns < c:
                        use_name = detect
                if use_name == font_name:
                    use_name = dflt
            else:
                raise FontException("requires dimensions (rows, cols)")
        if use_name in self._names:
            typed = self._supported_types[self._names[use_name][0]]
            inst = self.new_font_object(typed)
            inst.auto_name = use_name
            return inst
        else:
            raise FontException("unknown font name: {}".format(font_name))

    def new_font_object(self, font_type=None, columns=None):
        """Create a new font object."""
        use_type = None
        if font_type is None:
            use_type = self._supported_types[0]
        if font_type in self._supported_types:
            use_type = font_type
        if use_type is None:
            raise FontException("unknown font type: {}".format(font_type))
        return use_type()
