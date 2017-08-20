#!/usr/bin/python
"""Test default font factory settings."""
import unittest
import pyxstitch.font as ft
import string
import pyxstitch.font_five_by_nine as fbn
import pyxstitch.font_three_by_seven as tbs


class TestDefaultFont(unittest.TestCase):
    """Test character object."""

    def test_ascii(self):
        """Validate all ascii printable."""
        f = ft.Font()
        factory = f.new_font_object()
        self._check_font(factory)
        for fonts in f.get_names():
            self._check_font(f.new_font_by_name(fonts))

    def _check_font(self, factory):
        """Check font factory."""
        for ch in string.printable:
            if ch in ['\t', '\r', '\v', '\f', '\n']:
                continue
            factory.get(ch)

    def test_height(self):
        """Get height."""
        factory = ft.Font().new_font_object()
        self.assertEqual(10, max(factory.height()))

    def test_width(self):
        """Get width."""
        factory = ft.Font().new_font_object()
        self.assertEqual(4, max(factory.width()))

    def test_get_error(self):
        """Get non-character."""
        factory = ft.Font().new_font_object()
        with self.assertRaises(ft.FontException) as cm:
            factory.get(None)
        self.assertEqual("No font entry for character None", str(cm.exception))

    def test_preprocess(self):
        """Test preprocess."""
        factory = ft.Font().new_font_object()
        self.assertEqual("    ", factory.process('\t'))
        self.assertEqual("\n", factory.process('\r'))
        self.assertEqual("\n", factory.process('\v'))
        self.assertEqual("\n", factory.process('\f'))

    def test_by_type(self):
        """Passing a tyep into construction."""
        f = ft.Font()
        f.new_font_object()
        f.new_font_object(fbn.FiveByNine)
        with self.assertRaises(ft.FontException) as cm:
            f.new_font_object(str)
        self.assertEqual("unknown font type: <class 'str'>", str(cm.exception))
        with self.assertRaises(ft.FontException) as cm:
            f.new_font_by_name("test")
        self.assertEqual("unknown font name: test", str(cm.exception))
