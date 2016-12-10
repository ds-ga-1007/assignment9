'''
Author: ChuanYa Hsu

The main program allow user to enter a year, then display the histogram of the given year. 
Enter 'finish' to quit the program. The program will generate and save histograms and boxplots of the distribution of the 
income per person by region at the same time.  

Use command line (shell) to run the program like:
>>> python assignment9.py
 
The unit test can be run by using the command:
>>> python test.py
or
>>> python -m unittest 
'''

import numpy as np
from Func.Func import *
from AnalysisTools import AnalysisTools
     
def year_input(year_string):
    
    """Function year_input check whether the input year is correct"""
    
    # list the numbers we can input
    numbers = list(range(10))
    
    # convert to a list of strings
    initial_num = []
    for i in numbers:
        initial_num.append(str(i))
    numbers_string = initial_num
    
    # set the requirement. if f = 0, fulfill the number requirement
    list_year = list(year_string)
    check_year = []
    for i in list_year:
        if i in numbers_string:
            f = 0
        else:
            f = 1
        check_year.append(f)
    possible_year = check_year
    
    # set a comparison group assuming all elements from the input are correct, that is, all fs are zeros
    comp = list(np.zeros(len(possible_year)))
     
    if possible_year == comp:
        convert_year = int(year_string)
    else:
        convert_year = -9999 # using negative number to indicate invalid input 
    
    # only return the year in the range
    if convert_year in range(1800,2013):
        final_year = convert_year
    else:
        final_year = -9999
    return final_year      
    
def main():
    
    """
    main program to run by user, input 'finish' to quit program and save graphs between years 2007-2012.
     
    When input a year between 1800 and 2012, this program will display the distribution of 
    income per person across all countries in the world for the given year
    """
           
    user_input = input('Enter a year between 1800 and 2012 or enter finish to quit\n')
    
    while user_input != 'finish':
        year = year_input(user_input)
                
        while year == -9999:
            print('Invalid year')
            user_input = input('Enter a year between 1800 and 2012 or enter finish to quit\n')
            if user_input == 'finish':
                break
            else:
                year = year_input(user_input)
                    
        if year != -9999:
            plot_year(income, year)
            user_input = input('Enter a year between 1800 and 2012 or enter finish to quit\n')
    
    # Generate graphs for the years 2007-2012
    for i in range(2007, 2013):
        plot = AnalysisTools(i)
        plot.hist_plot()
        plot.box_plot()
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted by the keyboard')