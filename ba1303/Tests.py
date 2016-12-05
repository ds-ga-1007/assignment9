import unittest
from functions_and_classes import *
countries = pd.read_csv('/Users/Brenton/assignment9/countries.csv')
income = pd.read_excel('/Users/Brenton/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 'gdp pc test')


class Test(unittest.TestCase):

    def setUp(self):
        pass 

    def test_classYear1(self):
        '''Basic test for class "YEAR"'''
        year_value = 1892
        self.assertEqual(YEAR(1892).year_value, 1892)

    def test_classYear2(self):
        '''Test to reject years that are not in the range 1800-2012'''
        with self.assertRaises(YearOutOfRange) as message:
            YEAR(2016)
        self.assertTrue('Year must be between 1800 and 2012.' in str(message.exception))

    def test_classYear3(self):
        '''Test to reject non-integer input for year''' 
        with self.assertRaises (TypeError) as message:
            YEAR(1900.5)
        self.assertTrue('Must be an integer' in str(message.exception))

    def test_merge_by_year1(self):
        '''Test to see if dataframe has the correct three columns'''
        merged_df = merge_by_year(YEAR(2000).year_value, income, countries)
        self.assertEqual(list(merged_df.columns.values), ['Country', 'Region', 'Income']), 

    def test_merge_by_year2(self):
        '''Test to see if new dataframe has accurate information.'''
        merged_df = merge_by_year(YEAR(1800).year_value, income, countries)
        reindexed_df = merged_df.set_index('Country') #necessary step for test - index values of merged_df are unhelpful
        region_column = reindexed_df['Region']
        income_column = reindexed_df['Income']
        self.assertEqual(region_column['Norway'], 'EUROPE')
        self.assertEqual(income_column['Norway'], 950.0)

        
if __name__ == '__main__':
    unittest.main()
