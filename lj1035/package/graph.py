import pandas as pd
import matplotlib.pyplot as plt
import os


# Use absolute path to make sure the data files can be correctly found.
this_dir = os.path.dirname(os.path.abspath(__file__))
my_path = os.path.join(this_dir, os.pardir, os.pardir)
countries = pd.read_csv(my_path + '/countries.csv')
income = pd.read_excel(my_path + '/indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0).transpose()
print(income.head())


def plot_gdp(year):
    """
    This function takes year as its argument and uses the histogram to display the distribution of income per person
    across all countries in the world for a given year.
    """
    plt.hist(income.loc[year].dropna(), bins=20)
    plt.show()
    plt.close()


def merge_by_year(year):
    """
    This function takes year as its argument, merges the countries and income data sets for any given year, and
    finally returns a merged DataFrame.
    """
    income_by_year_df = pd.DataFrame(income.ix[year])
    income_by_year_df.reset_index(inplace=True)
    income_by_year_df.rename(columns={'gdp pc test': 'Country', year: 'Income'}, inplace=True)
    merge_df = pd.merge(countries, income_by_year_df, on='Country')
    return merge_df


# The GraphicalAnalysis class graphically explore the distribution of income by region using histogram and boxplot.
class GraphicalAnalysis(object):

    def __init__(self, dataset, year):
        """
        This is the constructor of the GraphicalAnalysis class.
        """
        self.dataset = dataset
        self.year = year

    def histogram_gdp_by_region(self):
        """
        This method plots this histogram to display the distribution of income by region and saves the graph to a
        PDF file.
        """
        gdp_by_year = self.dataset.dropna()
        gdp_by_year.hist(by='Region', figsize=(12, 10), color='b', bins=15)
        plt.savefig('histogram_' + str(self.year) + '_by_region.pdf')
        plt.close()

    def boxplot_gdp_by_region(self):
        """
        This method draws the boxplot to display the distribution of income by region and saves the graph to a PDF
        file.
        """
        gdp_by_year = self.dataset.dropna()
        gdp_by_year.boxplot(by='Region')
        plt.savefig('boxplot_' + str(self.year) + '_by_region.pdf')
        plt.close()
