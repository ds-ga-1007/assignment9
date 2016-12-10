# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def importMyCsv(file_name):
    
    '''Function to import csv from upper level dir: assumes header'''
    
    # COPYRIGHT NOTE: 
    # This way of setting directory is widely used by 
    #    professors and TA's during my current courses. 
    # Make sure the directory is correctly set. 
    
    currentDirectory = os.getcwd()
    datadir = "/".join(currentDirectory.split('/')[0:-1]) + "/"
    file = pd.read_csv(datadir + file_name + ".csv", header=0)
    return file

def importMyExcel(file_name):
    
    ''' Function to import excel from upper level dir: : assumes sheetname=0, index_col=0 '''
    
    # COPYRIGHT NOTE: 
    # This way of setting directory is widely used by 
    #    professors and TA's during my current courses. 
    # Make sure the directory is correctly set. 
    
    currentDirectory = os.getcwd()
    datadir = "/".join(currentDirectory.split('/')[0:-1]) + "/"
    file = pd.read_excel(datadir + file_name + ".xlsx", sheetname=0, index_col=0)
    return file

def stackUnstack(pandasDataFrame):
    
    '''Function to transpose any given pandas dataframe '''
    
    pandasDataFrame = pandasDataFrame.stack(dropna=False)
    pandasDataFrame = pandasDataFrame.unstack(level=0)
    return pandasDataFrame
    
class numberNotANumber(Exception):
    def __str__(self):
        return "Input is no number"    

def stringToNumber(number):
    
    ''' Function to pass string to number. If not, raise an exception '''
    
    try: 
        number = int(number)
        return number
    except: 
        raise numberNotANumber()
    
def TestIfInIndex(indexTest, pandasDataFrame):
    
    '''Function to test if  indexTest is in pandasDataFrame index'''
    
    value = indexTest in pandasDataFrame.index
    return value
    
    
def incomePerYear(data, year):
    
    ''' Function to display a graph bar of income per year '''
    
    plt.close("all")
    plt.figure(figsize=(18,10))
    
    # Note: ideally, I had (figsize=(18,25)) so names are well displayed, 
    #       but the UX in my computer is really bad, and does not 
    #       allow to scroll down. 
    
    yeardata = data.ix[year]
    noInfo = sum(pd.isnull(yeardata))
    yeardata = yeardata.dropna()
    yeardata.sort_values(axis=0, ascending=True, inplace=True) 
    y_pos = np.arange(len(yeardata))
    countriesNames = pd.Series(yeardata.index.values, dtype="category")
    plt.barh(y_pos, yeardata, color="#1d91c0")
    plt.yticks(y_pos, countriesNames, size=5)
    plt.ylim(0, len(yeardata))
    plt.xlabel('GDP per capita (PPP, 2005 dlls.)')
    plt.annotate("Countries with \n missing data: {} \n \n Source: Gapminder".format(noInfo), xy=(0.85, 0.01), xycoords='axes fraction', size=8)
    plt.title("GDP per capita per country \n {}".format(year))
    #plt.savefig("{}_income.pdf".format(year))
    plt.show()
    
def merge_by_year(year, dataset1, dataset2):
    yeardata = pd.DataFrame(dataset1.ix[year])
    yeardata["Country"] = yeardata.index.values
    mergedData = pd.merge(yeardata, dataset2, on="Country", how="right")
    
    ''' Right merge. Why? Because data of gapminder includes countries that have never been recognize or 
        countries that have been long dissapeared. If the .csv "countries.csv" was downloaded from an 
        official source such as the World Bank or the UN, is a better guideline for existing countries. 
        
        A note: merging on names is a really bad practice. We should try using iso3 or COW codes.
        MORE: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
        COW codes: http://cow.dss.ucdavis.edu/data-sets/cow-country-codes'''
    
    mergedData = mergedData.rename(columns={year:"Income"})
    return mergedData

class exploreByRegion():
    
    def __init__(self, year, dataset1, dataset2):      
        
        self.year = year
        self.dataset1 = dataset1
        self.dataset2 = dataset2
        self.dataFrame = merge_by_year(self.year, self.dataset1, self.dataset2).dropna()
        self.regionTabulation = self.dataFrame["Region"].value_counts()      
        
    def boxPlot(self):
        
        '''Note: y axis is forced to be 0 to 100 000 to compare 2007 to 2012'''
        
        plt.close("all")
        dataForPlot =  self.dataFrame.drop("Country", axis=1)        
        plt.figure(figsize=(18,25))
        dataForPlot.boxplot(by="Region", patch_artist=True)
        plt.title("Income by Region \n Year: {}".format(self.year))
        plt.suptitle("")
        plt.xlabel("Region")
        plt.ylim(0, 100000)
        plt.xticks(rotation=45)
        plt.savefig("boxPlot_{}.pdf".format(self.year))
        plt.close("all")
    
    def histograms(self):
        
        '''Note: range is forced to be 0 to 100 000 to compare 2007 to 2012'''
        
        plt.close("all")
        self.dataFrame.Income.hist(by=self.dataFrame["Region"], 
                                   figsize=(5, 7), color="#1d91c0", sharex=True, range=[0, 100000])
        plt.suptitle("Histograms of income by region \n Year: {}".format(self.year))
        plt.savefig("histogram_{}.pdf".format(self.year))