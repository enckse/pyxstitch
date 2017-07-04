#!/usr/bin/python
"""Floss testing."""
import unittest
import pyxstitch.floss as floss


class TestFloss(unittest.TestCase):
    """Test floss."""

    def test_lookup_close(self):
        """Floss lookup."""
        fl = floss.Floss()
        look = fl.lookup("______", (169, 226, 216))
        self.assertEqual("Sea Green Light", look.name)
        self.assertEqual("964", look.floss_number)
        self.assertEqual("a9e2d8", look.rgb)

    def test_lookup_code(self):
        """Floss lookup."""
        fl = floss.Floss()
        look = fl.lookup("A9E2D8", None)
        self.assertEqual("964", look.floss_number)
        self.assertEqual("Sea Green Light", look.name)
        self.assertEqual("a9e2d8", look.rgb)
