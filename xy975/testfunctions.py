from pac.functions import *
import unittest

class functionsTest(unittest.TestCase):
    """
    Test functions in functions.
    Assume that the type of all inputs are correct; otherwise, 
    functions in assignment9 will find the invalid input.
    """
    def test_year_valid(self): 
        self.assertEqual(year_valid(1800),1800)
        self.assertEqual(year_valid(2012),2012)
        self.assertEqual(year_valid(1900),1900)
        
        with self.assertRaises(ValueError):
            year_valid(1700)
        with self.assertRaises(ValueError):
            year_valid(2013)
        
    def test_merge_by_year(self):
        m = merge_by_year(income, countries, 2012)
        self.assertEqual(int(m[m.Country == 'Eritrea'].Income), 613)
        self.assertEqual(int(m[m.Country == 'Greece'].Income), 21811)
        m = None
        
if __name__ == "__main__":
    unittest.main()
