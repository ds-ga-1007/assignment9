'''
Created on Dec 5, 2016

@author: Yovela
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt


countries = pd.read_csv("countries.csv", sep=',')
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0).transpose()

def income_distribution(year, income):
    
    '''
    graphically display the distribution of income per person across all countries for the given year
    
    Input: a DataFrame and a given year
    Output: histogram
    '''
    income.loc[year,:].hist()
    plt.xlabel("Income per person")
    plt.ylabel("Number of Countries")
    plt.title("Distribution of Income per person across all countries")
    plt.show()
    return
    
def merge_by_year(year):
    
    '''
    merge the countries and income data sets for any given year
    
    Input: two DataFrames and a given year
    Output: a new DataFrame
    
    '''
    df1 = pd.concat([countries["Country"], countries["Region"]], axis = 1)
    df2 = income.loc[year,:].to_frame("Income")
    merged = pd.merge(df1, df2, left_on  = "Country", right_index = True)
    return merged

