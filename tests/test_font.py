#!/usr/bin/python
"""Test default font factory settings."""
import unittest
import pyxstitch.font as ft
import string
import pyxstitch.fonts.five_by_nine as fbn
import pyxstitch.fonts.three_by_seven as tbs


class MockStrip(ft.BaseFontFactory):
    """Mock stripping font."""

    def _height_width(self):
        """Override height/width."""
        return (3, 4)

    def _display(self):
        """Mock display."""
        return "mock_strip"

    def _initialize_characters(self):
        """Char set."""
        self._can_strip = True
        objs = {}
        objs['A'] = self._build_character("""
|1.00|1.00|    |    |
|1.00|1.00|    |    |
|1.00|1.00|    |    |
""")
        objs['B'] = self._build_character("""
|1.00|    |1.00|    |
|1.00|    |1.00|    |
|1.00|    |1.00|    |
""")
        objs[' '] = self._build_character("""
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
""", char_strip=False)
        return objs


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

    def test_display(self):
        """Test display names."""
        f = ft.Font()
        factory = f.new_font_object()
        self._check_font(factory)
        for fonts in f.get_names():
            fnt = f.new_font_by_name(fonts)
            hw = fnt._height_width()
            disp_name = "monospace-ascii-{}x{}".format(hw[1], hw[0])
            self.assertEqual(disp_name, fnt.display_name)

    def test_detect(self):
        """Detection on dimensions."""
        f = ft.Font()
        with self.assertRaises(ft.FontException) as cm:
            f.new_font_by_name("detect")
        self.assertEqual("requires dimensions (rows, cols)", str(cm.exception))
        with self.assertRaises(ft.FontException) as cm:
            f.new_font_by_name("detect", rows=100)
        self.assertEqual("requires dimensions (rows, cols)", str(cm.exception))
        with self.assertRaises(ft.FontException) as cm:
            f.new_font_by_name("detect", columns=100)
        self.assertEqual("requires dimensions (rows, cols)", str(cm.exception))
        dt = f.new_font_by_name("detect", rows=32, columns=30)
        self.assertEqual("TwoByFive", str(type(dt).__name__))
        dt = f.new_font_by_name("detect", rows=25, columns=45)
        self.assertEqual("ThreeBySeven", str(type(dt).__name__))
        dt = f.new_font_by_name("detect", rows=30, columns=25)
        self.assertEqual("ThreeByFive", str(type(dt).__name__))
        dt = f.new_font_by_name("detect", rows=9, columns=24)
        self.assertEqual("FiveByNine", str(type(dt).__name__))

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
        self.assertEqual("    ", ft.preprocess('\t')[0])
        self.assertEqual("\n", ft.preprocess('\r')[0])
        self.assertEqual("\n", ft.preprocess('\v')[0])
        self.assertEqual("\n", ft.preprocess('\f')[0])
        preproc = ft.preprocess("""test
        kdlaj; oieja ofij;ajfoiajoij109j
lkjealk; jaaaa
kd""")
        self.assertEqual(4, preproc[1])
        self.assertEqual(40, preproc[2])

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

    def test_strip(self):
        """Test stripping blank spaces from fonts."""
        f = MockStrip()
        a = f.get('A')
        self.assertEqual(2, a._width)
        self.assertEqual(5, a._height)
        a = f.get('B')
        self.assertEqual(3, a._width)
        self.assertEqual(5, a._height)
        a = f.get(' ')
        self.assertEqual(4, a._width)
        self.assertEqual(5, a._height)
