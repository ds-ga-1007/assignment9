# Author: Leslie Huang (lh1036)
# Description: unit tests for helper functions that handle and parse user input

import unittest
from income.distribution import IncomeDistribution 
from income.exceptions import *
from userinput import *
import pandas as pd

class QuittingInputTests(unittest.TestCase):
    '''
    Test that quitting_input ends program when input is "finish" but not otherwise
    '''
    def test_finish(self):
        with self.assertRaises(QuitError):
            quitting_input("", lambda _: "finish")
            
    def test_valid_input(self):
        self.assertEqual(quitting_input("", lambda _: "1999"), "1999")

class IncomeTestCase(unittest.TestCase):
    '''
    Base class for TestCases that require income DF
    '''
    
    def setUp(self):
        income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = "gdp pc test")
        self.income = income.transpose()
    

class PromptForYearTests(IncomeTestCase):
    '''
    Tests for prompt_for_year 
    '''
    def test_valid_year(self):
        '''
        Test that prompt_for_year correctly returns a valid year
        '''
        self.assertEqual(prompt_for_year(self.income, lambda _: "1999"), 1999)
            

class ValidateYearTests(IncomeTestCase):
    '''
    Tests that validate_year raises exception for invalid input or year outside of range
    '''
    
    def test_valid(self):
        '''
        Test validate_year on valid year
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
    
