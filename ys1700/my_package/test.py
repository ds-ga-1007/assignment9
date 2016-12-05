'''
Created on Dec 5, 2016

@author: sunyifu
'''
import unittest
from analysis_data import *

class Test(unittest.TestCase):


    def test_merged_by_year(self):
        countries, income = read_data()
        merged_data = merge_by_year(2008,income,countries)
        self.assertEqual(merged_data.columns.values.tolist(), ['Country', 'Region', 'Income'])
        self.assertTrue(merged['Region'][Norway], 'Europe')
         
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()