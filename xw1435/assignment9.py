from explore import *
from function import *

'''
prompt user for a input year, check input validity, then display the distribution of income per person 
across all countries until user input finish 
'''

terminate = False
print(countries.head())
print(income.head())

while terminate == False:
    user_input = input('Please choose a year you want to see in between 1800 and 2012: \n')
    if user_input == 'finish':
        print('Thank you for using this program, your plots will be ready soon!')
        terminate = True
        break
    else:
        try:
            user_input.isdigit()
            len(user_input) == 4
            year = int(user_input)
        except ValueError:
            print('Invalid input, please choose a year in 4 digit format ')
    
    income_by_year(year)    
        

'''
Generate plots for income per capita by region from year 2007 to 2013 
'''

for year in range(2007, 2013):
    
    year_to_explore = explore(year)
    year_to_explore.draw_boxplot()
    year_to_explore.draw_histogram()


