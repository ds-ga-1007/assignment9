import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0).transpose()


def income_distribution(year):
    """
    Produce a plot include income distribution for certain year.
    input: year
    output: histogram
    """
    income_year = income.loc[year]
    plt.hist(income_year.dropna())
    plt.show()


def merge_by_year(year):
    """
    Merge countries and income data set by column 'Country'.
    :param year:
    :return merged data set:
    """
    year_data = income.loc[year].to_frame('Income')
    year_data.index.names = ['Country']
    result = countries.join(year_data, on=['Country'], how='right', lsuffix='_x')
    return result


class Exploratory_Data_Analysis:
    """
    The class constructs two functions that build boxplots and histogram for different region.
    """
    def boxplots(self,year):
        """
        :param year:
        :return: a boxplot names:'Boxplots of Regions at year of year.pdf'
        """
        data = merge_by_year(year)
        data.boxplot('Income', by='Region')
        plt.savefig('Boxplots of Regions at year of' + str(year) + '.pdf')
        plt.close()

    def histogram(self,year):
        """

        :param year:
        :return: a histogram names: 'Histogram of Regions at year of year.pdf'
        """
        data = merge_by_year(year)
        data.hist('Income', by='Region')
        plt.savefig('Histograms of Regions at year of' + str(year) + '.pdf')
        plt.close()
