#!/usr/bin/python3
"""Formatter layout tests."""
import unittest
import pyxstitch.formatter_layout as fl


class Mock(object):
    """Mock dmc input floss object."""

    name = "xyz"
    rgb = "aaaaaa"
    symbol = "1"
    floss_number = "1234"
    dmc = None

    def _init(self):
        """Init mock dmc object."""
        self.dmc = Mock()


class TestFormatterLayout(unittest.TestCase):
    """Test formatter layout objects."""

    def test_style_save(self):
        """Test style saving."""
        style = fl.Style(Mock(), "X", "abc")
        saved = style.save()
        self.assertEqual(3, len(saved))
        self.assertEqual("xyz", saved[0])
        self.assertEqual("X", saved[1])
        self.assertEqual("abc", saved[2])

    def _check_legend(self, val, expect):
        """Validate a legend entry."""
        self.assertEqual(62, len(val))
        self.assertEqual(expect, val.strip())

    def test_build_legend(self):
        """Test building a legend."""
        lg = fl.Legend()
        mck = Mock()
        mck._init()
        lg.add_raw_stitch(mck)
        lg.add(mck)
        legend = lg.build()
        self.assertEqual(3, len(legend))
        self._check_legend(legend[0],
                           "dmc  symbol  edges  floss")
        self._check_legend(legend[1],
                           "---     ---    ---    ---")
        self._check_legend(legend[2],
                           "xyz (aaaaaa)       1      1   1234")
