#!/usr/bin/python
"""Test hex helpers."""
import unittest
import pyxstitch.hex as hu


class TestHex(unittest.TestCase):
    """Test hex object."""

    def test_to_hex(self):
        """Hex string to 3-part tuple."""
        val = hu.to_hex("001122")
        self.assertEqual(0, val[0])
        self.assertEqual(17, val[1])
        self.assertEqual(34, val[2])

    def test_to_string(self):
        """Test tuple to string."""
        self.assertEqual("001122", hu.to_rgb_string((00, 17, 34)))

    def test_is_rgb(self):
        """Test simple validation."""
        self.assertTrue(hu.is_rgb_string("0011Fa"))
        self.assertFalse(hu.is_rgb_string("0011Ga"))
        self.assertFalse(hu.is_rgb_string("0011a"))
        self.assertFalse(hu.is_rgb_string(None))
