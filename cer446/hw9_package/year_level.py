'''
Created on Dec 1, 2016

@author: Caroline
This module contains functions needed to create a plot for a particular year
These functions don't subdivide the data by region.
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import math
import load_data as l

def make_currency(amount, pos):
    'Turns float into a string representing currency, rounded to dollar'
    return '$' + '{:,d}'.format(int(amount))

def format_plot(data, subplotnum):
    '''Creates the distribution plot, formatting the bottom axis as currency'''
    
    ax = plt.subplot(subplotnum)

    s = pd.Series(data)
    s.hist(bins=50, alpha=0.75, color='#b3de69', normed=True, figsize = (10,6))
    s.plot(kind='kde', style='k--')

    formatter_x = FuncFormatter(make_currency)
    ax.xaxis.set_major_formatter(formatter_x)
    ax.set_xlabel('Income')
    plt.xlim([0, math.ceil(max(s) / 1000) * 1000])

def plot_distribution(year, data, subplotnum=111):
    '''Plots a distribution for a certain year for given income data'''
    data = data.loc[year, :].dropna().values
    format_plot(data, subplotnum)
    plt.title('Distribution of GDP per Capita, Year ' + str(year))
    plt.show()
    
def plot_requested_distributions(data):
    '''Asks the user for a year, outputs distribution graph for that year,
    repeats question until user types finish'''
    user_input = ''

    while user_input != 'finish':
        user_input = input('Year? ')
        if user_input != 'finish':
            try:
                year = validate_year(user_input)
                if year:
                    plot_distribution(year, l.income, 111)
            except Exception as ex:
                pass
                print (ex)

def validate_year(year):
    '''verifies that the year is valid for this dataset'''
    try:
        int(year)
        if int(year) < 1800:
            raise Exception ('The year must be 1800 or later')
        elif int(year) > 2012:
            raise Exception ('The year must be 2012 or earlier')
        elif int(year) >= 1800 and int(year) <= 2012:
            return int(year)
    except ValueError:
        print ('The year must be an integer')
