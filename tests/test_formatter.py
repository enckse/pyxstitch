#!/usr/bin/python3
"""Test formatter."""
import unittest
import pyxstitch.formatter as fmt


class TestFormatter(unittest.TestCase):
    """Test formatter."""

    def test_create(self):
        """Basic creation."""
        f = fmt.new_formatter("monokai", "test", "off")
        self.assertEqual("test", f.file_name)
        self.assertEqual("off", f.is_multipage)
        self.assertFalse(f.dark)
        self.assertFalse(f.colorize)
        self.assertFalse(f.is_raw)
        self.assertFalse(f.is_bw)
        self.assertEqual(None, f.config)
        self.assertEqual("FiveByNineMono", type(f.font_factory).__name__)
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
        self.assertEqual("FiveByNineMono", type(f.font_factory).__name__)
        self.assertEqual("DefaultSymbolGenerator",
                         f.symbol_generator.__class__.__name__)

    def test_map(self):
        """Floss mapping."""
        with self.assertRaises(fmt.FormatterException) as cm:
            fmt.new_formatter("monokai",
                              "test",
                              "off",
                              map_colors=["abc=xyz"])
        self.assertEqual("unable to map: abc=xyz", str(cm.exception))

    def test_symbols(self):
        """Test symbol setting."""
        f = fmt.new_formatter("monokai", "test", "off", symbols="abc")
        self.assertEqual("InputStringGenerator",
                         f.symbol_generator.__class__.__name__)

    def test_config(self):
        """Config settings."""
        f = fmt.new_formatter("monokai",
                              "test",
                              "off",
                              config=["page_legend=1"])
        self.assertFalse(f.config is None)

    def test_font(self):
        """Font selection."""
        f = fmt.new_formatter("monokai",
                              "test",
                              "off",
                              font_name="monospace-ascii-2x5")
        self.assertEqual("TwoByFiveMono", type(f.font_factory).__name__)
