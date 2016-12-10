'''
This module is for loading, shaping and pre-processing data set.

Created on Dec 3, 2016
@author: Zhiqi Guo(zg475)
@email: zg475@nyu.edu
'''
import pandas as pd

'''dataset loading'''
def load_data(dataset):
    if dataset == 'countries':
        countries = pd.read_csv('../countries.csv')
        return countries
    if dataset == 'income':
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx')
        
        '''dataset re-shaping'''    
        income = income.T
        new_header = income.iloc[0]                  #grab the first row for the header   
        income = income[1:]                          #take the data less the header row
        income = income.rename(columns = new_header) #set the header row as the df header
        return income
    