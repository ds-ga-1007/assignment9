'''
Module of data structure and methods 
1: GlobalIncome()
2: RegionIncome()
Created on Nov 28, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''
import pandas as pd
import matplotlib.pyplot as plt
import os
class GlobalIncome():

    def __init__(self,DataPath):
        ''' 
        set path of the data
        Args:
            DataPath 
        Returns:
            
        Raises:  
        
        '''
        self.DataPath=DataPath
    def loadingData(self):
        ''' 
        loading data 
        Args:
           
        Returns:
            
        Raises:  
          FileNotFoundError
        '''
        print("Loading Data...")
        self.countries = pd.read_csv(self.DataPath+'countries.csv',header=0)
        self.income = pd.read_excel(self.DataPath+'indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data', header=0,index_col=0)
        return True
    def datatransform(self):
        ''' 
        The program should transform the data set to have years as the rows and countries as the columns.
        Args:
            ALLDATA: dataset 
        Returns:
            
        Raises:  
        
        '''
        print("Data Transforming...")
        self.income=self.income.transpose()
        return True
    def AvailableYears(self):
        ''' 
        Show the head of this data set (all available years)
        Args:
            
        Returns:
            
        Raises:  
        
        '''
        print('All Available Years:')
        print(list(self.income.index))
        return True
    def worldIncomeDistribution(self,Year):
        ''' 
        Generate a histogram of income distribution of the world for a specific year
        Args:
            Year: show the information of this  year
        Returns:
            
        Raises:  
        
        '''
        plt.figure()
        plt.hist(self.income.loc[Year][self.income.loc[Year].notnull()],100)
        plt.xlabel('Income per person')
        plt.ylabel('Frequency')
        plt.title('Histogram of Income per person \n Across all countries '+'for Year:'+str(Year))
        plt.show() 
        return True
    def merge_by_year(self,Year):
        ''' 
        Merge the countries and income data sets for any given year
        Args:
            Year
        Returns:
            dataframe with three columns titled Country , Region ,and Income 
        Raises:  
        
        '''
        return pd.merge(self.countries, pd.DataFrame(self.income.loc[Year].rename('Income')), right_index=True,left_on='Country')
        
class RegionIncome():
    '''
    Income by Region
    '''
    def __init__(self,data,year,datapath):
        ''' 
        init the data set
        Args:
            data: data set 
            year: year lable for the data
        Returns:
            
        Raises:  
        
        '''
        self.data=data
        self.year=year
        self.Path=datapath
       
    def GenerateReport(self):
        ''' 
        Main function for generating report
        Args:
            
        Returns:
            
        Raises:  
        
        '''
        
        path=self.Path[:-8]+'reports/RegionIncomeOf'+str(self.year)
        if not os.path.exists(path):
            os.makedirs(path)
        self.histogram(path)
        self.boxplot(path)
        plt.close("all")
        return True
    def histogram(self,path):
        ''' 
        Histogram
        Args:
            path: path to save the figure
        Returns:
            
        Raises:  
        
        '''
        for region in self.data['Region'].unique():
            hist_figure=plt.figure()
            plt.hist(self.data[self.data.Region==region].Income[self.data[self.data.Region==region].Income.notnull()])   
            plt.xlabel('Income per person')
            plt.ylabel('Frequency')
            plt.title('Histogram of Income per person \n by '+ region +' for Year:'+str(self.year))
            hist_figure.savefig(''.join([path,'/histogram_',region,'_',str(self.year),'.pdf']))
        return True
    def boxplot(self,path):
        ''' 
        Boxplot
        Args:
            path: path to save the figure
        Returns:
            
        Raises:  
        
        '''
        hist=self.data.boxplot(column='Income',by='Region')
        hist_figure = hist.get_figure()
        plt.ylabel('Income per person')
        plt.ylabel('Region')
        plt.title('Boxplot of Income per person \n by Region ' +'for Year:'+str(self.year))
        hist_figure.savefig(''.join([path,'/boxplot_by_region_',str(self.year),'.pdf']))
        return True
        
        
        
        
        
        
        