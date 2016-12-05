# Solution for DS-GA 1007 Assignment#9
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

import pandas as pd
import matplotlib.pyplot as plt
import seaborn


class IncomeData:
    def __init__(self, income, countries):
        """Initialization for the class"""
        self.income = income
        self.countries = countries

    def dist_income_per_person(self, year):
        """show the histogram of the personal income for a given year"""
        income_count = self.income.ix[year]
        plt.figure()
        income_count.plot(kind="hist")
        plt.show()

    def merge_by_year(self, year):
        """get out the row from income for a given year, and merge with the countries dataset"""
        data = {
            "Country": self.income.columns,
            "Income": self.income.ix[year]
        }
        data_df = pd.DataFrame(data)
        # the merge operation
        result = pd.merge(self.countries, data_df, on="Country")
        return result

    def explore_income(self, year):
        """explore the income data, save the plots for the income for each region for the given year"""
        income_data = self.merge_by_year(year)
        regions = income_data["Region"].unique()
        result = {}
        # for each region, save one histogram and one boxplot
        # note that you should create a folder named "fig"
        for region in regions:
            result[region] = income_data[income_data["Region"] == region]
            result[region].plot(kind="hist")
            plt.savefig("fig/hist_" + region + "_" + str(year) + ".png")
            result[region].plot(kind="box")
            plt.savefig("fig/box_" + region + "_" + str(year) + ".png")
