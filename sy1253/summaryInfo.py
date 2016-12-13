# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 01:38:39 2016

@author: kevinyan
"""
import pandas as pd
import matplotlib.pyplot as plt

def mergeByYear(year, income, countries):
    """
    this function merges the countries and income data sets for any given year
    """
    incomeSingle = pd.DataFrame(income.loc[year]).reset_index()
    #change the category name is the previous file
    incomeSingle = incomeSingle.rename(columns = {'gdp pc test':'Country'})
    incomeSingle = incomeSingle.rename(columns = {year:'Income'})
    mergedYear = pd.merge(countries, incomeSingle, on='Country')
    return mergedYear


def displaySummary(year, income):
    """
    this function uses histogram to present the distribution of income per person across all countries
    """
    plt.hist(income.loc[year].dropna())
    plt.title("distribution of income per person across all countries in the world in " + str(year))
    plt.xlabel("income per person")
    plt.ylabel("number of countries")
    plt.show()

 





