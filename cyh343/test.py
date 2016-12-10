import unittest
from Func.Func import *
from AnalysisTools import AnalysisTools
from assignment9 import year_input

# Since the user input section function main() in assignment9.py is in
# while loop, which difficult to have the test. We split it to just show
# if the input is valid or not.
# Notice that we only test string here because the user only allowed to 
# input string, also only allowed the input between 1800 and 2012

def print_plot(year_string):
    if year_input(year_string) == -9999:
        return('Invalid input')
    else:
        return('Print Plot')
    

class Test(unittest.TestCase):
    
    """Unittest for testing whether the user input is correct or not, and the merge function"""

    def test_year_input_invalid(self):
        self.assertEqual(print_plot('A'), 'Invalid input')
        self.assertEqual(print_plot('$'), 'Invalid input')
        self.assertEqual(print_plot('0'), 'Invalid input')
        self.assertEqual(print_plot(' '), 'Invalid input')
        self.assertEqual(print_plot('10**'), 'Invalid input')
        self.assertEqual(print_plot('1700'), 'Invalid input')
        self.assertEqual(print_plot('-2012'), 'Invalid input')
        self.assertEqual(print_plot('2013'), 'Invalid input')
    
    def test_year_input_valid(self):
        self.assertEqual(print_plot('1800'), 'Print Plot')
        self.assertEqual(print_plot('1900'), 'Print Plot')
        self.assertEqual(print_plot('2000'), 'Print Plot')
        self.assertEqual(print_plot('2012'), 'Print Plot')
        
    def test_merge(self): 
        merged = merge_by_year(1800)
        self.assertEqual(merged.columns.values.tolist(), ['Country', 'Region', 'Income'])
        self.assertEqual(merged.ix[0][1], 'AFRICA')

if __name__ == "__main__":
    unittest.main()