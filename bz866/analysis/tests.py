'''
Created on 2016年12月4日

@author: bz866
'''
import unittest
import numpy as np
from analysis.data_analysis import *
from analysis.functions import *

class TestIncome(unittest.TestCase):

    def calcPositionValue(self):
        merge_df = merge_by_year(1800, countries, income)
        self.assertEqual(merge_df.loc[:53, 'Region'].unique(), np.array(['AFRICA'], dtype=object))

if __name__ == '__main__':
    unittest.main()