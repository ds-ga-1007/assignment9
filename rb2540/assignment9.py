"""
This is a program that analyzes GDP per capita data across countries and regions
from 1800 to 2012.
"""
import numpy as np
import pandas
import matplotlib.pyplot as plt
from GDPAnalysis import GDPAnalysis

def income_per_person(year) :
    """Plots a histogram of per capita GDP for a given year"""
    incomes.hist(str(year))
    plt.title('Histogram of per capita GDP for each country in '+str(year))
    plt.xlabel('Per capita GDP in Dollars')
    plt.ylabel('# of Countries')
    plt.show()

def merge_by_year(year) :
    """Merges the countries and income data sets for a given year"""
    m = pandas.merge(sincomes.loc[sincomes['Year']==str(year)],countries,on='Country')
    return m.drop('Year',axis=1)

def loadData() :
    """Loads csv files representing country and per capita GDP data"""
    global countries, incomes, incomesT, sincomes
    countries = pandas.read_csv('../countries.csv')
    incomes = pandas.read_csv('./indicator gapminder gdp_per_capita_ppp.csv',
                              header=0)
    incomesT = incomes.set_index('Country')
    incomesT = incomesT.transpose()
    sincomes = pandas.melt(incomes,id_vars=['Country'],var_name='Year',value_name='Income')
    print(incomesT.head())

def main() :
    """Prompts the user for years, and 
    performs analyses on the data"""
    loadData()
    while True:
        try :
            inp = input("Input a year to analyze ('finish' to end): ")
            if inp == 'finish' :
                break
            income_per_person(int(inp))
        except ValueError as err :
            print('Invalid year entered: '+str(err))
        except KeyError as err :
            print('Invalid year entered: '+str(err))
    for year in range(2007,2012+1) :
        gdp = GDPAnalysis(year,merge_by_year(year))
        gdp.performAnalysis()

if __name__ == "__main__" :
    main()

