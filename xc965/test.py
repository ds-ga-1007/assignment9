'''
This module tests:
    - visualization class and its methods
    - country_income_display function
    - merge_by_year function in dataprep module
    - exceptions and errors

@author: Xianzhi Cao (xc965)
'''

import unittest
from dataprep import *
from visualtools import *
from UserError import *


class UserTest(unittest.TestCase):
    """
    This class allows users to run tests with classes and functions.
    """

    def setUp(self):
        pass


    def test_data_prep(self):
        '''
        test whether the data_prep function returns the correct DataFrames
        '''
        # test if the size of output of data_prep function is correct
        self.assertEqual(2, len(data_prep()))
        # test whether the output elements are pandas DataFrames
        self.assertEqual(pd.DataFrame, type(data_prep()[0]))


    def test_merge_by_year(self):
        '''
        test whether the merge_by_year function returns the correct object value
        '''
        # test whether the maximum income in year 2012 goes to Qatar (index: 75)
        self.assertEqual(75, merge_by_year(2012).Income.argmax())
        # test whether the region of New Zealand is merged correctly as 'OCEANIA'
        self.assertEqual('OCEANIA', merge_by_year(2000).loc[157, 'Region'])
        # test whether the country with the highest ppp in 1954 is Kuwait
        self.assertEqual('Kuwait', merge_by_year(1954).Country.ix[merge_by_year(1954).Income.argmax()])

        # test whether the country with the highest PPP in year 2010 is Liechtenstein
        self.assertTrue('Liechtenstein',
                        merge_by_year(2010).sort_values(by='Income', ascending=False).head(1).Country)

    def test_country_income_display(self):
        '''
        test whether the expected exceptions and errors occurred when invalid inputs are entered
        '''
        income_df = data_prep()[1]
        # test when year input is emtpy
        with self.assertRaises(EmptyInputError):
            country_income_display(year='', df=income_df)

        # test when the format of year input is correct
        with self.assertRaises(InputFormatError):
            country_income_display(year='foo', df=income_df)
        with self.assertRaises(InputFormatError):
            country_income_display(year='(2000)', df=income_df)
        with self.assertRaises(InputFormatError):
            country_income_display(year='nineteen fifty', df=income_df)
        with self.assertRaises(InputFormatError):
            country_income_display(year='BC2000', df=income_df)
        with self.assertRaises(InputFormatError):
            country_income_display(year='!', df=income_df)

        # test when the chosen year input is within the range
        with self.assertRaises(InputValueError):
            country_income_display(year='2016', df=income_df)
        with self.assertRaises(InputValueError):
            country_income_display(year='1799', df=income_df)

    def test_regional_incomes(self):
        '''
        test whether the correct income lists are returned
        '''
        vis = visualization(1999)
        self.assertEqual(6, len(vis.regional_incomes()))


if __name__ == "__main__":
    unittest.main()
