#!/usr/env/python
"""Output formats."""
from PIL import Image, ImageDraw
from io import StringIO
import json


class FormatError(Exception):
    """Format errors."""


class Format(object):
    """Base format output."""

    def init(self, style, dims, color):
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

    def init(self, style, dims, color):
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

    def __init__(self, dump=False):
        """Init the instance."""
        self._io = StringIO()
        self._dump = dump
        self._version = "0.1"

    def init(self, style, dims, color):
        """Init the instance."""
        self._write("init", [style, dims, color])

    def _write(self, obj_type, values):
        """Write data."""
        obj = {}
        obj['type'] = obj_type
        obj['data'] = values
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
        self._write("save", [file_name])
        contents = self._io.getvalue()
        if self._dump:
            return contents
        with open(file_name, 'w') as f:
            f.write(contents)

    def meta(self, char_meta, style, char):
        """Character metadata."""
        self._write("meta", [char_meta, style, char, self._version])
