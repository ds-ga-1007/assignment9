"""
Date: Dec 5, 2016
Author: Chloe Meng(lm3226)
Description: This program intends to generate a histogram and a boxplot of countries' GDP per capita for a given year
"""

from read_and_display_GDP import *
import pandas as pd
import matplotlib.pyplot as plt

class data_analysis_graphs():
    def __init__(self, year):
        self.year = year
        self.merged_GDP = data_analysis_graphs.merge_by_year(year)

    def merge_by_year(year):
        #This function merges the countries and income data sets for any given year.
        countries = read_and_display_GDP.read_dataset('countries', False)
        income = read_and_display_GDP.read_dataset('income', False)
        column_names = ['Country','Region','Income']
        merged_GDP = countries.merge(income.take([income.columns.get_loc(year)], axis=1), how='inner', left_on='Country', right_index=True)
        merged_GDP.columns = column_names
        return merged_GDP

    def generate_merged_income_histogram(self):
        #This function generates histogram of income per capita for different regions for a given year.
        fig, ax = plt.subplots(figsize=(10,10))
        self.merged_GDP['Income'].dropna().hist()
        ax.set_title('Histogram of income for '+str(self.year))
        ax.set_xlabel('Income per capita')
        ax.set_ylabel('Number of Countries')
        fig.savefig('Histogram of merged income per capita for '+str(self.year)+'.pdf')

    def generate_merged_income_boxplot(self):
        #This function generates boxplot of income per capita for different regions for a given year.
        fig, ax = plt.subplots(figsize=(10,10))
        self.merged_GDP.boxplot('Income', by='Region', ax=ax)
        ax.set_title('Boxplot of merged income per capita for '+str(self.year))
        fig.savefig('Boxplot of merged income per capita for year '+str(self.year)+'.pdf')
