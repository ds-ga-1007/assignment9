import unittest
from EconVisualizer import *

class TestEconVisualizer(unittest.TestCase):
    """
    Economic Visualizer test cases
    """
    def setUp(self):

        self.countries = pd.read_csv('../countries.csv')
        self.income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()

        self.merged_df = merge_by_year(self.income, self.countries, 2010)

    def test_econ_visualizer_constructor(self):

        ev = EconVisualizer()
        self.assertEqual(ev.income, None)
        self.assertEqual(ev.countries, None)

        ev = EconVisualizer(income=self.income, countries=self.countries)
        self.assertEqual(ev.income.shape, self.income.shape)
        self.assertEqual(ev.countries.shape, self.countries.shape)

        with self.assertRaises(TypeError):
            EconVisualizer(income=12, countries=self.countries)
        with self.assertRaises(TypeError):
            EconVisualizer(income=self.income, countries=[])

    def test_graph_years(self):

        ev = EconVisualizer()
        with self.assertRaises(TypeError):
            ev.graph_years()
        with self.assertRaises(ValueError):
            ev.graph_years(1900)
        with self.assertRaises(ValueError):
            ev.graph_years([1900, 1200, 1902])

    def test_hist(self):

        ev = EconVisualizer(self.income, self.countries)
        ev._hist(self.merged_df, visualize=False)

        ev = EconVisualizer()
        ev._hist(self.merged_df, visualize=False)

        with self.assertRaises(TypeError):
            ev._hist(10, visualize=False)
        with self.assertRaises(KeyError):
            ev._hist(df=self.countries, visualize=False)

    def test_bar(self):

        ev = EconVisualizer(self.income, self.countries)
        ev._box(self.merged_df, visualize=False)

        ev = EconVisualizer()
        ev._box(self.merged_df, visualize=False)

        with self.assertRaises(TypeError):
            ev._box(10, visualize=False)
        with self.assertRaises(KeyError):
            ev._box(df=self.countries, visualize=False)











