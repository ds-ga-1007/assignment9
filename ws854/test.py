import unittest

from distribution_year import *
from data_analysis_tools import *
from merge_year import *
countries = pd.read_csv("countries.csv")
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx",sheetname="Data",index_col = "gdp pc test")
income = income.T


class MyTest(unittest.TestCase):
    """
    Not too much to test for this program. However, I want to make sure the merge function works.
    """
    def test_database_index(self):

        self.assertEqual(merge_year(income, countries, 1902).result().shape,(277,3))

        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()