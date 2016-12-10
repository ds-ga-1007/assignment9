import unittest
from function import *
from hist_box_class import hist_box
from assignment9 import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Test(unittest.TestCase):
    def test_input_year_correct(self):
        #In function justify, 0 indicates valid input and 1 indicates wrong input
        self.assertEqual(justify('1'),1)
        self.assertEqual(justify('100'),1)
        self.assertEqual(justify('-100'),1)
        self.assertEqual(justify('shy'),1)
        self.assertEqual(justify('shy2000'),1)
        self.assertEqual(justify('$'),1)
    def test_input_year_wrong(self):
        #In function justify, 0 indicates valid input and 1 indicates wrong input
        self.assertEqual(justify('1800'),0)
        self.assertEqual(justify('2012'),0)
        self.assertEqual(justify('2000'),0)
        self.assertEqual(justify('2008'),0)
        self.assertEqual(justify('1900'),0)
        self.assertEqual(justify('1990'),0)
if __name__ == "__main__":
    unittest.main()