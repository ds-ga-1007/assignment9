
from unittest import TestCase
from plotter import merge_year
import pandas as PD


class TestMerge(TestCase):
    def setUp(self):
        # Prepare our own copy of dataset
        countries = PD.read_csv("../countries.csv")
        self.income = PD.read_excel(
                "../indicator gapminder gdp_per_capita_ppp.xlsx",
                index_col=0
                ).T
        self.ctr_region_map = dict(zip(countries.Country, countries.Region))

    def test_merge(self):
        # Exhaustively test every year.
        for year in self.income.index:
            merged = merge_year(year)
            for ctr, region, gdp in merged.values:
                self.assertEqual(self.ctr_region_map[ctr], region)
                self.assertEqual(self.income.loc[year, ctr], gdp)
