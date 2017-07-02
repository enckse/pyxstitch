#!/usr/bin/python
"""Test config definitions."""
import unittest
import pyxstitch.config as cfg


class TestConfig(unittest.TestCase):
    """Test config object."""

    def test_no_ins(self):
        """No inputs defined."""
        conf = cfg.Config(None)
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config([])
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)

    def test_ins(self):
        """Input defined."""
        conf = cfg.Config(["input=1=2", "input"])
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config(["input=0", "page_input=1"])
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config(["page_pad=0", "page_input=1"])
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config(["page_pad=1", "page_width=2", "page_height=-100"])
        self.assertEqual(600, conf.page_height)
        self.assertEqual(2, conf.page_width)
        self.assertEqual(1, conf.page_pad)
