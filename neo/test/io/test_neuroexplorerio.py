# encoding: utf-8
"""
Tests of io.NeuroExplorerIO
"""

from __future__ import division

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from neo.io import NeuroExplorerIO
import numpy

from neo.test.io.common_io_test import BaseTestIO, download_test_files_if_not_present

files_to_test = [ 'File_neuroexplorer_1.nex',
                        'File_neuroexplorer_2.nex',
                        ]


class TestNeuroExplorerIO(unittest.TestCase, BaseTestIO):
    ioclass = NeuroExplorerIO
    
    def test_on_files(self):
        localdir = download_test_files_if_not_present(NeuroExplorerIO, files_to_test)




if __name__ == "__main__":
    unittest.main()
