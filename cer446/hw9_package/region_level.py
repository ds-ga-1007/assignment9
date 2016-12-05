'''
Created on Dec 1, 2016

@author: Caroline
This module contains functions needed to create a plot for a particular year subdivided by region
'''

import matplotlib.pyplot as plt
import year_level as yr
import pandas as pd
import load_data as l

def merge_by_year(year, data):
    '''Merges the country data set with the given data set based on the country name'''
    merged = pd.DataFrame(data.loc[year, :].T.index)
    merged.columns = ['Country']
    merged['Income']  = data.loc[year, :].T.values
    merged = pd.merge(merged, l.countries, on='Country')
    merged = merged[['Country', 'Region', 'Income']]
    return merged

def plot_regional_distribution(year, region, subplotnum=111):
    '''Plots the distribution of a certain region within a certain year'''
    income_for_year = merge_by_year(year, l.income)
    data = income_for_year[income_for_year['Region'] == region]['Income']
    yr.format_plot(data, subplotnum)
    plt.title('Distribution of GDP per Capita for Countries in ' + str(region) + ', ' + str(year))

    