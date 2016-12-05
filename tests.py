import unittest
import pandas as pd
from dataset import *

"""
This class tests the merge function.
"""

class Tests(unittest.TestCase):

    def testMerge(self):
        merged = merge_by_year(1800)
        self.assertEqual(merged.columns.values.tolist(), ['Country', 'Region', 'Income'])
        self.assertEqual(merged.ix[0][1], 'AFRICA')

if __name__=="__main__":
    unittest.main()
