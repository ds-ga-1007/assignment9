"""
Date: Dec 5, 2016
Author: Chloe Meng(lm3226)
Description: This program tests functions in read_and_display_GDP.
"""
import unittest
from read_and_display_GDP import *

class test_daily_investement_return(unittest.TestCase):
    def test_data_analysis_graphs_class(self):
        with self.assertRaises(ValueError):
            data_analysis_graphs(1799)
        with self.assertRaises(ValueError):
            data_analysis_graphs(2013)
        with self.assertRaises(ValueError):
            data_analysis_graphs('abc')

    def test_read_and_display_GDP_class(self):
        with self.assertRaises(ValueError):
            read_and_display_GDP(1799)
        with self.assertRaises(ValueError):
            read_and_display_GDP(2013)
        with self.assertRaises(ValueError):
            read_and_display_GDP('abc')

if __name__ == "__main__":
    unittest.main()
