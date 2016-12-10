'''
Created on Dec 3, 2016
@author: Zahra Kadkhodaie
Main program. The program asks the user to enter a year, then displays the graph of income for the given year 
It Continues asking the user for a year and displaying the graph until the string finish is entered. The program 
then uses the class explore to generate graphs for the years 2007-2012
'''
 

from explore import *
from auxilary_functions import *


while True:
    
    year_str = input('Enter a year between 1800 to 2012 to see the graph. Close the plot window before entering the next year: ')

    if year_str.lower() == 'finish':
        print('Goodbye!')
        break
    else: 
        if year_str.isdigit(): #Check if the entered value is a positive integer
            year_int = int(year_str)
            if year_int > 2012 or year_int < 1800: #Check if data is available for the entered year 
                print('No data for this year. Please enter a valid year.')
            else:
                visualize_income_year(year_int)
                #plt.show()
        else:
            print('The value entered was not a year. Please enter a year!')

years = list(range(2007,2013)) #years given in the instruction

for item in years: 
    '''Create the box plots in individual files'''
    small_data = merge_by_year(item)
    explore(small_data, item).box()
    explore(small_data,item).histo()
