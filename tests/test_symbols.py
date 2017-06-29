#!/usr/bin/python
"""Test symbol generator(s)."""
import unittest
import pyxstitch.symbols as symb
import string


class TestSymbols(unittest.TestCase):
    """Test symbols object."""

    def test_reuse(self):
        """Test reuse."""
        s = symb.DefaultSymbolGenerator()
        t = s.next('red')
        r = s.next('red')
        u = s.next('blue')
        self.assertEqual(t, r)
        self.assertNotEqual(t, u)

    def test_out(self):
        """Run out."""
        s = symb.DefaultSymbolGenerator()
        for st in string.printable:
            s.next(st)
        with self.assertRaises(symb.SymbolError) as cm:
            s.next('red')
        self.assertEqual("out of symbols!", str(cm.exception))
