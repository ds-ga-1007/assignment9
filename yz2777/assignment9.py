""" Question 7, main program """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from func import *
from class_analysis import analysis_tools

# Q7
# define a function to make sure the input year is correct
def year_input_correct(year_string):
    
    # list the numbers we can input
    numbers = list(range(10))
    
    # convert to a list of number strings
    initial_num = []
    for i in numbers:
        initial_num.append(str(i))
    numbers_string = initial_num
    
    list_year = list(year_string)
    check_year = []
    for i in list_year:
        if i in numbers_string:
            f = 0    # fulfill the number requirement
        else:
            f = 1    # not fulfill 
        check_year.append(f)
    possible_year = check_year
    
    # set a comparison group assuming all elements from the input are correct, that is, all fs are zeros
    comp = list(np.zeros(len(possible_year)))
    
    if possible_year == comp:
        convert_year = int(year_string)
    else:
        convert_year = -9999 # using negative number to indicate invalid input 
   
    if convert_year in range(1800,2013):
        final_year = convert_year
    else:
        final_year = -9999
    return final_year     


# user input
def inpt():
    user_input = input('Please enter a year between 1800 and 2012 or enter finsih to quit\n')
    # first, give an indicator for input, 0 means incorrect input and 1 means correct
    # while loop to check whether the user input the correct year
    while user_input != 'finish':
        year = year_input_correct(user_input)
        
        # if the user input is incorrect, the program will ask to enter again 
        while year == -9999:
            print ('Invalid year input')
            user_input = input('Please enter a year between 1800 and 2012 or enter finsih to quit\n')
            if user_input == 'finish':
                break
            else:
                 year = year_input_correct(user_input)
        
        # if the year input is correct, the plot will come out and then ask user to input year again until enter finish
        if year != -9999:
            plot_income_by_year(year,read_income(file_path_i)) # if the year input is correct we use function based on Q4
            user_input = input('Please enter a year between 1800 and 2012 or enter finsih to quit\n')
    
    # Q8
    # get the plots from 2007 to 2012 based on the class created in Q6
    for i in range(2007,2013):
        plot = analysis_tools(i)
        plot.hist_plot()
        plot.box_plot()
        
        
if __name__ == '__main__':
    try:
        inpt()
    except KeyboardInterrupt:
        print('Interrupted by the keyboard')
