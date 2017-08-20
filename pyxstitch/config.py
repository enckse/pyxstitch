#!/usr/env/python
"""pyxstitch operating configuration settings."""

_PAGE = "page_"
_NO_IDX = "no_index"
_BOOLS = [_PAGE + _NO_IDX]


class Config(object):
    """Configuration definition."""

    def __init__(self, inputs):
        """Init the instance."""
        self.page_height = 600
        self.page_width = 1000
        self.page_pad = 50
        self.page_no_index = 0
        self.page_legend = 0
        self._parse(inputs)

    def save(self):
        """Save to disk."""
        return [self.page_height,
                self.page_width,
                self.page_pad,
                self.page_no_index,
                self.page_legend]

    @staticmethod
    def _create_input(key, value):
        """create an input."""
        return "{}{}={}".format(_PAGE, key, value)

    @staticmethod
    def load(values):
        """load config from saved type."""
        inputs = []
        if len(values) == 5:
            inputs.append(Config._create_input("height", values[0]))
            inputs.append(Config._create_input("width", values[1]))
            inputs.append(Config._create_input("pad", values[2]))
            inputs.append(Config._create_input(_NO_IDX, values[3]))
            inputs.append(Config._create_input("legend", values[4]))
        return Config(inputs)

    def _parse(self, inputs):
        """parse inputs."""
        if inputs is None:
            return
        if len(inputs) == 0:
            return
        for item in inputs:
            parts = item.split("=")
            if len(parts) != 2:
                print('unable to parse config input: {}'.format(item))
                continue
            key = parts[0]
            val = parts[1]
            if key.startswith(_PAGE):
                if key in dir(self):
                    try:
                        int_val = int(val)
                        if int_val > 0 or (int_val >= 0 and key in _BOOLS):
                            setattr(self, key, int_val)
                            continue
                    except:
                        pass
            print("invalid attribute {}".format(item))
