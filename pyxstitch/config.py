#!/usr/env/python
"""pyxstitch operating configuration settings."""


class Config(object):
    """Configuration definition."""

    def __init__(self, inputs):
        """Init the instance."""
        self.page_height = 600
        self.page_width = 1000
        self.page_pad = 50
        self._parse(inputs)

    def save(self):
        """Save to disk."""
        return [self.page_height, self.page_width, self.page_pad]

    @staticmethod
    def _create_input(key, value):
        """create an input."""
        return "{}={}".format(key, value)

    @staticmethod
    def load(values):
        """load config from saved type."""
        inputs = []
        if len(values) == 3:
            inputs.append(Config._create_input("page_height", values[0]))
            inputs.append(Config._create_input("page_width", values[1]))
            inputs.append(Config._create_input("page_pad", values[2]))
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
            if key.startswith("page_"):
                if key in dir(self):
                    try:
                        int_val = int(val)
                        if int_val > 0:
                            setattr(self, key, int_val)
                            continue
                    except:
                        pass
            print("invalid attribute {}".format(item))
