import unittest
from functions import *
import numpy as np

'''The test script tests to functions for random number between the valid input year. The test passes successfully'''

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col= 0)

class test(unittest.TestCase):
    def test_func(self):
        i = np.random.randint(1800,2012,dtype='I')
        self.assertEqual(list(merge_by_year(i).columns.values),['Country', 'Region', 'Income'])
        self.assertEqual(len(income[i].dropna()),len(countries['Region']))

