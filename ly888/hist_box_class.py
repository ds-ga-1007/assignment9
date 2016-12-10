from function import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class hist_box:
    def __init__(self, year):
        # remember the input year
        self.year = year

    def figure(self):
        if self.year>=1800 and self.year<=2012:
            #Merge the data
            merge_data_all=merge_by_year(self.year)
            merge_data=merge_data_all.dropna()
            #Do the histogram
            plt.figure()
            merge_data.hist("Income",by="Region",bins=50,xlabelsize=6);
            plt.xlabel("Income")
            plt.ylabel("Frequency")
            #Save the figure
            plt.savefig("Income histogram for different regions in year %d.pdf"%self.year)
            plt.close()
            #Do boxplot
            plt.figure()
            merge_data.boxplot("Income",by="Region")
            plt.xlabel("Region")
            plt.ylabel("Income")
            #Save the figure
            plt.savefig("Income boxplot for different regions in year %d.pdf"%self.year)
            plt.close()
            return ("The histogram and boxplot are saved")
        else:
            #If the input is not valid, return a warning
            return ("The input year is not valid")