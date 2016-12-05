import unittest
from IncomeAnalysisToolKit import IncomeAnalysisToolKit
import pandas as pd



class TestTool(unittest.TestCase):
    
    def test_merge(self):
    	countries = pd.read_csv('countries.csv',index_col = 0, header = 0)
    	income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col = 0, header = 0).transpose()
    	target = IncomeAnalysisToolKit(countries, income)
    	self.assertTrue(all(map(lambda x: x in ['Region','Income','Country'], target.merge_by_year(2012))))
    	self.assertEqual(target.merge_by_year(2009).shape, (177, 3))



if __name__ == '__main__':
    unittest.main(exit=False)