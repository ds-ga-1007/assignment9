"""
Unit tests for income_analysis module.
For running the unit tests use the command 'python -m unittest discover' in the netid (ak6179) directory.
The command will automatically discover unit tests and will run them.
I had previously added a main function allowing standalone running of tests. I have removed that
functionality because you can't do relative imports using that procedure.
Eg: The statement from ..simulation import * would be invalid. There is a workaround to this
problem as indicated by this answer: http://stackoverflow.com/questions/16981921/relative-imports-in-python-3 .
I went through a number of online resources and unit tests implementation in python (eg: sklearn) and
the standard way to run tests is using the command 'python -m unittest discover'.
Note that you have to run the tests inside the 'ak6179' directory and you need to have
the test files used below at the relative paths used below.
"""
import unittest
from income_analysis import *


class IncomeAnalysisTest(unittest.TestCase):
    @staticmethod
    def _read_test_data(countries_path, gdp_path):
        """
        Read test data. Throws exception if files not found.
        """
        countries = pd.read_csv(countries_path)
        country_gdp_per_capita = pd.read_excel(gdp_path)
        country_gdp_per_capita = country_gdp_per_capita.set_index('gdp pc test').T
        return countries, country_gdp_per_capita

    def test_constructor(self):
        """
        Test the IncomeAnalysis constructor.
        Data is read in every test because the tests are supposed to be independent.
        """
        countries, country_gdp_per_capita = self._read_test_data(
            "../countries.csv", "../indicator gapminder gdp_per_capita_ppp.xlsx")
        _ = IncomeAnalysis(countries, country_gdp_per_capita)
        with self.assertRaises(ValueError):
            _ = IncomeAnalysis(pd.DataFrame(), [23])
        with self.assertRaises(ValueError):
            _ = IncomeAnalysis([42], pd.DataFrame())

    def test_plot_histogram(self):
        """
        Testing histogram plotting. Displaying the histogram is turned off.
        Data is read in every test because the tests are supposed to be independent.
        """
        countries, country_gdp_per_capita = self._read_test_data(
            "../countries.csv", "../indicator gapminder gdp_per_capita_ppp.xlsx")
        analysis = IncomeAnalysis(countries, country_gdp_per_capita)
        analysis.plot_histogram_income_year(1992, display_plot=False)
        with self.assertRaises(ValueError):
            analysis.plot_histogram_income_year(1700, display_plot=False)
        with self.assertRaises(ValueError):
            analysis.plot_histogram_income_year("something", display_plot=False)
        with self.assertRaises(ValueError):
            analysis.plot_histogram_income_year(-100, display_plot=False)

    def test_merge_by_year(self):
        """
        Test merge_by_year method.
        Data is read in every test because the tests are supposed to be independent.
        """
        countries, country_gdp_per_capita = self._read_test_data(
            "../countries.csv", "../indicator gapminder gdp_per_capita_ppp.xlsx")
        analysis = IncomeAnalysis(countries, country_gdp_per_capita)
        _ = analysis.merge_by_year(1820)
        _ = analysis.merge_by_year(1910)
        with self.assertRaises(ValueError):
            _ = analysis.merge_by_year(1000)
        with self.assertRaises(ValueError):
            _ = analysis.merge_by_year(5000)
        with self.assertRaises(ValueError):
            _ = analysis.merge_by_year('text')
        with self.assertRaises(ValueError):
            _ = analysis.merge_by_year('2005text')

    def test_plot_regions_histogram(self):
        """
        Test plot_regions_histogram method.
        Data is read in every test because the tests are supposed to be independent.
        """
        countries, country_gdp_per_capita = self._read_test_data(
            "../countries.csv", "../indicator gapminder gdp_per_capita_ppp.xlsx")
        analysis = IncomeAnalysis(countries, country_gdp_per_capita)
        analysis.plot_regions_histogram([2000, 2005], save_figs=False)
        analysis.plot_regions_histogram([1810, 1910], save_figs=False)
        with self.assertRaises(ValueError):
            analysis.plot_regions_histogram([1500], save_figs=False)
        with self.assertRaises(ValueError):
            analysis.plot_regions_histogram(['text1', 'text2'], save_figs=False)

    def test_plt_regions_boxplot(self):
        """
        Test plot_regions_boxplot method.
        Data is read in every test because the tests are supposed to be independent.
        """
        countries, country_gdp_per_capita = self._read_test_data(
            "../countries.csv", "../indicator gapminder gdp_per_capita_ppp.xlsx")
        analysis = IncomeAnalysis(countries, country_gdp_per_capita)
        analysis.plot_regions_boxplot([2000, 2005], save_figs=False)
        analysis.plot_regions_boxplot([2000, 2005], save_figs=False)
        with self.assertRaises(ValueError):
            analysis.plot_regions_boxplot([1500], save_figs=False)
        with self.assertRaises(ValueError):
            analysis.plot_regions_boxplot(['text1', 'text2'], save_figs=False)