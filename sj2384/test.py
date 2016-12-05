'''
Created on Dec 5, 2016

@author: sj238
'''

import unittest
from dataNmerge import *
import random

class Test(unittest.TestCase):
    '''This class test the merge_by_year function randomly chooses
       a year to check if the country region and income columns have the correct data
    '''
    def test_merge_by_year(self):
        a = merge_by_year(random.randrange(1800,2013,1))
        self.assertEqual(a.columns.values.tolist(), ['Country', 'Region', 'Income'])
        self.assertEqual(a.ix[0][1], 'AFRICA')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()