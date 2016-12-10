import unittest
from analysis import *

class Test(unittest.TestCase):
    def test_merge_function(self):
        countries=pd.read_csv("/Users/zoem/Documents/ds1007/assignment9/countries.csv")
        income=pd.read_excel("/Users/zoem/Documents/ds1007/assignment9/indicator_gapminder_gdp_per_capita_ppp.xlsx")
        income=income.transpose()
        income.columns = [income.ix[0]]
        merged_data = merge_by_year(2007, countries, income)

        self.assertEqual(list(merged_data.columns),['Country', 'Region', 'Income'])
        self.assertEqual(merged_data.Country[0],'Algeria')
        self.assertEqual(merged_data.Region[0],'AFRICA')
        self.assertEqual(int(merged_data.Income[0]),6133)
         
if __name__ == '__main__':
    unittest.main() 
