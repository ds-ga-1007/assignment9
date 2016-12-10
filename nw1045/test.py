'''
Created on Nov 28, 2016

@author: apple
'''
import pandas as pd
DataPath = 'dataset/'
countries = pd.read_csv(DataPath+'countries.csv',header=0)
income = pd.read_excel(DataPath+'indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data', header=0,index_col=0)
print(sum(income.isnull()))
print(1)