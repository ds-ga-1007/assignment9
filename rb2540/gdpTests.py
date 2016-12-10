import unittest
from assignment9 import *

class gdpTest(unittest.TestCase):
    """Class to test the merge_by_year function"""
    def testMergeByYear(self):
        """Loads data and checks for an arbitrary year (2000) that the column names are correct 
        and have been loaded properly"""
        loadData()
        d = merge_by_year(2000)
        self.assertTrue('Region' in d.columns.values)
        self.assertTrue('Country' in d.columns.values)
        self.assertTrue('Income' in d.columns.values)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()