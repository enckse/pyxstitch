#!/usr/bin/python3
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

    def test_input(self):
        """Test input generator."""
        s = symb.InputStringGenerator("bl")
        t = s.next('red')
        r = s.next('red')
        u = s.next('blue')
        self.assertEqual(t, r)
        self.assertNotEqual(t, u)
        self.assertEqual("b", t)
        self.assertEqual("l", u)
        with self.assertRaises(symb.SymbolError) as cm:
            s.next('yellow')
        self.assertEqual("out of symbols!", str(cm.exception))
        with self.assertRaises(symb.SymbolError) as cm:
            s = symb.InputStringGenerator(" ")
        self.assertEqual("non-alphanumeric not supported", str(cm.exception))
        with self.assertRaises(symb.SymbolError) as cm:
            s = symb.InputStringGenerator("aa")
        self.assertEqual("duplicate symbols detected", str(cm.exception))
        with self.assertRaises(symb.SymbolError) as cm:
            s = symb.InputStringGenerator("")
        self.assertEqual("empty symbol input", str(cm.exception))
