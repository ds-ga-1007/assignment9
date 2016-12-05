'''
Created on Dec 5, 2016

@author: Akash
'''
import sys
sys.path.append('..')

import unittest
import pandas as pd
from income_dist import income_distribution


class Test(unittest.TestCase):
    def setUp(self): # To load the data for testing and create a class of income distribution
        country_by_region_data = pd.read_csv('../countries.csv')
        gdp_by_year = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx')
        
        self.test_inputs = income_distribution()
        self.test_inputs.set_Data(country_by_region_data, gdp_by_year)
        
    def test_check_valid_year(self): # test case for valid input
        self.test_inputs.check_valid_year('1990', 0)
        self.assertEqual(self.test_inputs.valid_input, 1)
        
    def test_check_invalid_year_1(self): # test cases to check invalid inputs
        self.test_inputs.check_valid_year('12345', 0)
        self.assertEqual(self.test_inputs.valid_input, 0)
        
    def test_check_invalid_year_2(self):
        self.test_inputs.check_valid_year('asdfgh', 0)
        self.assertEqual(self.test_inputs.valid_input, 0)
        
    def test_check_invalid_year_3(self):
        self.test_inputs.check_valid_year('1234asdf', 0)
        self.assertEqual(self.test_inputs.valid_input, 0)
    
    def test_merged_check_columns(self):  # Test to check that merged data has three columns - Country, Region and Income
        merged_data = self.test_inputs.merge_by_year(1888)
        self.assertEqual(merged_data.shape[1], 3)
    
    def test_transposed_data_head_rows(self): # Test to check that the head data has 5 rows
        head_data = self.test_inputs.display_head()
        self.assertEqual(head_data.shape[0], 5)


if __name__ == "__main__":
    unittest.main()