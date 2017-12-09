#!/usr/bin/python
"""Test config definitions."""
import unittest
import pyxstitch.config as cfg
import pyxstitch.log as log


class TestConfig(unittest.TestCase):
    """Test config object."""

    def setUp(self):
        """Test setup."""
        log.Log.is_verbose = False

    def tearDown(self):
        """Test teardown."""
        log.Log.is_verbose = True

    def test_no_ins(self):
        """No inputs defined."""
        conf = cfg.Config(None, "test")
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config([], None)
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)

    def test_ins(self):
        """Input defined."""
        conf = cfg.Config(["input=1=2", "input"], None)
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        self.assertEqual(0, conf.page_no_index)
        self.assertEqual(0, conf.page_legend)
        self.assertEqual(0, conf.page_font_size)
        conf = cfg.Config(["input=0", "page_input=1"], None)
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config(["page_pad=0", "page_input=1"], None)
        self.assertEqual(600, conf.page_height)
        self.assertEqual(1000, conf.page_width)
        self.assertEqual(50, conf.page_pad)
        conf = cfg.Config(["page_pad=1",
                           "page_width=2",
                           "page_height=-100",
                           "page_no_index=1",
                           "page_legend=1",
                           "legend_hoff=1000",
                           "legend_woff=10",
                           "page_font_size=50"], None)
        self.assertEqual(600, conf.page_height)
        self.assertEqual(2, conf.page_width)
        self.assertEqual(1, conf.page_pad)
        self.assertEqual(1, conf.page_no_index)
        self.assertEqual(1, conf.page_legend)
        self.assertEqual(1000, conf.legend_hoff)
        self.assertEqual(10, conf.legend_woff)
        self.assertEqual(50, conf.page_font_size)
        conf = cfg.Config(["page_no_index=0"], None)
        self.assertEqual(0, conf.page_no_index)
        conf = cfg.Config(["page_no_index=-1"], None)
        self.assertEqual(0, conf.page_no_index)
        conf = cfg.Config(["page_no_index=1"], None)
        self.assertEqual(1, conf.page_no_index)
        conf = cfg.Config(["legend_hoff=-100"], None)
        self.assertEqual(-100, conf.legend_hoff)
        conf = cfg.Config(["legend_woff=-20"], None)
        self.assertEqual(-20, conf.legend_woff)
        conf = cfg.Config(["page_font_size=40"], None)
        self.assertEqual(40, conf.page_font_size)

    def test_save_load(self):
        """Save and load config."""
        cg = cfg.Config(["page_pad=1", "page_width=2", "page_height=-100"],
                        None)
        conf = cfg.Config.load(cg.save())
        self.assertEqual(600, conf.page_height)
        self.assertEqual(2, conf.page_width)
        self.assertEqual(1, conf.page_pad)

    def test_dump(self):
        """Dumping extras."""
        cg = cfg.Config(["page_pad=1", "legend_hoff=-10"], None)
        dmp = cg.dump()
        self.assertEqual(2, len(dmp))
        self.assertEqual(-10, dmp[0])
        self.assertEqual(0, dmp[1])
