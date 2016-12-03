# Author: Leslie Huang (lh1036)
# Description: main unit tests

import unittest
from income.distribution import IncomeDistribution 
from income.exceptions import *
from assignment9 import *

class MainTests(unittest.TestCase):
    
    def test_validate_year(self):
        
    
    def test_quitting_input(self):
        '''
        Test that 'finish' terminates program by raising QuitError 
        '''
        with self.assertRaises(QuitError):
            quitting_input("finish")
            
            
if __name__ == '__main__':
    unittest.main()
    
