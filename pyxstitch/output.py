#!/usr/env/python
"""Output formats."""
from PIL import Image, ImageDraw
from io import StringIO
import json

RAW_FORMAT = "pyxstitch"


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

    def __init__(self):
        """Init the output objects."""
        self._im = None
        self._dr = None
        self._is_multi = False

    def init(self, style, dims, color, multipage):
        """Init the image."""
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

    def save(self, file_name):
        """Save the output image."""
        self._im.save(file_name)

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
