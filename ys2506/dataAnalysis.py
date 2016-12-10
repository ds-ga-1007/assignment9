# Solution for DS-GA 1007 Assignment#9
# Author: Yanan Shi y2506 N11812897
import matplotlib.pyplot as plt
import pandas as pd

#	Provide a class that uses exploratory data analysis tools (histograms and boxplots) to graphically explore the distribution of the income per person by region data set from question 5 for a given year. Save these graphs to individual files.
class DataAnalysis(object):
    
    def __init__(self, income, countries):
        self.income = income
        self.countries = countries
    
    #	Provide a function to graphically display the distribution of income per person across all countries in the world for the given year. Choose the best kind of plot to display this information.
    def distribution_income(self,year):
        income = self.income.transpose()
        year_income = income.ix[year]
        plt.hist(year_income.dropna(axis=0),bins = 10)
        plt.title("distribution of income per person across all countries in the world for the year" + str(year))
        plt.xlabel("Income Per Person")
        plt.ylabel("Countries")
        plt.savefig("Distribution of " + str(year) + ".png")
        plt.show()
        plt.close()
    
    #Provide a function called merge_by_year(year) to merge the countries and income data sets for any given year. The result should be a DataFrame with three columns titled Country, Region, and Income.
    def merge_by_year(self, year):
        income_year = pd.DataFrame(self.income[year])
        merged = pd.merge(self.countries,income_year,left_index=True,right_index=True)
        merged["Country"] = merged.index
        merged.rename(columns = {year:'Income'}, inplace = True)
        return merged

    #graphically explore the distribution of the income per person by region data set from question 5 for a given year. Save these graphs to individual files.
    def generate_graphs(self, year):
        merged = self.merge_by_year(year)
        self.graphs(merged, year)
   
    def graphs(self, data, year):
     #use histograms to graphically explore the distribution of the income per person by region data set
        fig = plt.figure()
        plt.hist (data["Income"].dropna().values)
        plt.title("histogram for year" + str(year))
        fig.savefig("histogram for year" + str(year) + '.png')
        plt.show()
        plt.close()
        #use boxplots to graphically explore the distribution of the income per person by region data set
        data.boxplot('Income', by = 'Region')
        plt.title("boxplots for year" + str(year))
        plt.savefig("boxplots for year" + str(year) + '.png')
        plt.show()
        plt.close()







