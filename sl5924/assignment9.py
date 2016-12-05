"""
This module was used for interaction

Created on 2016/12/03
Version: 1.0
@author: Sheng Liu
ShengLiu Copyright 2016-2017
"""
from data_exploratory import *
from data import Display_GDP_All_Countries
import sys

if __name__ == '__main__':
	while True:
		try:
			year = input('Please enter a year from 1800 to 2013: ')
			if year == 'finish':
				break
			if year.isdigit(): 
				if int(year) in range(1800,2013):
					Display_GDP_All_Countries(int(year))
			else:
				raise ValueError('Invalid Input! \n')
		except KeyboardInterrupt:
			sys.exit(1)
		except Exception:
			raise
for year in range(2007,2013):
	data_explore(year).save_histogram()
	data_explore(year).save_boxplots()
