'''
    This module is the unit test for investment.py program.
'''

import unittest
import numpy as np
from incomeclass import mergeByYear

class TestIncome(unittest.TestCase):

    def calcPositionValue(self):
        merge_df = mergeByYear(1800, income, countires)
        self.assertEqual(merge_df.loc[:53, 'Region'].unique(), np.array(['AFRICA'], dtype=object))

if __name__ == '__main__':
    unittest.main()
