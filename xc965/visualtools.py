'''
This module serves to visualize the distribution of GDP per capita
for given years by regional settings.
Regional colors in different visualizations are correspondingly matched.

@author: Xianzhi Cao (xc965)
'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import re
from dataprep import *
from UserError import *


class visualization(object):
    '''
    Visualize the distribution of the given data set
    in chosen year with histograms and boxplots.
    '''
    def __init__(self, year):
        self.year = year
        self.df = merge_by_year(self.year)  # merged DataFrame
        self.region_ls = self.df.Region.unique().tolist()  # the list of regions


    def regional_incomes(self):
        '''put all regions' incomes into a list'''
        regions = []
        for region in self.region_ls:
            regions.append(self.df[self.df.Region == region].Income)
        return regions


    def histogram_plot(self):
        '''
        Plot histograms, both stacked and unstacked, by regions for chosen year;
        Save as png files.
        '''

        # use subplots to present histograms
        fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(15, 6))

        # plot the unstacked histogram in the first subplot
        # x-axis and y-axis are both customized
        ax0.hist(self.regional_incomes(), bins=10, range=(0, 100000),
                label=self.region_ls, alpha=0.8)
        ax0.set_xlabel('GDP Per Capita [in US Dollar]')
        ax0.set_ylabel('Country Counts')
        ax0.set_xticks(range(0, 100001, 10000))
        ax0.set_xticklabels(str(int(i/1000))+'k' for i in range(0, 100001, 10000))
        ax0.set_title('Histogram (Unstacked) of GDP Per Capita - All Regions in {}'.format(self.year))
        ax0.legend()

        # plot the stacked histogram in the second subplot
        # x-axis and y-axis are both customized
        ax1.hist(self.regional_incomes(), bins=10, histtype='barstacked', range=(0, 100000),
                label=self.region_ls, alpha=0.8)
        ax1.set_xlabel('GDP Per Capita [in US Dollar]')
        ax1.set_ylabel('Country Counts')
        ax1.set_xticks(range(0, 100001, 10000))
        ax1.set_xticklabels(str(int(i/1000))+'k' for i in range(0, 100001, 10000))
        ax1.set_yticks(range(0, 121, 20))
        ax1.set_yticklabels(i for i in range(0, 121, 20))
        ax1.set_title('Histogram (Stacked) of GDP Per Capita - All Regions in {}'.format(self.year))
        ax1.legend()

        # save the histogram of the chosen  year into a png file
        fig.savefig('Histogram of Regional Incomes in {}.png'.format(self.year))


    def boxplot_plot(self):
        '''
        Plot boxplots by regions for a chosen year;
        Both axes and title are customized.
        Save as png files.
        '''
        fig = plt.figure(figsize=(7,5))

        # use seaborn to present better visualization of boxplots
        sns.boxplot(x="Region", y="Income", data=self.df, width=0.4, linewidth=0.8, notch=True)
        plt.ylabel('GDP Per Capita [in US Dollar]')
        plt.xticks(rotation = -30)
        plt.yticks(range(0, 100001, 20000), ['0', '20k', '40k', '60k', '80k', '100k'])
        plt.title('Boxplot of GDP Per Capita - All Regions in {}'.format(self.year))

        # save the boxplot as a png file
        fig.tight_layout()
        fig.savefig('Boxplot of Regional Incomes in {}.png'.format(self.year))


def country_income_display(year, df):
    '''
    Take the parameter of year and data set;
    Display the distribution of income per person across all countries,
    in both hisgrams and kde curves.
    '''

    if year == '':
        raise EmptyInputError
    else:
        year = year.replace(' ', '')
        if not re.match(r'(\d{4})', year):
            raise InputFormatError
        elif int(year) < 1800 or int(year) > 2012:
            raise InputValueError
        else:
            year = int(year)

    print('Please close the graph window to continue.')

    income_by_year = df.loc[year, :].dropna()  # type: pandas Series
    upper = income_by_year.max()

    #  Histogram of gdp per capita ppp distribution across all countries
    fig1 = plt.subplot(211)
    income_by_year.hist(bins=20, range=(0, upper+1), alpha=0.4, color='navy')
    plt.ylabel('Country Counts')
    plt.title('Histogram: Country Income Distribution in {}'.format(year))

    #  Density in perventile of kde Histogram of gdp per capita ppp distribution across all countries
    fig2 = plt.subplot(212)
    income_by_year.hist(bins=20, normed=True, range=(0, upper+1), alpha=0.2, color='navy')
    income_by_year.plot(kind='kde', style='k--').set(xlim=(0, upper))
    plt.yticks(fig2.get_yticks(), (fig2.get_yticks() * 100))  # yticks in percentiles
    plt.xlabel('Country GDP Per Capita [in US Dollar]')
    plt.ylabel('Density [%]')

    plt.show()
