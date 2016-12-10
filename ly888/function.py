import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_income(path):
    #Read the income data from path
    income=pd.read_excel(path,index_col='gdp pc test')
    #Transpose income data
    income_tran=income.transpose()
    return income_tran
  

def load_country(path):
    #Read the country data from path
    country=pd.read_csv(path)
    return country 


def load_income_head(path):
    #Read the income data from path and show the head
    income=pd.read_excel(path,index_col='gdp pc test')
    income_tran=income.transpose()
    print(income_tran.head())


def hist_income(income,year):
    #Input income data and year, than return income histogram for that year
    #If the input year is not valid, a warning "input is not valid" will appear
    if year>=1800 and year<=2012:
        income_year_all=income.ix[year]
        #Drop the missing value
        income_year=pd.DataFrame(income_year_all).dropna()
        income_year.columns=['Income']
        #Define the meaning of x-axis, y-axis and then plot histogram
        income_year['Income'].hist(bins=50)
        plt.title("The income histogram for year %d" %year)
        plt.xlabel("Income")
        plt.ylabel("Frequency")
        plt.show()
    else:
        return("The input year is not valid")


def merge_by_year(year):
     #Read the data
    income=load_income('e:/income.xlsx')
    country=load_country('e:/countries.csv')
    #Find the income given input year
    income_year_all=income.ix[year]
    #Drop the missing value
    income_year=pd.DataFrame(income_year_all).dropna()
    #Rename the index and columns
    income_year.columns=['Income']
    income_year['Country']=income_year.index
    #Merge data
    df_income_year=pd.merge(country,income_year,on='Country',how='left')
    return(df_income_year)


