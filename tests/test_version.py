#!/usr/bin/python3
"""Tests version information."""
import unittest
import pyxstitch.version as version


class TestVersion(unittest.TestCase):
    """Test version object."""

    def test_same(self):
        """Test version matches setup.py and internal constant."""
        read_version = None
        with open("setup.py", "r") as f:
            for line in f:
                trim = line.strip()
                if not trim.startswith("version="):
                    continue
                self.assertTrue(read_version is None)
                vers = trim.split("=").replace('"', '').replace(',', '')
                read_version = vers
        self.assertTrue(version.__version__, read_version)
