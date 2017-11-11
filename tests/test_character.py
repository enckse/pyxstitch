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
