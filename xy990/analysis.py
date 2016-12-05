import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Provide a class do analysis, which define a function to do initialization, define a function
#to do merge_by_year, define a function to plot a histogram and boxplot of income per capita in different regions in a year
#define a function to plot histogram of income per capita in different countries in a year.
class analysis:
    #Initialization
    def __init__(self, data, year):
        self.data = data
        self.year = year

    #Define a function to merge two datasets.
    def merge_by_year(df1, df2, year):
        income_year =pd.DataFrame(df1.loc[str(year)])
        income_year["Country"] = income_year.index
        income_year_merge = pd.merge(income_year, df2)
        income_year_merge = income_year_merge.rename(columns ={str(year): "Income"})
        return income_year_merge

     #Define a function to plot a histogram and boxplot about income per capita in different regions in a certain year.
    def income_by_region(df1, df2, year):
        plt.close("all")
        df = analysis.merge_by_year(df1, df2, year)
        income_region = df.groupby("Region").Income.apply(list)
        in_label = income_region.index.tolist()
        plt.hist(income_region.dropna(), label = in_label)
        plt.title("Histogram of Income in " + str(year))
        plt.xlabel("Income")
        plt.ylabel("Counts")
        plt.legend()
        plt.savefig("Histogram of Income in year" + str(year) +'.pdf')
        plt.close("all")

        df.boxplot(column ='Income', by ="Region")
    
        plt.savefig("Boxplot of Income in year" + str(year) +'.pdf')

     #Define a function to plot a histogram about income per capita in different countries.   
    def income_by_countries(df, year):
        income_per = df.loc[str(year)].dropna()
        plt.hist(income_per, alpha =0.3, color ='r', normed =True)
        plt.title("Histogram of income per person across all countries in year"+ str(year))
        plt.xlabel('Income')
        plt.ylabel("Counts")
        plt.show()
        plt.close("all")
        
    
        
            
    
        
    
    
    
    
    
