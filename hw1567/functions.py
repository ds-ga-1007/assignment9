import pandas as pd
import matplotlib.pyplot as plt


def read_data():
	#this function read dataset 'countries.csv' and 'indicator gapminder gdp_per_capita_ppp.xlsx'
	countries = pd.read_csv('countries.csv')
	income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0)

	#transform the dataframe income to have years as the rows and countries as the columns,
	#and show the head of this dataset
	income_transpose = income.T
	print(income_transpose.head())
	return countries, income

def merge_by_year(year, countries, income):
	"""
	This function merge the countries and income data sets for any given year.
	
	parameters:
		year: int
		countries: Dataframe
		income: Dataframe

	Return:
		nerged_data: Dataframe with columns as 'Country', 'Region', 'Income'
	"""
	income_one_year = pd.DataFrame(income[year])
	merged_data = pd.merge(countries, income_one_year, left_on='Country', right_index=True).dropna()
	merged_data.columns = ['Country', 'Region', 'Income']
	return merged_data

def show_distribution(income, year):
	"""
	This function display the distribution of income per person across all countries in the world for the given year
	parameters:
		year: int
		income: Dataframe
	
	Return:
		Show the histogram
	"""
	income[year].dropna().plot(kind = 'hist')
	plt.title("Histogram of graphically distribution of the income per person in " + str(year))
	plt.xlabel('Income per person')
	plt.ylabel('Count')
	plt.show()
	plt.close()