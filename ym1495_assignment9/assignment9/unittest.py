'''
Created on Dec 5, 2016

@author: muriel820
'''
import unittest
import pandas as pd
import sys
from assignment9.functions import *
from assignment9.loadData import *
from assignment9.functions import *
from assignment9.exceptions import *

class Test(unittest.TestCase):
    def test_merge_by_year(self):
        test = loadData()
        test_merge = merge_by_year(test.income,test.countries,2001)
        self.assertEqual(test_merge.columns.values.tolist(), ['Country', 'Region', 'Income'])
        self.assertTrue(test_merge['Region']['Norway'], 'Europe')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()