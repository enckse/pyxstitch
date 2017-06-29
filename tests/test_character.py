import unittest
import pyxstitch.character as ch

class TestCharacter(unittest.TestCase):
    """Test character object."""


    def test_cells(self):
        """Cell data retrieval."""
        char = ch.Character(5, 3)
        self.assertEqual(4, len(list(char.cells(3))))
        self.assertEqual([], list(char.cells(100)))
