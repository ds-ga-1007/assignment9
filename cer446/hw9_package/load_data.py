'''
Created on Dec 1, 2016

@author: Caroline
This module loads the data
'''
import pandas as pd

def load(filename):
    '''Loads the file and processes it'''
    file = pd.read_excel(filename)
    file = file.T
    file.columns = file.iloc[0, :]
    file.drop(file.index[0], axis=0, inplace = True)
    return file

income = load('indicator gapminder gdp_per_capita_ppp.xlsx')

countries = pd.read_csv('countries.csv')