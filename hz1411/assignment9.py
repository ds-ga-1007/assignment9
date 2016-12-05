'''
author: Han Zhao 
email: hz1411@nyu.edu

This is the main program that keeps prompting the user to enter a year, until the string ‘finish’ is entered. 
It then display the distribution of income per person across all countries in the world for the given year. 
It also generates histograms and boxplots of the distribution of the income per person by region for the years 2007-2012.

'''
from analysis import *
from data import *
from exceptions import *

while True:
# keep reading year from user input until input == 'finish'
	try:
		year_input = input("Enter year or 'finish' to exit:")
		if year_input == 'finish':
			break
		else:
			try:
				year = int(year_input)
				if year < 1800 or year > 2012:
					raise InvalidInput
				income_distribution(year)
			except InvalidInput:
				print('Value out of range!')
				continue
			except ValueError:
				print('Invalid Input!')
	except KeyboardInterrupt:
		print('User Interrupt')
	except EOFError:
		print('Input Error')


for year in range(2007,2013):
    merged = merge_by_year(year)
    analysis_year = analysis(merged, year)
    analysis_year.histogram_by_region()
    analysis_year.boxplot_by_region()


