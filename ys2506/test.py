# Solution for DS-GA 1007 Assignment#9
# Author: Yanan Shi y2506 N11812897
import unittest
from exceptions import InvalidInputException
from dataAnalysis import DataAnalysis
from assignment9 import validYears

#Unit tests are provided with the solution code
#The unit tests pass correctly
class Test(unittest.TestCase):
    
    #test function validYears
    def test_validYears(self):
        self.assertEqual(validYears('2000'),2000)
        self.assertEqual(validYears('1992'),1992)
        self.assertEqual(validYears('2001'),2001)
        self.assertEqual(validYears('2011'),2011)
        self.assertEqual(validYears('1989'),1989)
        self.assertEqual(validYears('2010'),2010)
        
        with self.assertRaises(InvalidInputException):
            validYears('abc')
            validYears('1799')
            validYears('2018')


if __name__ == "__main__":
    unittest.main()