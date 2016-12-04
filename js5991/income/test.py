'''
Created on Dec 3, 2016

@author: Jy
'''
import unittest
from income import load_display_data
from income.load_display_data import merge_by_year, income_transpose, countries

class Test(unittest.TestCase):
    
    def test_merge_columns(self):
        
        self.assertListEqual(list(merge_by_year(1801).columns.values),['Country', 'Income', 'Region'])
        
    def test_merge_income(self):
        self.assertEqual(merge_by_year(1901)[merge_by_year(1901)["Country"]=="United States"]["Income"].item(), income_transpose["United States"].loc[1901])
        self.assertEqual(merge_by_year(2001)[merge_by_year(2001)["Country"]=="United States"]["Income"].item(), income_transpose["United States"].loc[2001])
        self.assertEqual(merge_by_year(1852)[merge_by_year(1852)["Country"]=="Australia"]["Income"].item(), income_transpose["Australia"].loc[1852])
        self.assertEqual(merge_by_year(1985)[merge_by_year(1985)["Country"]=="China"]["Income"].item(), income_transpose["China"].loc[1985])
    
    def test_merge_region(self):
        self.assertEqual(merge_by_year(1901)[merge_by_year(1901)["Country"]=="United States"]["Region"].item(), countries[countries["Country"]=="United States"]["Region"].item())
        self.assertEqual(merge_by_year(2001)[merge_by_year(2001)["Country"]=="United States"]["Region"].item(), merge_by_year(1901)[merge_by_year(1901)["Country"]=="United States"]["Region"].item())
        self.assertEqual(merge_by_year(1852)[merge_by_year(1852)["Country"]=="Australia"]["Region"].item(), countries[countries["Country"]=="Australia"]["Region"].item())
        self.assertEqual(merge_by_year(1985)[merge_by_year(1985)["Country"]=="China"]["Region"].item(), countries[countries["Country"]=="China"]["Region"].item())        
    
if __name__ == "__main__":
    unittest.main()