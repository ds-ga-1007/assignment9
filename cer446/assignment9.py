'''
Created on Dec 1, 2016

@author: Caroline Roper, cer446

This program loads two data sets: (1) GDP per capita data and (2) a list of countries and their regions.
It asks the user to input a year between 1800 and 2015 and plots the distribution of
GDP per capita over all countries that year.
It also analyzes the distributions at a regional level for the years 2007-2012
and outputs two files for each year - one with a boxplot of each region and one with a
histogram and density graph for each region.
'''

import sys

sys.path.append('hw9_package')

import analysis_class as ac
import year_level as yr
import load_data as l

print (l.income.head())
                
yr.plot_requested_distributions(l.income)

years = [2007, 2008, 2009, 2010, 2011, 2012]
analyses = []

for i in range(0, len(years)):
    analyses.append(ac.Analysis(years[i], l.income))
    analyses[i].create_regional_boxplot()
    analyses[i].plot_all_regional_distributions()
    
print('analysis of year 2007 - 2012 saved')