'''
Created on Dec 4, 2016

@author: Zahra
'''
import unittest
from auxilary_functions import *
from explore import *


class Test(unittest.TestCase):


    def test_merge_by_year(self):
        self.assertEqual(merge_by_year(2008).shape, (177, 3))
        self.assertEqual(merge_by_year(1998).shape, (177, 3))
    
    def test_merge_by_year2(self):
        self.assertEqual(merge_by_year(2014), 'No data for this year!')
        self.assertEqual(merge_by_year(109), 'No data for this year!')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_merge_by_year']
    unittest.main()