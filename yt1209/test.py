'''
Created on Dec 5, 2016

@author: Yovela
'''
import unittest
from functions import *

countries = pd.read_csv("countries.csv", sep=',')
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0).transpose()

class test(unittest.TestCase):


    def test_input(self):

        with self.assertRaises(KeyError):
            income_distribution(11, income)
        with self.assertRaises(KeyError):
            income_distribution(2900, income)
        with self.assertRaises(KeyError):
            income_distribution(1500, income)
        
            
    def test_merge(self):
        self.assertEqual(merge_by_year(1900, countries, income).columns.values[0], "Country")
        self.assertEqual(merge_by_year(1900, countries, income).columns.values[1], "Region")
        self.assertEqual(merge_by_year(1900, countries, income).columns.values[2], "Income")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()