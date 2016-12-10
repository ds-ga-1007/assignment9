# Author: Leslie Huang (lh1036)
# Description: unit test for function that appears in the main ("assignment9" file)

import unittest
from income.distribution import IncomeDistribution 
from income.exceptions import *
from assignment9 import *
from pandas.util.testing import assert_frame_equal

class IncomeCountriesTestCase(unittest.TestCase):
    '''
    Base class for TestCases that require income, countries, and example merged DFs
    '''
    
    def setUp(self):
        income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = "gdp pc test")
        self.income = income.transpose()
        self.countries = pd.read_csv("countries.csv", index_col = "Country")
        
        # create an example DF of a merged year
        merged1999 = self.countries.join(self.income.ix[1999], how = "outer")
        merged1999.reset_index(level = 0, inplace = True)
        self.merged1999 = merged1999.rename(columns = {"index": "Country", 1999: "Income"})        


class MainTests(IncomeCountriesTestCase):
    '''
    Unit tests for functions that appear in the main (there is only one)
    '''
    def test_merge_by_year(self):
        '''
        Test merge_by_year function generates correct dataframe
        '''
        assert_frame_equal(merge_by_year(1999, self.income, self.countries), self.merged1999)
            
            
if __name__ == '__main__':
    unittest.main()
    


### Sources consulted:
# https://penandpants.com/2014/10/07/testing-with-numpy-and-pandas/