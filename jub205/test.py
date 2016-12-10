"""
Created on Sat Dec 3 2016
@author: jinubak/jub205
@desc: This file contains unittest for GDPanalysis.py
"""

import unittest
import GDPanalysis as gdp

class MyTest(unittest.TestCase):
    
    def test_country_data_load(self):
        
        df = gdp.load_country_data('../countries.csv')
        self.assertEqual(len(df), 194)
        self.assertEqual(df.shape,(194,2))
        self.assertRaises(SystemExit,gdp.load_country_data,'wrongfile.csv')
        
    def test_income_data_load(self):
        
        df = gdp.load_gdp_data('../indicator gapminder gdp_per_capita_ppp.xlsx')
        self.assertEqual(len(df), 214)
        self.assertEqual(df.shape,(214,260))
        self.assertRaises(SystemExit,gdp.load_gdp_data,'wrongfile.xlsx')
    
    def test_merge_function(self):
        
        countries = gdp.load_country_data('../countries.csv')
        income = gdp.load_gdp_data('../indicator gapminder gdp_per_capita_ppp.xlsx')
        year = '2006'
        merged_data = gdp.merge_by_year(year, countries, income)   
        
        self.assertEqual(list(merged_data.columns),['Country', 'Region', 'Income'])
        self.assertEqual(merged_data.Country[0],'Algeria')
        self.assertEqual(merged_data.Region[0],'AFRICA')
        self.assertEqual(int(merged_data.Income[0]),6022)
        
if __name__ == '__main__':
    unittest.main()