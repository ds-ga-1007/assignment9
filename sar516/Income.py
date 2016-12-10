class Yearly_Income:
    
    
    def __init__(self, data, year) :
        import pandas as pd
        import numpy as np
        if type(data) == pd.core.frame.DataFrame:
            self.data = data
        else:
            raise ValueError("Invalid type for data passed into this class")
            
        self.region_list = data["Region"].value_counts().index.values
        if type(year) == int :
            if year in range (1800,2013) :
                self.year = year
            else :
                raise ValueError("Invalid year passed into this class")
        elif type(year) == float :
            if year in range (1800,2013) :
                self.year = year
            else :
                raise ValueError("Invalid year passed into this class")
        else:
            raise ValueError("Improper type for year passed into this class")
        
        self.global_mean = data["Income"].mean()
        self.global_median = data["Income"].median()
    
    def regional_income(self) :
        self.region_income = {}
        for region in self.region_list :
            self.region_income[region] = self.data["Income"][self.data["Region"] == region]
        
    
    def regional_boxplot(self, folder) :
        """Creates boxplots of the Income per person per region and then saves it to a file"""
        import matplotlib.pyplot as plt
        import numpy as np
        
        if type(folder) == str :
            pass
        else:
            raise ValueError("expected string for foldername")
        self.regional_income()
        incomes = []
        label = []
        for region in self.region_list :
            incomes.append(self.region_income[region])
            label.append(region)
        plt.close()
        plt.figure(figsize=(14, 7))
        plt.boxplot(incomes, labels = label)
        plt.plot([self.global_mean] * (len(self.region_list) + 2), "r--", label="Global Mean")
        plt.plot([self.global_median] * (len(self.region_list) + 2), "g--", label="Global Median")
        plt.xlabel("Region")
        plt.ylabel("Income per person")
        plt.title("Boxplots of the Income per person for each region for the Year " + str(self.year))
        plt.legend()
        plt.savefig(folder + "/income_boxplot_" + str(self.year) +".pdf")
        plt.close()
        
        
    def regional_histos(self, folder) :
        """Creates a histogram of the distribution of Income for each region and then saves
           each it to a file"""
        import matplotlib.pyplot as plt
        import numpy as np
        
        if type(folder) == str :
            pass
        else:
            raise ValueError("expected string for foldername")
        
        self.regional_income()
        for n in range(len(self.region_list)) :
            region = self.region_list[n]
            plt.close()
            plt.figure(n, figsize=(14, 7))
            plt.hist(self.region_income[region])
            plt.xlabel("Income per person")
            plt.ylabel("Number of Countries")
            plt.title("Histogram for Income per person in " + region + " for Year " + str(self.year))
            plt.savefig(folder + "/histogram_" + region +  "_" + str(self.year) +".pdf")
            plt.close()