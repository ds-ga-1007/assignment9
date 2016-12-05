"""
This module was used to load data and transform data

Created on 2016/12/03
Version: 1.0
@author: Sheng Liu
ShengLiu Copyright 2016-2017
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
# This part is loading countries and income data sets
print('>>>>>>>Loading Data.........')
countries = pd.read_csv('../countries.csv')
income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',index_col = 0)
income = income.T
print(income.head(5))


def Display_GDP_All_Countries(year):
	'''
	This function is to plot the distribution of income per person for given year
	'''
	df = income.loc[year]
	clean_df = df[~(df.isnull())]
	clean_df.hist(bins = 20)
	plt.xlabel('Income per person across all countries')
	plt.ylabel('Count')
	plt.title('Distribution of per person income for year ' + str(year))
	plt.show()

def merge_by_year(year):
	'''
	This function is to merge countries and income data sets for a given year
	'''
	df = income.loc[year]
	Income_For_Year = pd.DataFrame({'Country': df.index.values,'Income': df.values})
	return pd.merge(countries,Income_For_Year, on = 'Country')


