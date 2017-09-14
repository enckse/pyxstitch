#!/usr/bin/python
"""Floss testing."""
import unittest
import pyxstitch.floss as floss


class TestFloss(unittest.TestCase):
    """Test floss."""

    def test_lookup(self):
        """Floss lookup."""
        fl = floss.Floss()
        look = fl.lookup((169, 226, 216))
        self.assertEqual("Sea Green Light", look.name)
        self.assertEqual("964", look.floss_number)
        self.assertEqual("a9e2d8", look.rgb)

    def test_map(self):
        """Test mapping."""
        fl = floss.Floss()
        self.assertEqual("Black", fl.lookup((000, 000, 000)).name)
        mapped = fl.map((000, 000, 000), "ffffff")
        self.assertTrue(mapped)
        self.assertEqual("Snow White", fl.lookup((000, 000, 000)).name)
        mapped = fl.map((000, 000, 000), "abcdef")
        self.assertFalse(mapped)
