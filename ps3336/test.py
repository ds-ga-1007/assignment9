'''
Created on Nov 30, 2016

@author: peimengsui
@desc: test the data analysis tool program
'''
import unittest
from dataTool import *

countries = pd.read_csv('countries.csv',index_col=0)
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
class Test(unittest.TestCase):
    def testMerge(self):
        self.assertTrue(all(map(lambda v:v in ['Region','Income','Country'],merge_by_year(countries,income,2000))))
if __name__ == "__main__":
    unittest.main()