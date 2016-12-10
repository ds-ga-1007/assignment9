'''
Auther: Liwei Song
Time Created: 12/04/2016
This is the main file that prompts user to enter years and exhibit histograms of input year
Then, it will automatically generate histograms and boxplots by region from 2006 to 2013
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from a9_function import *

def main():
    #Problem 1
	countries=pd.read_csv('countries.csv')
    #Problem 2
	income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
	income_tp=income.T
	#Problem 3
	income_tp.head()
	while(True):
		try:
			#Prompt user to enter a valid year
			year=input('Please enter a valid year, and enter finish to continue\nEnter quit to end the programming\n')
			if year=='finish':
				break
			elif year.isdigit() and int(year)in income.columns.values:
				show_dist(int(year))
			elif year=='quit':
				sys.exit()
			else:
			#raise error if an incorrect year is input
				raise InputError
		except InputError:
			print('Please enter an valid year between  1800 and 2013')
		except KeyboardInterrupt:
			sys.exit()
		except EOFError:
			sys.exit()

	#generate histograms and boxplots for years from 2007 to 2013.
	for year in range(2007,2013):
		new_year=region_explore(year)
		new_year.define_year_data()
		new_year.make_plot()

if __name__=='__main__':
	main()