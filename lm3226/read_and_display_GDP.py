"""
Date: Dec 5, 2016
Author: Chloe Meng(lm3226)
Description: This program reads two files: countries.csv and indicator gapminder gdp_per_capita_ppp.xlsx.
It generates coresponding bar char for every country's GPD per capita for a given year.
"""
import pandas as pd
import matplotlib.pyplot as plt

class read_and_display_GDP():
    def __init__(self, year):
        self.year = year

    def read_dataset(dataset_name, transpose):
        #This function reads two files into dataframe.
        #In question 3, it requires us to do transpose. We would like to give the option for transpose.
        if dataset_name == 'countries':
            dataset = pd.read_csv('../countries.csv', header=0)

        if dataset_name == 'income':
            dataset = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', 'Data', index_col=0)
            #We want to set years as the rows and countries as the columns for the second file.
            if transpose:
                dataset = dataset.T
                new_header = dataset.iloc[0]
                dataset = dataset[1:]
                dataset = dataset.rename(columns = new_header)

        return dataset

    def generate_income_barchart(self):
        #This function generates bar chart of income per capita for all countries in the given year.
        fig, ax = plt.subplots(figsize=(100,10))
        income = read_and_display_GDP.read_dataset('income', False)
        income = income.take([income.columns.get_loc(self.year)], axis=1)
        ax = income.plot(kind = 'bar')
        ax.set_title('Bar chart of income per capita for '+ str(self.year))
        ax.set_xlabel('Country')
        ax.set_ylabel('Income per capita')
        fig.savefig('Bar chart of income per capita for '+ str(self.year)+'.pdf')
        plt.show()
        plt.close()
