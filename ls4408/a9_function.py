import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Author:Liwei Song
Time created: 12/04/2016
This module contain most functions that will be be used in main file
'''

#Problem 4
'''This function shows the histogram of a given year input by the user''' 
def show_dist(year):
    countries=pd.read_csv('countries.csv')
    income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)#'gdp pc test')
    income_tp=income.transpose()
    income_series=income_tp.ix[year].dropna()
    plt.hist(income_series)
    plt.title('Histogram of Income Per Person Across the World ')
    plt.xlabel('Income')
    plt.ylabel('Number of Countries')
    plt.show()
    plt.close()

'''This function merge countries with income dataframe at a given year input by the user.''' 

def merge_by_year(year):
    income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)#'gdp pc test')
    countries=pd.read_csv('countries.csv')
    income_tp=income.transpose()
    year_income=pd.DataFrame(income[year])
    new_data_frame=pd.merge(countries,year_income,left_on='Country',right_index=True)
    rename=new_data_frame.rename(columns={year:'Income'})
    return rename

'''This class is used for boxplots and histogram by year at a given year input by the user.'''
class region_explore(object):
    def __init__(self, year):
        self.year = year
    
    
    def define_year_data(self):
        self.data=merge_by_year(self.year)
        #define the year
        
    def make_plot(self):
        a=[321,322,323,324,325,326]
        i=0
        plt.figure(figsize=(20,10 ))
        for region in np.unique(self.data['Region']):
            new_data=self.data[self.data['Region']==region]
            income_by_region_series=new_data['Income'].dropna()
            plt.subplot(a[i])
            #make a subplot of histogram
            plt.hist(income_by_region_series)
            plt.title('Histogram of Income Per Person in '+ str(region)+' in Year ' +str(self.year))
            #make histograms by region
            plt.ylabel('Number of Countries')
            i=i+1
        plt.savefig('Histogram_of_Income_Per_Person_by region_'+str(self.year)+'.pdf')
        #save the histograms by region
        plt.close()
        
    
        
        i=0
        plt.figure(figsize=(20,10 ))
        plt.title('Boxplot of Income Per Person by region in Year ' +str(self.year))
        for region in np.unique(self.data['Region']): 
            new_data=self.data[self.data['Region']==region].dropna()
            income_by_region_series=new_data['Income']
            plt.subplot(a[i])
            #make a subplot of boxplot
            plt.title('Boxplot of Income Per Person in '+ str(region)+' in Year ' +str(self.year))
            plt.boxplot(income_by_region_series.reset_index(drop=True))
            plt.ylabel('Range of Income Per Person in '+ region)
            i=i+1
        plt.savefig('Boxplot_of_Income_Per_Person_in_by region_' +str(self.year)+'.pdf')
        #save the histograms by region
        plt.close()

'''define a input exception for user input error'''
class InputError(Exception):
    def __init__(self):
        pass


    