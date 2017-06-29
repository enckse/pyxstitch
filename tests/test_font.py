#!/usr/bin/python
"""Test default font factory settings."""
import unittest
import pyxstitch.font as ft
import string


class TestDefaultFont(unittest.TestCase):
    """Test character object."""

    def test_ascii(self):
        """Validate all ascii printable."""
        factory = ft.DefaultFontFactory()
        for ch in string.printable:
            factory.get(ch)

    def test_height(self):
        """Get height."""
        factory = ft.DefaultFontFactory()
        self.assertEqual(10, max(factory.height()))

    def test_width(self):
        """Get width."""
        factory = ft.DefaultFontFactory()
        self.assertEqual(4, max(factory.width()))

    def test_get_error(self):
        """Get non-character."""
        factory = ft.DefaultFontFactory()
        with self.assertRaises(ft.FontException) as cm:
            factory.get(None)
        self.assertEqual("No font entry for character None", str(cm.exception))
