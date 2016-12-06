'''
Created on 2016.12.5

@author: xulei
'''

import unittest
from assignment9 import *
from load_data import *
from excep_class import *
from year_class import *
from Region_class import *

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_Year(self):
        self.assertSequenceEqual([Year('1888').yr,Year('1952').yr,Year('1844').yr],[1888,1952,1844])
        
        with self.assertRaises(rangeException):
            Year('1233')


if __name__ =='__main__':
    unittest.main()