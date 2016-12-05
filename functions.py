import pandas as pd
import matplotlib.pyplot as plt

'''The self-defined functions utilize pandas and matplotlib to clean data and facilitate data visualiztions.'''

def load_data():
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col= 0)
    print(income.T.head())
    return countries, income

def display(year):
    plt.xlabel('Income/person of Each Country')
    plt.ylabel('Number of Countries')
    plt.hist(income[year].dropna(), bins=20)
    plt.show()
    plt.close()

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col= 0)
def merge_by_year(year):
    income_given_year = income[year]
    income_given_year.name = 'Income'
    merged_df_year = countries.join(income_given_year, on='Country').dropna()
    return merged_df_year
