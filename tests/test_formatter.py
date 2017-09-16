#!/usr/bin/python
"""Test formatter."""
import unittest
import pyxstitch.formatter as fmt


class TestFormatter(unittest.TestCase):
    """Test formatter."""

    def test_create(self):
        f = fmt.new_formatter("monokai", "test", "off")
        self.assertEqual("test", f.file_name)
        self.assertEqual("off", f.is_multipage)
        self.assertFalse(f.dark)
        self.assertFalse(f.colorize)
        self.assertFalse(f.is_raw)
        self.assertFalse(f.is_bw)
        self.assertEqual(None, f.config)
        self.assertEqual("FiveByNine", type(f.font_factory).__name__)
        f = fmt.new_formatter("monokai",
                               "test",
                               "off",
                               dark=True,
                               colorize=True,
                               is_raw=True,
                               is_bw=True)
        self.assertEqual("test", f.file_name)
        self.assertEqual("off", f.is_multipage)
        self.assertTrue(f.dark)
        self.assertTrue(f.colorize)
        self.assertTrue(f.is_raw)
        self.assertTrue(f.is_bw)
        self.assertEqual(None, f.config)
        self.assertEqual("FiveByNine", type(f.font_factory).__name__)

    def test_map(self):
        pass

    def test_config(self):
        pass

    def test_font(self):
        pass
