import unittest
import pandas as pd
from Methods import merge_by_year

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).T

# This is the unittest class. 
class MergeTest(unittest.TestCase):
    
    # This function will test the merge_by_year function for a certain year to see
    # if the function returns a dataframe where all rows have 3 columns. 
    def testMerge(self):
    	self.assertTrue(all(map(lambda x: x in ['Country', 'Region', 'Income'], merge_by_year(1999, income, countries))))

if __name__ == "__main__":
    unittest.main()