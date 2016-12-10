'''
Created on Dec 4, 2016

@author: felix
'''
import unittest
from data_funcs import *

class Test(unittest.TestCase):


    def test_get_countries(self):
        test_df = get_countries()
        self.assertEquals(test_df['Region'][0],'AFRICA')
        
    def test_get_income(self):
        test_df = get_income()
        self.assertEquals(test_df.iloc[1,1],472.05349959347001)
    
    def test_valid_year_str(self):
        corr_list = ['1234','4567','0123','9876']
        for this_str in corr_list:
            self.assertEqual(valid_year_str(this_str), True)
            
        wrong_list = ['dfksdaf','123','45673.','90']
        for this_str in wrong_list:
            self.assertEqual(valid_year_str(this_str), False)
            
    def test_valid_finish_str(self):
        corr_list = ['finish','Finish','FINISH','FinIsh']
        for this_str in corr_list:
            self.assertEqual(valid_finish_str(this_str), True)
            
        wrong_list = ['finish ','123','45673.','90']
        for this_str in wrong_list:
            self.assertEqual(valid_finish_str(this_str), False)
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()