'''
Created on Dec 4, 2016

@author: ShashaLin
'''
import unittest
from funcs import merge_by_year, Region
import pandas as pd
import os
import matplotlib.pyplot as plt
cwd = os.getcwd()
countries = pd.read_csv(cwd + '/countries.csv')
income = pd.read_excel(cwd + '/indicator gapminder gdp_per_capita_ppp.xlsx',
                      index_col = 0).T
class Test(unittest.TestCase):


    def testMerge(self):
        self.assertEqual(merge_by_year(1820, income, countries).shape[0], 3)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()