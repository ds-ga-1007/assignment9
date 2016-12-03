# Author: Leslie Huang (lh1036)
# Description: unit tests for helper functions that handle and parse user input

import unittest
from income.distribution import IncomeDistribution 
from income.exceptions import *
from userinput import *
import pandas as pd

class ValidateYearTests(unittest.TestCase):
    '''
    Tests that validate_year raises exception for invalid input or year outside of range
    '''
    
    def setUp(self):
        income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = "gdp pc test")
        self.income = income.transpose()
    
    def test_valid(self):
        '''
        test valid year
        '''
        self.assertEqual(validate_year(1970, self.income), 1970)
    
    def test_invalidtype(self):
        '''
        test invalid input type raises exception
        '''
        with self.assertRaises(InvalidYearError):
            validate_year("foo", self.income)
        
        with self.assertRaises(InvalidYearError):
            validate_year("2.1", self.income)
    
    def test_year_out_of_bounds(self):
        '''
        test int year out of bounds raises exception
        '''
        with self.assertRaises(InvalidYearError):
            validate_year("2016", self.income)

            
if __name__ == '__main__':
    unittest.main()
    
