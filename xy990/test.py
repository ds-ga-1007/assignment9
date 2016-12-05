
# coding: utf-8

# In[ ]:

import pandas as pd
import unittest
from analysis import *

countries = pd.read_csv("C:/Users/sherryyang/assignment9/countries.csv")
income =pd.read_csv("C:/Users/sherryyang/assignment9/indicator gapminder gdp_per_capita_ppp.csv",index_col =0)
income = income.T
class SimpleTest(unittest.TestCase):
    #This is a function to test the function merge_by_year.
    
    def testmerge(self):
        for i in income.index:
            merge = analysis.merge_by_year(income,countries, i)
            self.assertEqual(merge.columns.values.tolist(), ['Income','Country','Region'])
            
if __name__ =="__main__":
    unittest.main()
            

