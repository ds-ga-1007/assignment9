import matplotlib.pyplot as plt
import pandas as pd

# Question 1,2
countries = pd.read_csv('E:/DS1007/assignment9/countries.csv')
income = pd.read_excel('E:/DS1007/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
income = income.T


# Question 3
print(income.head())


# Question 4
def plot_hist(year):
    data = income.loc[year]
    plt.hist(data.dropna(), bins=20)


# Question 5
def merge_by_year(year):
    data = income.loc[year]
    result = countries.join(data, on='Country')
    return result


# Question 6
def boxplot(year,ax):
    result = merge_by_year(year)
    result.columns = ['Country', 'Region','Income']
    result.boxplot(column="Income", by="Region",fontsize=8, ax=ax)


def plot_hist_region(year,ax):
    result = merge_by_year(year)
    result.columns = ['Country', 'Region','Income']
    result.hist(column="Income", by="Region",xlabelsize=5,ylabelsize=5, ax=ax)
