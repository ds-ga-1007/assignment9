import pandas as pd
import matplotlib.pyplot as plt

# This funciton will plot the distribution of income per persion for a given year. 
def displayIncome(year, data):
    plt.hist(data.loc[year].dropna().values)
    plt.title('Distribution of income per person across all countries in the world for year ' + str(year))
    plt.xlabel('Countries')
    plt.ylabel('Income per person')
    plt.show()

# This function will merge the data of income for a giving year and the data of 
# countries into a dataframe with three columns: Income, countries, region.
def merge_by_year(year, data, countries):
    income_of_year = pd.DataFrame(data.loc[year])
    income_of_year['Country'] = income_of_year.index
    ret_val = pd.merge(countries, income_of_year)
    ret_val.rename(columns = {year: 'Income'}, inplace = True)
    return ret_val