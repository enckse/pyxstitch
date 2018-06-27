#!/usr/bin/python
"""Tests character object definitions."""
import unittest
import pyxstitch.utils as utils


class TestUtils(unittest.TestCase):
    """Test utils object."""

    def test_supported(self):
        """Test utils supported check."""
        v = utils._supported((3, 3))
        self.assertTrue(v is None)
        v = utils._supported((2, 7))
        self.assertTrue(v is None)
        valid = (3, 4)
        v = utils._supported(valid)
        self.assertEqual(valid, v)

    def test_home(self):
        """Test getting home."""
        v = utils.home()
        self.assertTrue(len(v) != 0)
