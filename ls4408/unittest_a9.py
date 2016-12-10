'''This is a test file to test functions defined by the author
auther: Liwei Song
Time created: 12/04/2016
'''

from a9_function import *
import unittest

class Test(unittest.TestCase):
    
    def test_Merge_by_year(self):
        df_1998=merge_by_year(1998)
        self.assertEqual(df_1998.columns.values[0], 'Country')
        self.assertEqual(df_1998.columns.values[1], 'Region')
        self.assertEqual(df_1998.columns.values[2], 'Income')
        #test the merge_by_year by checking the column names
    
    def test_class(self):
        test=region_explore(2000)
        test.define_year_data()
        #generate an instance of class region_explore
        df_2000=test.data
        self.assertEqual(df_2000.columns.values[0], 'Country')
        self.assertEqual(df_2000.columns.values[1], 'Region')
        self.assertEqual(df_2000.columns.values[2], 'Income')
        #test whether the define_year_data method generates correct dataframe

        
        
if __name__ == "__main__":
    unittest.main() 