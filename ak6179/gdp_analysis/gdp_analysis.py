from . import gdp_analysis_utils as utils
import pandas as pd
import matplotlib.pyplot as plt


class Analysis(object):
    def __init__(self, countries, country_gdp_per_capita):
        self.countries = countries
        self.country_gdp_per_capita = country_gdp_per_capita

    def plot_histogram_income_year(self, year, bins=50):
        """
        Plot histogram for incomes in the :param year.
        The histogram is displayed on screen. To move ahead the histogram window should be closed.
        :param year
        :param bins
        """
        year = utils.get_int_year(year)
        if year not in self.country_gdp_per_capita.index:
            raise ValueError("Year \'%s\' not present in the dataset." % str(year))
        incomes = self.country_gdp_per_capita.loc[year]
        incomes = incomes.dropna()
        plt.hist(incomes, bins=bins)
        plt.xlabel('income per person')
        plt.ylabel('number of countries')
        plt.title('Histogram of income per person vs number of countries')
        plt.show()

    def merge_by_year(self, year):
        
