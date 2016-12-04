'''
Created on Dec 3, 2016

@author: twff
'''
import pandas as pd
import matplotlib.pyplot as plt


def incomeDistribution(df, year, bins=50):
    '''
    Graphically display the distribution of income per person across all countries 
    in the world for the given year. Choose the histogram to display this 
    information.
    '''
    fig = plt.figure()
    df[year].dropna().hist(bins=bins)
    plt.xlabel('income per person')
    plt.ylabel('Income count')
    plt.title('distribution of income per person across all countries in the world in the year '+str(year))
    plt.show()
    fig.savefig('Distribution of Income '+str(year)+'.pdf')
    plt.close()

def merge_by_year(countries, income, year=2012):
    '''
    Merge the countries and income data sets for any given year. 
    The result is a DataFrame with three columns titled Country, Region, and Income.

    '''
    year_df = pd.DataFrame(income[year])
    income.rename(columns={'gdp pc test' : 'Country'})
    mdf = pd.merge(countries, year_df, left_index=True, right_index = True).rename(columns= {year:'Income'})
    return mdf

    
class tools:
    '''
    Use histograms and boxplots to graphically explore the distribution of the income 
    per person by region data set for a given year. 
    Save these graphs to individual files.
    '''
    def __init__(self, bins =20):
        self.bins = bins
    
    def histogram_by_region(self, mdf, filename = None, year=2012):
        region = mdf.groupby('Region').Income.apply(list)
        values = list(region.values)
        label = list(region.index)
        
        plt.hist(values, bins = self.bins, label=label)
        plt.xlabel('income per person in different countries')
        plt.ylabel('Income count')
        plt.title('histograms of the income per person by region in the year '+str(year))
        plt.legend(loc=1)
        
        if filename == None:
            plt.show()
        else:
            plt.savefig(filename)
        
        plt.close()
        
    def boxplot_by_region(self, mdf, filename = None, year=2012):
        
        mdf.boxplot('Income', by = 'Region')
        plt.xlabel('income per person in different countries')
        plt.ylabel('Income count')
        plt.title('boxplot of the income per person by region in the year '+str(year))
        
        if filename == None:
            plt.show()
        else:
            plt.savefig(filename)
        
        plt.close()