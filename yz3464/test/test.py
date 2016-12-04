'''
Created on Dec 4, 2016

@author: twff
'''
import unittest
from tools import *
#import pandas as pd
import numpy as np

countries = pd.read_csv('/Users/twff/assignment9/yz3464/countries.csv', index_col = 0) #question1
income = pd.read_excel('/Users/twff/assignment9/yz3464/indicator gapminder gdp_per_capita_ppp.xlsx',index_col = 0)

class testClass:
    def setUp(self):
        pass
    
    def testMerge(self):
        for year in income.T.index:
            merged = merge_by_year(countries, income, year)
            for country, region, income in merged.values:
                self.assertEqual(income.loc[year, country], income)
                
        merged = merge_by_year(countries, income, 2012)
        self.assertEqual(merged.ix[0][1],'AFRICA')
        
        merged = merge_by_year(countries, income, 2002)
        self.assertEqual(merged.ix[100][1],'EUROPE')
        
        
if __name__ == "__main__":
    unittest.main()