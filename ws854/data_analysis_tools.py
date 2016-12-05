import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class data_analysis_tools():
    """
    Input requires database to analyze  and the year to analyze
    Pre-process: there are quite a few countries can't be mapped to the region (such as Russia), which I will keep all of them as "UNMAPPED"
    Plot the histogram first by using pandas default plot function and output as pdf
    Plot the boxplot also by using pandas default plot function. Change the y-axis to the same max value, which is easier for analysis.
    """

    def __init__(self,database,year):
        self.database = database
        self.year = year
        self.database["Region"] = self.database["Region"].fillna(value = "UNMAPPED")

    def plot(self):
        self.database.hist(column="Income", by="Region", figsize=(10, 10), grid=True,bins =10)
        plt.xlabel("Income Per Person")
        plt.ylabel("Number of Countries")
        plt.savefig("Data Exploratory - Histograms - " + str(self.year) + ".pdf")
        plt.show()
        self.database.boxplot(column="Income", by="Region", figsize=(10, 10), grid=True, rot = 45)
        # make sure the fig is large enough to capture the outlier
        plt.ylim(ymax=120000)
        plt.savefig("Data Exploratory - Boxplots - " + str(self.year) + ".pdf")
        plt.show()
