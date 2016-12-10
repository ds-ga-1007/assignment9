import unittest
from income.income_class import *
from income.functions import *
from income.exceptions import *

class SimpleTest(unittest.TestCase):
    '''This unittest tests the validity of the user inputs and the results of the 
merge_by_year function.'''
    
    def test_inputvalidity(self):
        '''This function tests the validity of user inputs. Invalid inputs would raise
exceptions.'''
        self.assertEqual(check_validity('2008'), '2008')
        with self.assertRaises(BreakException):
            check_validity('finish')
        with self.assertRaises(IntegerError):
            check_validity('test')
        with self.assertRaises(IntegerError):
            check_validity('6.4')
        with self.assertRaises(RangeError):
            check_validity('2017')
    
    def test_merge(self):
        '''This function tests whether the merge_by_year function returns the correct 
DataFrame.'''
        self.assertEqual(merge_by_year('2012').shape, (177,3))
        self.assertEqual(merge_by_year('1997').iloc[0,1], 'AFRICA')
        self.assertEqual(merge_by_year('1993').iloc[2,0], 'Benin')
        self.assertEqual(list(merge_by_year('2007').columns), ['Country', 'Region', 'Income'])

if __name__ == '__main__':
    unittest.main()