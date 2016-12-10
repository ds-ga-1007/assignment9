import unittest
from analysis import *

'''Unittest that tests the functions from class analysis'''
class Test(unittest.TestCase):
    '''Test function merge_by_year'''
    def test_merged(self):
        countries = pd.read_csv('countries.csv')
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').transpose()
        income.columns = [income.ix[0]]
        income = income.drop(['gdp pc test'],axis=0)
        merged = merge_by_year(2007,income,countries)
        self.assertTrue(merged['Country'][4], 'Burundi')
        self.assertTrue(merged['Region'][4], 'AFRICA')
        self.assertEqual(merged['Income'][4], 445.873956719168)

if __name__ == "__main__":
    unittest.main()