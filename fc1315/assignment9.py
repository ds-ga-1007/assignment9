'''
Created on Dec 3, 2016
@author: Fanglin Chen
First, this program loads the countries and income data sets. 
Next, it transforms the income data set to have years as the rows and countries as the columns, 
and shows the head of the new data set.
Then, it asks the user to enter a year between 1800 and 2012, and displays the distribution 
of income per person across all countries in the world for the given year, 
until the string ‘finish’ is entered.
Finally, it displays the distribution of income per person by region for the years 2007-2012.
'''

import pandas as p
import matplotlib.pyplot as plt
from Region_dis import *

# Load data set
countries = p.read_csv('../countries.csv')
income = p.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 'gdp pc test', sheetname='Data')

# Transform the income data set to have years as the rows and countries as the columns, 
# then show the head of this data set.
transformed_income = income.transpose()
print(transformed_income.head(n = 5))

def dis(data, year):
    '''
    This function uses histograms to graphically display the distribution of 
    income per person across all countries in the world for a given year.
    '''
    data.hist(column = year)
    plt.show()

def merge_by_year(year):
    '''
    This function merges the countries and income data sets for a given year.
    '''
    merge_data = p.merge(countries, income, left_on = 'Country', right_index = True)[['Country', 'Region', year]]
    return merge_data.rename(columns={year: 'Income'})

while True:
    try:
        year_input = input('Please enter a year:\n> ')   # Ask the user to enter a year
        if year_input == 'finish':   # Continue until the string ‘finish’ is entered    
            break
        else:
            year = int(year_input)
            if not 1800 <= year <= 2012:
                raise InputError(year_input, 'Invalid input')
            dis(income, year)   # Display the graph using the dis function 
            continue
    except InputError:   # Handle invalid user input
        print('The input is not a valid year')
    except ValueError:
        print('Invalid value')
    except EOFError:
        print('This is the end of file')
    except KeyboardInterrupt:
        print('You have hit the interrupt key')

# Use the Region_dis class to generate graphs for the years 2007-2012
for year in range (2007, 2013):
    merge_data = Region_dis()
    merge_data.histogram(merge_by_year(year))
    plt.savefig('Histogram_' + str(year) + '.pdf')
    merge_data.boxplot(merge_by_year(year))
    plt.savefig('Boxplot_' + str(year) + '.pdf')
    
if __name__ == '__main__':
    pass