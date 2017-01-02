#Author: Julie Cachia
#Email: jyc436@nyu.edu

import pandas as pd
import matplotlib.pyplot as plt
from analysis import *
from dataset import *

"""
This main program will take as input a year between 1800 and 2012, until the user
types in "finish". The program will graphically explore the distributions of income
per person in relation to geographical region for that year. 
"""

while True:
    try:
        year_input = input("Enter a year between 1800 and 2012 to display graphs: ")
	if year_input == "finish":
	    break
        else:
	    try:
                year = int(year_input)
		if year < 1800 or year > 2012:
		    raise InvalidInput
		income_dist(year)
	    except InvalidInput:
                print("Value is not between 1800 - 2012.")
		continue
	    except ValueError:
		print('Invalid Input')
    except EOFError:
	print('Input Error')
    except KeyboardInterrupt:
	print('Keyboard Interrupt')


for y in range(2007,2013):
    merged = merge_by_year(y)
    analysis_by_year = analysis(merged, y)
    analysis_by_year.histogram_region()
    analysis_by_year.boxplot_region()
