import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class YearOutOfRange(Exception):
    def __str__(self):
        return 'Year must be between 1800 and 2012.'
    
class YEAR():
    '''This class defines the parameters for a valid year. In particular, a year must be a four-digit
    integer between 1800 and 2012.'''
    def __init__(self, year_value):
        self.year_value = year_value
        if type(year_value) != int:
            raise TypeError ('Must be an integer')
        if year_value < 1800 or year_value > 2012:
            raise YearOutOfRange

def display_income_distribution(year, income_data):
    '''This function displays (and saves) a histogram illustrating the distribution of GDP per Capita across all the 
    countries of the world for a given year.'''
    try:
        year = YEAR(year).year_value  #test whether the argument is a valid year
        country_gdp_arr = income_data[year]
        HistGraph = country_gdp_arr.hist()
        plt.title('Distribution of GDP Per Capita in {0}'.format(year))
        plt.xlabel('GDP per Capita')
        plt.ylabel('Number of Countries')
        plt.savefig('Histogram of GDP Per Capita in {0}'.format(year))

        return HistGraph
    except YearOutOfRange:
        print('Enter a year between 1800 and 2012.')
        pass
    except TypeError:
        print('Must be an integer.')


def merge_by_year(year, income_data, country_data):
    '''This function merges the datasets "income" and "countries" for a given year, producing a new data 
    frame with the columns "Country", "Region", and "Income". Inner merge used.'''
    try:
        year = YEAR(year).year_value #test whether the argument is a valid year
        multi_year_df = pd.merge(income_data, country_data, left_index = True, right_on = 'Country', how = 'inner')
        final_df = pd.DataFrame(multi_year_df[['Country', 'Region']])
        final_df['Income'] = multi_year_df[year]
        return final_df
    except YearOutOfRange:
        print('Enter a year between 1800 and 2012.')
        pass
    except TypeError:
        print('Must be an integer.')       

    '''
    Author's note:
    I considered using a right-hand merge (so that all the records in the "countries" dataset were
    retained). However, there would have been many missing NaN values as a result. I thought about
    dealing with this issue by filling the NaN values with the mean income of a country's region (for 
    example, if South Korea had a NaN for income in 1800, we would fill the blank with the mean income of all countries
    in Asia in 1800). However, I thought this approach could potentially distort the eventual histograms
    and boxplots by artificially adding more records near the regional mean. As such, I decided to use 
    an inner merge.
    '''

class Graph():
    def __init__(self, attribute, grouping_feature, year, data):
        '''This class defines the variables and tools used to build a histogram or boxplot.
        @param "attribute": Feature whose distribution we'll be visualizing. (e.g. "Income")
        @param "grouping_feature": categorical feature used to place countries into "bins". (e.g. "Region")
        @param "year": if many columns have the same attribute (e.g., 200 columns for "Income"), "year" is used to select a particular column.        
        @param "data": dataset that includes "grouping_feature" and "attribute" (e.g. merge_by_year(year))
        '''
        self.year = YEAR(year).year_value
        self.data = data
        self.attribute = attribute 
        self.grouping_feature = grouping_feature
      
    def create_histograms(self):
        '''Method to proudce histograms.'''
        HistPlot = self.data.hist(column=self.attribute, by=self.grouping_feature, figsize = (10,15))
        plt.suptitle('Distribution of Incomes by {0} in {1}'.format(self.grouping_feature, self.year), y = 0.95, fontsize = 20)
        plt.savefig('Histograms of GDP by {0} in {1}'.format(self.grouping_feature, self.year))
        return HistPlot
    
    def create_boxplots(self):
        '''Method to produce boxplots.'''
        BoxGram = self.data.boxplot(column=self.attribute, by=self.grouping_feature, figsize=(12,8))
        plt.title('Distribution of Incomes by {0} in {1}'.format(self.grouping_feature, self.year), fontsize = 15)
        plt.ylabel('Income')
        plt.suptitle('')
        plt.savefig('Boxplots of GDP by {0} in {1}'.format(self.grouping_feature, self.year))
        plt.axis([0, 7, 0, 100000])
        return BoxGram

