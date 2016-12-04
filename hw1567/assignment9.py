# author: Hezhi Wang
from data_analysis import *
from functions import *
import sys

def main():
	"""
	The main function ask the user to enter a year, then display the graph by calling the function
	show_distribution. Continue asking the user for a year and displaying the graph until the string
	'finish' is entered.
	"""

	countries, income = read_data()
	
	while True:
		try:
			str_year = input('Please enter a year between 1800 and 2012, or finish:\n')
			#if the user enter finish, generate histogram and boxplot graph from 2007 to 2012
			if (str_year == 'finish'):
				for i in range(2007, 2013):
					merged_data =  merge_by_year(i, countries, income)
					d = data_analysis(merged_data, i)
					d.histogram()
					d.boxplot()
				sys.exit()
			
			year = int(str_year)

			if (1800 <= year and year <= 2012):
			#calling the question 4 function to display the distribution of income per person across
			#all countries in the world for the given year.
				show_distribution(income, year)
			else: 
				raise ValueError
		except ValueError:
			print("Invalid input year")
		except KeyboardInterrupt:
			sys.exit()
		except EOFError:
			sys.exit()

if __name__ == "__main__":
    main()