'''
Created on Dec 4, 2016
@author: Yanli Zhou
'''
import unittest
from Data_processing import *
from Data_tool import *


class Test(unittest.TestCase):

    def test_merge_by_year(self):
        self.assertEqual(merge_by_year(1801).shape, (177, 3))
        self.assertEqual(merge_by_year(2011).shape, (177, 3))
    
    def test_merge_by_year2(self):
        self.assertEqual(merge_by_year(2222), 'No data for the year entered!')
        self.assertEqual(merge_by_year(9), 'No data for the year entered!')

if __name__ == "__main__":
    unittest.main()