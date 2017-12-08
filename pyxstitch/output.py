#!/usr/env/python
"""Output formats."""
from PIL import Image, ImageDraw
from io import StringIO
import pyxstitch.config as cfg
import pyxstitch.version as vers
import pyxstitch.log as log
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

    def init(self, style, dims, color, multipage, config):
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

    def legend(self, pos, legend, symbols):
        """Legend output."""
        raise FormatError("not implemented")

    def extras(self, config_values):
        """Save extra information, not replayed."""
        raise FormatError("not implemented")


class PILFormat(Format):
    """PIL/image format."""

    _HTML = "<html><body>{}</body></html>"

    def __init__(self):
        """Init the output objects."""
        self._im = None
        self._dr = None
        self._img_dims = None
        self._is_multi = False
        self._img_color = None
        self._cfg = None
        self._legends = []
        self._legend_start = None

    def init(self, style, dims, color, multipage, config):
        """Init the image."""
        self._img_dims = dims
        self._img_color = color
        self._cfg = config
        if multipage == MULTI_PAGE_ON:
            self._is_multi = True
        elif multipage == MULTI_PAGE_AUTO:
            self._is_multi = self._img_dims[0] > self._cfg.page_width or \
                             self._img_dims[1] > self._cfg.page_height
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
        log.Log.write("saving {}".format(file_name))
        im.save(file_name, quality=100)

    def extras(self, config_values):
        """Ignore extras on PIL."""
        pass

    def _calculate_width(self, offset):
        """Width calculation."""
        return self._cfg.page_width + offset * 2

    def _new_image(self, use_offset):
        """New output image."""
        return Image.new('RGB',
                         (self._calculate_width(use_offset),
                          self._cfg.page_height + use_offset * 2),
                         self._img_color)

    def _new_page(self, file_parts, page, report_out):
        """Create a new page name for file output."""
        paged = "{}_{}{}".format(file_parts[0],
                                 str(page).rjust(3, '0'),
                                 file_parts[1])
        report_out.append(os.path.basename(paged))
        return paged

    def save(self, file_name):
        """Save the output image."""
        if self._is_multi:
            page = 1
            width = self._img_dims[0]
            height = self._img_dims[1]
            use_height = min(height, self._cfg.page_height)
            use_width = min(width, self._cfg.page_width)
            use_offset = self._cfg.page_pad
            file_name_outputs = []

            file_parts = os.path.splitext(file_name)
            for h in range(0, height, use_height):
                if h > self._legend_start:
                    continue
                for w in range(0, width, use_width):
                    w_end = w + use_width
                    h_end = h + use_height
                    if w_end > width:
                        w_end = width
                    if h_end > height:
                        h_end = height
                    box = (w, h, w_end, h_end)
                    cropped = self._im.crop(box)
                    im = self._new_image(use_offset)
                    im.paste(cropped, (use_offset, use_offset))
                    extrema = im.convert("L").getextrema()
                    if extrema[0] == extrema[1]:
                        continue
                    paged = self._new_page(file_parts, page, file_name_outputs)
                    self._save(im, paged)
                    page += 1
            lgd_im = self._new_image(use_offset)
            lgd_dr = ImageDraw.Draw(lgd_im)
            use_lgd_pos = (use_offset, use_offset)
            self._legendize(lgd_im, lgd_dr, position=use_lgd_pos)
            self._save(lgd_im, self._new_page(file_parts,
                                              page,
                                              file_name_outputs))
            if self._cfg.page_no_index == 0:
                index_page = "{}-index.html".format(file_parts[0])
                log.Log.write("producing index page {}".format(index_page))
                with open(index_page, 'w') as f:
                    output_img = "".join(["<img src='{}' />".format(x)
                                         for x in file_name_outputs])
                    f.write(self._HTML.format(output_img))
        else:
            self._legendize(self._im, self._dr)
            self._save(self._im, file_name)

    def _legendize(self, image, draw, position=None):
        """Create a legend on a drawing."""
        for l in self._legends:
            if self._cfg.page_legend == 0:
                lgd = self._new_image(0)
                lgd_dr = ImageDraw.Draw(lgd)
                use_pos = position
                if use_pos is None:
                    pos = l[0]
                    use_pos = (int(pos[0]), int(pos[1]))
                lgd_dr.text((0, 0), l[1], l[2])
                width = self._calculate_width(0) + self._cfg.page_font_size
                percent = (width / float(lgd.size[0]))
                height = int((float(lgd.size[1]) * float(percent)))
                lgd = lgd.resize((width, height), Image.ANTIALIAS)
                image.paste(lgd, use_pos)
            else:
                log.Log.writeln()
                log.Log.write("legend")
                log.Log.write("======")
                log.Log.write(l[1])
                log.Log.writeln()

    def meta(self, char_meta, style, char):
        """Character metadata and style."""
        pass

    def legend(self, pos, legend, symbols):
        """Save legend information."""
        if self._legend_start is None or pos[1] < self._legend_start:
            self._legend_start = pos[1]
        self._legends.append((pos, legend, symbols))


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
        self._version = "0.5"

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
        log.Log.write("{} -> {}".format(level, fmt.format(*args)))

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
                    conf = cfg.Config.load(datum[len(datum) - 1])
                    datum = datum[1:len(datum) - 1]
                    datum.append(conf)
                passing = self._unpack(datum)
                attr = getattr(pil, cmd)
                attr(*passing)
            except Exception as e:
                self._log_replay("error",
                                 "line number {}: {}",
                                 [line_idx, e])
                break
            line_idx += 1

    def init(self, style, dims, color, multipage, config):
        """Init the instance."""
        self._write(self._INIT, [self._version,
                                 style,
                                 dims,
                                 color,
                                 multipage,
                                 config.save()])

    def _write(self, obj_type, values):
        """Write data."""
        obj = {}
        obj[self._TYPE] = obj_type
        obj[self._DATA] = values
        self._io.write(json.dumps(obj) + "\n")

    def legend(self, pos, legend, symbols):
        """Legend output."""
        self._write("legend", [pos, legend, symbols])

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

    def extras(self, config_values):
        """Store extra information."""
        self._write("extras", [[vers.__version__, config_values]])

    def meta(self, char_meta, style, char):
        """Character metadata."""
        self._write("meta", [char_meta, style, char])
