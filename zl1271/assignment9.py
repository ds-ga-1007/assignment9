'''
Created on Nov 30, 2016

@author: felix
'''

from data_funcs import * 
from distribution_plot import Distribution
import numpy as np

def main():
    while True:
        try:
            countries = get_countries()
            income = get_income()
            # Question 3
            print(income.transpose().head())
            try:
                income_data = Income(countries, income)
                
                try:
                    # Question 7
                    user_input_str = ''
                    while not valid_user_str(user_input_str):
                        user_input_str = input('Please enter a year (4 digits), or \'finish\' to finish\n')
                    
                        if not valid_user_str(user_input_str):
                            pass
                        elif valid_finish_str(user_input_str):
                            exit('Program finished')   
                        else:
                            year = int(user_input_str)
                            
                            if income_data.year_is_valid(year):
                                income_data.plot_distribution_of_year(year)
                            else:
                                print('Year out of range')
                            
                        user_input_str = ''
            
                except:
                    # When question 7 is done, program goes here
                    # Question 8
                    for year in np.arange(2007,2013):
                        this_df = income_data.merge_by_year(year)
                        this_distribution = Distribution(this_df, year)
                        this_distribution.plot_box()
                        this_distribution.plot_hist()
                        print('Year ' + str(year) + ' finished')

                    print('Program finished') 
                    break 
                
            except:
                raise Exception('Unexpected data files')
                break
            
        except:
            raise Exception('Data files not found at default location.')
            break
        

            
            
if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass