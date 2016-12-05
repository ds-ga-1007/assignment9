import unittest
from EconVisualizer import *

class TestVisualizerUtilities(unittest.TestCase):
    """
    Visualizer utility test cases
    """
    def setUp(self):

        self.countries = pd.read_csv('../countries.csv')
        self.income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()

    def test_graph_income(self):

        graph_income(self.income, 2008, visualize=False)

        with self.assertRaises(TypeError):
            graph_income(self.income, 'year')
        with self.assertRaises(TypeError):
            graph_income(self.income, [])
        with self.assertRaises(ValueError):
            graph_income(self.income, 1600)
        with self.assertRaises(ValueError):
            graph_income(self.income, 2100.5)

    def test_merge_by_year(self):

        merge_by_year(self.income, self.countries, 2010)

        with self.assertRaises(TypeError):
            merge_by_year(self.income, self.countries)
        with self.assertRaises(TypeError):
            merge_by_year(self.income, [], 1900)
        with self.assertRaises(TypeError):
            merge_by_year(self.income, self.countries, 'year')
        with self.assertRaises(ValueError):
            merge_by_year(self.income, self.countries, 1200)
        with self.assertRaises(ValueError):
            merge_by_year(self.income, self.countries, 5000)
        with self.assertRaises(KeyError):
            merge_by_year(self.income, pd.DataFrame(np.ones(5)), 2000)
        with self.assertRaises(ValueError):
            merge_by_year(pd.DataFrame(np.ones(5)), self.countries, 2000)
        with self.assertRaises(ValueError):
            merge_by_year(self.countries, self.income, 2000)








