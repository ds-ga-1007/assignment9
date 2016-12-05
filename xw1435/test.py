import unittest
from function import merge_by_year


class Test(unittest.TestCase):
    
    def test_merge_by_year(self):
        self.assertEqual(merge_by_year(2012).shape, (177, 3))
        self.assertEqual(merge_by_year(1994).shape, (177, 3))
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()