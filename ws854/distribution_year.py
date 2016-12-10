import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class distribution_year():
    """
    The class requires the database, an quaified year integer (since all the filter steps are taken care of in the main program.
    """

    def __init__(self,database,year_input):
        self.database = database
        self.int_year_input = int(year_input)

    def plot(self):
        # the function looks for the row for the int_year_input
        self.year_income = self.database.ix[self.int_year_input]
        # dropout those countries without any data (just to make this part more accurate)
        plt.hist(self.year_income.dropna(axis=0),bins = 10)
        plt.title("Distribution of Income Per Person in "+ str(self.int_year_input))
        plt.xlabel("Income Per Person")
        plt.ylabel("Number of Countries")
        plt.savefig("Distribution in  - " + str(self.int_year_input) + " by Country.pdf")
        plt.show()
