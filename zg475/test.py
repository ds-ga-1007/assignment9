'''
Test module for the program

Created on Dec 3, 2016
@author: Zhiqi Guo(zg475)
@email: zg475@nyu.edu
'''
import unittest
import pandas as pd
from graph import merge_by_year
from data_process import load_data

countries = load_data('countries')
income = load_data('income')

class Test(unittest.TestCase): 
    '''
    Run the test in the project's root directory
    with the following command:
        $ python -m unittest discover
    '''
    def test_merge(self):
        '''
        Test merge function Exhaustively for every country at year 2000. 
        And repeat the test 10 times. 
        '''
        for count in range(10):
            year = 2000
            income_yr = pd.DataFrame(income.ix[year]).astype(float)
            merged = merge_by_year(year)
            
            for country in merged['Country']:
                bool = (merged['Country']==country)
                self.assertTrue( (merged[bool]['Income'] == income_yr.ix[country]).all()  )

if __name__ == "__main__":
    
    unittest.main()