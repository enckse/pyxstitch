#!/usr/bin/python3
"""Test output definition."""
import unittest
import pyxstitch.output as out
import pyxstitch.config as cfg
import pyxstitch.version as ver


class TestTextFormat(unittest.TestCase):
    """Test text output object."""

    def test_init(self):
        """Test dump of init object."""
        txt = out.TextFormat(dump=True)
        txt.init("a", (1,), "b", False, cfg.Config(None, None))
        vals = txt.save("blah")
        parts = vals.split("\n")
        self.assertEqual(3, len(parts))
        expect = """
{\"type\": \"init\",
 \"data\": [\"0.5\", \"a\", [1], \"b\", false, [600, 1000, 50, 0, 0, 0]]}"""
        self.assertEqual(expect.replace("\n", "").strip(), parts[0])
        self.assertEqual("{\"type\": \"save\", \"data\": [\"blah\"]}",
                         parts[1])
        self.assertEqual("", parts[2])

    def test_extra(self):
        """Test dump of extra config items."""
        txt = out.TextFormat(dump=True)
        txt.extras(cfg.Config(None, None).dump())
        vals = txt.save("blah")
        parts = vals.split("\n")
        self.assertEqual(3, len(parts))
        expect = """
{\"type\": \"extras\", \"data\": [[\"VERSION\", [0, 0]]]}
                 """.replace("VERSION", ver.__version__)
        self.assertEqual(expect.replace("\n", "").strip(), parts[0])
        self.assertEqual("{\"type\": \"save\", \"data\": [\"blah\"]}",
                         parts[1])
        self.assertEqual("", parts[2])

    def test_rect(self):
        """Test dump of rect object."""
        txt = out.TextFormat(dump=True)
        txt.rect((1, 2, 3), outline='ab')
        vals = txt.save("blah")
        parts = vals.split("\n")
        self.assertEqual(3, len(parts))
        self.assertEqual("{\"type\": \"rect\", \"data\": [[1, 2, 3], \"ab\"]}",
                         parts[0])
        self.assertEqual("{\"type\": \"save\", \"data\": [\"blah\"]}",
                         parts[1])
        self.assertEqual("", parts[2])

    def test_line(self):
        """Test dump of line object."""
        txt = out.TextFormat(dump=True)
        txt.line((0, 5), fill='white')
        vals = txt.save("blah")
        parts = vals.split("\n")
        self.assertEqual(3, len(parts))
        self.assertEqual("{\"type\": \"line\", \"data\": [[0, 5], \"white\"]}",
                         parts[0])
        self.assertEqual("{\"type\": \"save\", \"data\": [\"blah\"]}",
                         parts[1])
        self.assertEqual("", parts[2])

    def test_meta(self):
        """Test dump of text object."""
        txt = out.TextFormat(dump=True)
        txt.meta([], [], 'ab')
        vals = txt.save("blah")
        parts = vals.split("\n")
        self.assertEqual(3, len(parts))
        expect = "{\"type\": \"meta\", \"data\": [[], [], \"ab\"]}"
        self.assertEqual(expect, parts[0])
        self.assertEqual("{\"type\": \"save\", \"data\": [\"blah\"]}",
                         parts[1])
        self.assertEqual("", parts[2])

    def test_text(self):
        """Test dump of text object."""
        txt = out.TextFormat(dump=True)
        txt.text((), 'A', 'a')
        vals = txt.save("blah")
        parts = vals.split("\n")
        self.assertEqual(3, len(parts))
        self.assertEqual("{\"type\": \"text\", \"data\": [[], \"A\", \"a\"]}",
                         parts[0])
        self.assertEqual("{\"type\": \"save\", \"data\": [\"blah\"]}",
                         parts[1])
        self.assertEqual("", parts[2])
