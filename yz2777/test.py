""" Unittest for testing whether the user input is correct or not """

import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import func
from class_analysis import analysis_tools
from assignment9 import year_input_correct 


# user input part (i.e., inpt()) in assignment9.py is in while loop, difficult to do test
# split it to just show whether the user input is invalid or not
# here only test string because the user input is string only
# also only the input between 1800 and 2012 is acceptable
def print_plot(year_string):
    if year_input_correct(year_string) == -9999:
        return ('Invalid year input')
    else:
        return ('Plots will be printed')


class Test(unittest.TestCase):
    def test_year_input_invalid(self):
        self.assertEqual(print_plot('a'), 'Invalid year input')
        self.assertEqual(print_plot('*'), 'Invalid year input')
        self.assertEqual(print_plot('1'), 'Invalid year input')
        self.assertEqual(print_plot(' '), 'Invalid year input')
        self.assertEqual(print_plot('a1*'), 'Invalid year input')
        self.assertEqual(print_plot('1799'), 'Invalid year input')
        self.assertEqual(print_plot('-1800'), 'Invalid year input')
        self.assertEqual(print_plot('2013'), 'Invalid year input')

    def test_year_input_valid(self):
        self.assertEqual(print_plot('1800'), 'Plots will be printed')
        self.assertEqual(print_plot('1988'), 'Plots will be printed')
        self.assertEqual(print_plot('2000'), 'Plots will be printed')
        self.assertEqual(print_plot('2012'), 'Plots will be printed')
        
    
if __name__ == "__main__":
    unittest.main()
