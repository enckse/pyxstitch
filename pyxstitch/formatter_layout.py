#!/usr/bin/python
"""Formatter layout settings."""


class Style(object):
    """Output/legend formatting."""

    def __init__(self, dmc, symbol, original_hex):
        """Init the instance."""
        self.dmc = dmc
        self.symbol = symbol
        self._raw_hex = original_hex

    def save(self):
        """Save to metadata format."""
        return [self.dmc.name, self.symbol, self._raw_hex]


class Legend(object):
    """Legend object."""

    def __init__(self):
        """Init the instance."""
        self._stitches = {}
        self._entries = []

    def add_raw_stitch(self, dmc):
        """Add raw stitch edge."""
        raw_color = dmc.name
        if raw_color not in self._stitches:
            self._stitches[raw_color] = 0
        self._stitches[raw_color] += 1

    def add(self, style):
        """New legend entry."""
        self._entries.append(style)

    def build(self):
        """Build output legend."""
        headers = []
        cols = ("dmc", "symbol", "edges", "floss")
        delim = []
        for col in cols:
            delim.append("---")
        headers.append(cols)
        headers.append(tuple(delim))
        output = []
        for item in self._entries:
            output.append(("{} ({})".format(item.dmc.name, item.dmc.rgb),
                           item.symbol,
                           self._stitches[item.dmc.name],
                           item.dmc.floss_number))
        return ["{:>40} {:>7} {:>6} {:>6}".format(x[0],
                                                  x[1],
                                                  x[2],
                                                  x[3])
                for x in headers + sorted(set(output))]
