'''
Created on Dec 4, 2016

@author: Christine
'''
import pandas as pd
import matplotlib.pyplot as plt

'''
Function that graphically displays the distribution of income per person across all
countries in the world for the given year
'''
def distr_income(income,year):
    plt.hist(income.loc[year].dropna())
    plt.xlabel('Income per person')
    plt.ylabel('Number of countries')
    plt.title('Distribution of income per person across all countries in the world for year' + str(year))
    plt.show()
    plt.close()
    
'''
Provide a function called merge_by_year(year) to merge the countries and income
data sets for any given year.
'''
def merge_by_year(year,income,countries):
    inc = pd.DataFrame(income.loc[year]).reset_index()
    inc = inc.rename(columns = {'gdp pc test':'Country'})
    inc = inc.rename(columns = {year:'Income'})
    merged_df_year = pd.merge(countries,inc,on='Country')
    return(merged_df_year)

class InvalidInput(Exception):
    def __repr__(self):
        return "Invalid Year Input!\n"

'''
A class that uses exploratory data analysis tools (histograms and boxplots) to
graphically explore the distribution of the income per person by region data set for a given year. 
Save these graphs to individual files.
'''
class analysis:
    def __init__(self, merged_df, year):
        self.merged_df = merged_df
        self.year = year
    
    def histogram(self):
        for region in self.merged_df['Region'].unique():
            income = self.merged_df[self.merged_df['Region'] == region]['Income'].dropna()
            plt.hist(income,alpha=0.75, label=region)
        plt.xlabel('Income per person')
        plt.ylabel('Number of countries')
        plt.title('Histogram of income per person across regions ' )
        plt.legend()
        plt.savefig('Histogram for' + str(self.year) +'.pdf')
        plt.close()
        
    def boxplot(self):
        self.merged_df['Income'] = list(self.merged_df['Income'])
        self.merged_df.boxplot(column = 'Income', by = 'Region', figsize=(11,8))
        plt.title('Boxplot of income per person across regions')
        plt.ylabel('Income per person')
        plt.xlabel('Region')
        plt.savefig('Boxplot for' +str(self.year) + '.pdf')
        plt.close()
        
        
        
        
        
        
        