#!/usr/env/python
"""Output formats."""
from PIL import Image, ImageDraw
from io import StringIO
import json
import os

RAW_FORMAT = "pyxstitch"

MULTI_PAGE_ON = "on"
MULTI_PAGE_OFF = "off"
MULTI_PAGE_AUTO = "auto"


class FormatError(Exception):
    """Format errors."""


class Format(object):
    """Base format output."""

    def init(self, style, dims, color, multipage):
        """init the instance."""
        raise FormatError("not implemented.")

    def rect(self, dims, outline=None):
        """Create  rectangle (square)."""
        raise FormatError("not implemented.")

    def text(self, dims, symbol, color):
        """Draw text."""
        raise FormatError("not implemented.")

    def line(self, dims, fill=None):
        """Draw a line."""
        raise FormatError("not implemented.")

    def save(self, file_name):
        """Save the output."""
        raise FormatError("not implemented.")

    def meta(self, char_meta, style, char):
        """Meta data."""
        raise FormatError("not implemented")


class PILFormat(Format):
    """PIL/image format."""

    _PAGE_HEIGHT = 970
    _PAGE_WIDTH = 720
    _PADDING = 25

    def __init__(self):
        """Init the output objects."""
        self._im = None
        self._dr = None
        self._img_dims = None
        self._is_multi = False
        self._img_color = None

    def init(self, style, dims, color, multipage):
        """Init the image."""
        self._img_dims = dims
        self._img_color = color
        if multipage == MULTI_PAGE_ON:
            self._is_multi = True
        elif multipage == MULTI_PAGE_AUTO:
            self._is_multi = self._img_dims[0] > self._PAGE_WIDTH or \
                             self._img_dims[1] > self._PAGE_HEIGHT
        self._im = Image.new(style, dims, color)
        self._dr = ImageDraw.Draw(self._im)

    def rect(self, dims, outline=None):
        """Draw a rectangle."""
        self._dr.rectangle(dims, outline=outline)

    def text(self, dims, symbol, color):
        """Draw text."""
        self._dr.text(dims, symbol, color)

    def line(self, dims, fill=None):
        """Draw a line."""
        self._dr.line(dims, fill=fill)

    def _save(self, im, file_name):
        """Save an image."""
        print("saving {}".format(file_name))
        im.save(file_name)

    def save(self, file_name):
        """Save the output image."""
        if self._is_multi:
            page = 1
            width = self._img_dims[0]
            height = self._img_dims[1]
            use_height = min(height, self._PAGE_HEIGHT)
            use_width = min(width, self._PAGE_WIDTH)
            for h in range(0, height, use_height):
                for w in range(0, width, use_width):
                    w_end = w + use_width
                    h_end = h + use_height
                    if w_end > width:
                        w_end = width
                    if h_end > height:
                        h_end = height
                    box = (w, h, w_end, h_end)
                    cropped = self._im.crop(box)
                    file_parts = os.path.splitext(file_name)
                    paged = "{}_{}{}".format(file_parts[0],
                                             str(page).rjust(3, '0'),
                                             file_parts[1])
                    im = Image.new('RGB',
                                   (self._PAGE_WIDTH + self._PADDING * 2,
                                    self._PAGE_HEIGHT + self._PADDING * 2),
                                   self._img_color)
                    im.paste(cropped, (self._PADDING, self._PADDING))
                    self._save(im, paged)
                    page += 1
        else:
            self._save(self._im, file_name)

    def meta(self, char_meta, style, char):
        """Character metadata and style."""
        pass


class TextFormat(Format):
    """Raw texst output."""

    _TYPE = "type"
    _DATA = "data"
    _INIT = "init"
    _SAVE = "save"

    def __init__(self, dump=False):
        """Init the instance."""
        self._io = StringIO()
        self._dump = dump
        self._version = "0.1"

    def _unpack(self, args):
        """Unpack lists back to tuples (due to json)."""
        unpacked = []
        for arg in args:
            if isinstance(arg, list):
                unpacked.append(tuple(self._unpack(arg)))
            else:
                unpacked.append(arg)
        return unpacked

    def _log_replay(self, level, fmt, args):
        """log replay messages."""
        print("{} -> {}".format(level, fmt.format(*args)))

    def replay(self, content, out_file_name):
        """Replay a file into another format."""
        line_idx = 1
        pil = PILFormat()
        for line in content.split("\n"):
            if len(line.strip()) == 0:
                continue
            try:
                obj = json.loads(line)
                cmd = obj[self._TYPE]
                datum = obj[self._DATA]
                if cmd == self._SAVE:
                    pil.save(out_file_name)
                    continue
                if cmd == self._INIT:
                    vers = datum[0]
                    if vers != self._version:
                        self._log_replay("warning",
                                         "Version: file {}, current {}",
                                         [vers, self._version])
                    datum = datum[1:]
                passing = self._unpack(datum)
                attr = getattr(pil, cmd)
                attr(*passing)
            except Exception as e:
                self._log_replay("error",
                                 "line number {}: {}",
                                 [line_idx, e])
                break
            line_idx += 1

    def init(self, style, dims, color, multipage):
        """Init the instance."""
        self._write(self._INIT, [self._version, style, dims, color, multipage])

    def _write(self, obj_type, values):
        """Write data."""
        obj = {}
        obj[self._TYPE] = obj_type
        obj[self._DATA] = values
        self._io.write(json.dumps(obj) + "\n")

    def rect(self, dims, outline=None):
        """Write rectangle information."""
        self._write("rect", [dims, outline])

    def text(self, dims, symbol, color):
        """Write text."""
        self._write("text", [dims, symbol, color])

    def line(self, dims, fill=None):
        """Write a line."""
        self._write('line', [dims, fill])

    def save(self, file_name):
        """Save outputs."""
        self._write(self._SAVE, [file_name])
        contents = self._io.getvalue()
        if self._dump:
            return contents
        with open(file_name, 'w') as f:
            f.write(contents)

    def meta(self, char_meta, style, char):
        """Character metadata."""
        self._write("meta", [char_meta, style, char])
