#!/usr/bin/python
"""Tests character object definitions."""
import unittest
import pyxstitch.character as ch


class TestCharacter(unittest.TestCase):
    """Test character object."""

    def test_cells(self):
        """Cell data retrieval."""
        char = ch.Character(5, 3)
        self.assertEqual(4, len(list(char.cells(3))))
        self.assertEqual([], list(char.cells(-1)))
        self.assertEqual([], list(char.cells(100)))

    def test_meta(self):
        """Metadata test."""
        char = ch.Character(1, 2)
        self.assertEqual([1, 2], char.metadata())

    def _flag_check(self, flag):
        """Test flag as power of 2."""
        flags = list(flag)
        current = 0
        length = len(flags)
        self.assertTrue(length > 0)
        for f in flags:
            check = pow(2, current)
            self.assertEqual(int(f), check)
            current += 1
        self.assertEqual(length, current)

    def test_flags(self):
        """Test flag definitions."""
        self._flag_check(ch.Stitch)
        self._flag_check(ch.BackStitch)
