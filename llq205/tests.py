import unittest
from graphs import *
import pandas as pd

# $ python -m unittest -v tests.py

class Tests(unittest.TestCase):
    
    def testMerge(self):
        """Tests for merge function"""
        countries = pd.read_csv("countries.csv")
        income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0)
        income = income.T
        
        merged = merge_by_year(countries, income, 1800)
        self.assertEqual(merged.columns.values.tolist(), ['Country', 'Region', 'Income'])
        self.assertEqual(merged.ix[0][1], 'AFRICA')
        
if __name__ == "__main__":
    unittest.main()

