'''
@Author: Jingyi Su js5991 
@description: This contains the code for loading data and the methods to transform the data

Functions:
1. plot_income (year): it takes a parameter of year and plots a distribution of income for all nations for the given year
2. merge_by_year(year): it takes a parameter of year and merge the income and country information for the given year


'''
import pandas as pd
import matplotlib.pyplot as plt


#Question #1 load countries.csv
countries=pd.read_csv('../countries.csv')

#Question #2 load income per capita data
income=pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)

#Question #3 transform the income dataset so that the rows are years and columns are countries
income_transpose=income.transpose()
print('Head of the transformed income dataset:'+'\n')
print(income_transpose.head())

#Question #4 plot the income distribution of all nations with kde method for a given year
def plot_income(year):
    income_year=income_transpose.loc[1990].dropna()
    income_year.plot(kind='kde',xlim=[0,60000], title='Income Distribution of All Countries using KDE' )
    plt.show()
    

#Question #5 merge the income and country data for a given year
def merge_by_year(year):
    income_year=pd.DataFrame(income_transpose.loc[year].dropna())
    income_year.reset_index(level=0,inplace=True)
    income_year.columns=['Country','Income']
    merged_year=income_year.merge(countries, on="Country", how='inner')
    return merged_year

