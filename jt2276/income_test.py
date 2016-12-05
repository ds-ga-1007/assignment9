'''
Unittest for assignment 9 package
@author: jonathanatoy
'''
import unittest
from income_package.assignment9 import YearException


class Test(unittest.TestCase):


    def testValidYearCheck1(self):
        input = '1945'
        year = validYearCheck(input)
        self.assertEqual(1945, year)
        
    def testValidYearCheck2(self):
        valid = True
        input = '1492'
        try:
            year = validYearCheck(input)
        except YearException:
            valid = False
        self.assertEqual(valid, False)
        
    def testValidYearCheck3(self):
        valid = True
        input = 'Non-number'
        try:
            year = validYearCheck(input)
        except YearException:
            valid = False
        self.assertEqual(valid, False)
if __name__ == "__main__":
    unittest.main()