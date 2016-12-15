import unittest
import pandas as pd
from assignment9 import *
from hist_and_boxplot import merge_by_year

class plot_Test(unittest.TestCase):
    '''
    setup the unit_test
    print messages
    '''
    def setUp(self):
        print("Unit_test starting")
        pass
    
    '''
    test merge_year, see if the merged data have the same country name as the original data
    '''
    def test_merge(self):
        countries = pd.read_csv("countries.csv")
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',encoding='iso-8859-1',index_col=0)
        income = income.transpose()
        for year in range(1800,2013):
            self.assertEqual(sum(merge_by_year(2000).Region != countries.Region),0)

    
            
if __name__ == "__main__":
    unittest.main()