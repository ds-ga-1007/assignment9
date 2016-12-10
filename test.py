# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:21:15 2016

@author: kevinyan
"""

import unittest
import pandas as pd
from summaryInfo import *

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()


class Test(unittest.TestCase):
    
    def testMerged(self):
        mergedTest = mergeByYear(2007,income,countries)
        #check if the dataFrame is correctly constructed
        self.assertTrue(all(map(lambda x: x in ['Country', 'Region', 'Income'], mergedTest)))
        self.assertTrue(mergedTest['Country'][4], 'Burundi')
        self.assertTrue(mergedTest['Region'][5], 'AFRICA')
        
        
if __name__ == "__main__":
    unittest.main()