
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def graph_income(income, year):
    """
    Graphs income for a given year in a histogram
    :param income: pandas.DataFrame of income values.
    :param year: int-like. used as row index in income.
    :return: None. draws matplotlib.pyplot graph and shows figure.
    """
    try:
        year = int(year)
    except ValueError:
        raise TypeError("year must be numeric")

    if not year in income.index.values:
        raise ValueError("year must be between " + str(np.min(income.index.values))
                         + " and " + str(np.min(income.index.values)))

    incomes_at_year = income.ix[year ,:]
    incomes_at_year.hist()
    plt.show()

def merge_by_year(income, countries, year):
    """
    Merge income and countries to a single dataframe of country, region and income for a given year
    :param income: A pandas.DataFrame of incomes.
    :param countries: a pandas.DataFrame of regions and countries
    :param year: int-like. This shall be used as the year for the income DataFrame to get incomes from
    :return: pandas.DataFrame containing Country and Region from countries, and incomes for a year from
             the income DataFrame
    """

    if not isinstance(income, pd.DataFrame) or not isinstance(countries, pd.DataFrame):
        raise TypeError("income and countries must be pandas DataFrames")
    try:
        year = int(year)
    except ValueError:
        raise TypeError("year must be numeric")

    if not year in income.index.values:
        raise ValueError("year must be between " + str(np.min(income.index.values))
                         + " and " + str(np.min(income.index.values)))

    try:
        merged_df = countries.merge(income.transpose().ix[: ,[year]], left_on = "Country", right_index = True)
    except KeyError:
        raise KeyError("countries must have Country Column")

    merged_df.columns = ["Country", "Region", "income"]
    merged_df.year = year

    return merged_df