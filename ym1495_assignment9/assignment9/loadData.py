'''
Created on Dec 5, 2016

@author: muriel820
'''

import pandas as pd
import sys


class loadData():
    def __init__(self):
        self.countries = pd.read_csv('countries.csv')
        self.income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').transpose()
        self.income.columns = [self.income.ix[0]]
        self.income = self.income.drop(['gdp pc test'],axis=0)
    def __repr__(self):
        print (self.income.head())