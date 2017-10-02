#!/usr/env/python
"""pyxstitch operating configuration settings."""
import os
from pathlib import Path

_PAGE = "page_"
_NO_IDX = "no_index"
_BOOLS = [_PAGE + _NO_IDX]
_LEGEND_ATTR = "legend_"
_LGD_HOFF = _LEGEND_ATTR + "hoff"
_LGD_WOFF = _LEGEND_ATTR + "woff"
_OFFSET = [_LGD_HOFF, _LGD_WOFF]
_DELIMIT = "="


class Config(object):
    """Configuration definition."""

    def __init__(self, inputs):
        """Init the instance."""
        self.page_height = 600
        self.page_width = 1000
        self.page_pad = 50
        self.page_no_index = 0
        self.page_legend = 0
        self.legend_hoff = 0
        self.legend_woff = 0
        self.page_font_size = 0
        if inputs is None or len(inputs) == 0:
            self._parse_config(inputs)
        else:
            self._parse(inputs)

    def save(self):
        """Save to disk."""
        return [self.page_height,
                self.page_width,
                self.page_pad,
                self.page_no_index,
                self.page_legend,
                self.page_font_size]

    def dump(self):
        """dump extraneous settings passed in."""
        return [self.legend_hoff, self.legend_woff]

    @staticmethod
    def _create_page_input(key, value):
        """create an input."""
        return "{}{}{}{}".format(_PAGE, key, _DELIMIT, value)

    @staticmethod
    def load(values):
        """load config from saved type."""
        inputs = []
        if len(values) == 6:
            inputs.append(Config._create_page_input("height", values[0]))
            inputs.append(Config._create_page_input("width", values[1]))
            inputs.append(Config._create_page_input("pad", values[2]))
            inputs.append(Config._create_page_input(_NO_IDX, values[3]))
            inputs.append(Config._create_page_input("legend", values[4]))
            inputs.append(Config._create_page_input("font_size", values[5]))
        return Config(inputs)

    def _parse_config(self, inputs):
        """Parse and load the config file."""
        home = str(Path.home())
        conf = os.path.join(home, ".pyxstitch.config")
        if os.path.exists(conf):
            config_input = []
            with open(conf, 'r') as f:
                for l in f:
                    line = l.strip()
                    if line.startswith("#") or len(line) == 0:
                        continue
                    config_input.append(line)
            if len(config_input) > 0:
                self._parse(config_input)

    def _parse(self, inputs):
        """parse inputs."""
        for item in inputs:
            parts = item.split(_DELIMIT)
            if len(parts) != 2:
                print('unable to parse config input: {}'.format(item))
                continue
            key = parts[0]
            val = parts[1]
            if key.startswith(_PAGE) or key.startswith(_LEGEND_ATTR):
                if key in dir(self):
                    try:
                        int_val = int(val)
                        if int_val > 0 or (int_val >= 0 and key in _BOOLS) or \
                           (int_val <= 0 and key in _OFFSET):
                            setattr(self, key, int_val)
                            continue
                    except:
                        pass
            print("invalid attribute {}".format(item))
