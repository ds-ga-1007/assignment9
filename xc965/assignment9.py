'''
This is the main module which allows to:
    - visualize the income distribution patterns by user's inputting a year
    - export histograms and boxplots during 2007 to 2012, and save files
    - specifically catch exceptions and errors

@author: Xianzhi Cao (xc965)
'''

import sys
import time
from visualtools import *
from dataprep import *
from UserError import *

def user_interact(df):
    '''

    '''
    while True:
        try:
            year = input('Please select a year between 1800 and 2012 (enter \'q\' for quitting; \'finish\' for the next): ')

            if year.lower() == 'q':
                print(' *** Quitted *** ')
                sys.exit()
            elif year.lower() == 'finish':
                print('\n *** Finish the Display Section *** \n')
                time.sleep(.5)
                break
            else:
                # run the function in question 4
                country_income_display(year, df)

        except EmptyInputError as x:
            print(x)

        except InputFormatError as x:
            print(x)

        except InputValueError as x:
            print(x)

    while True:
        try:
            user_input = input('Do you want to visualize the distributions of regional incomes from 2007 to 2012? (y/n/q)\n>> ')
            if (user_input.lower() == 'n') or (user_input.lower() == 'q'):
                break
            elif user_input.lower() == 'y':
                print('Visualizing incomes distributions from 2007 to 2012 for you.')
                time.sleep(.5)
                print('Please wait ...\n')
                # Visualize histograms and boxplots for incomes across all regions from 2007 to 2013
                for yr in range(2007, 2013):
                    visualization(yr).histogram_plot()
                    visualization(yr).boxplot_plot()
                    print('Histograms and Boxplots of regional incomes in {} have been saved.'.format(yr))
                break
            else:
                raise InvalidInputError
        except InvalidInputError as x:
            print(x)

    # the end of the program
    time.sleep(.5)
    print('\n *** The End *** \n')


if __name__ == '__main__':
    try:
        user_interact(data_prep()[1])  # use the income DataFrame as the parameter

    except EOFError:
        print(' *** Ended *** ')
        sys.exit()

    except KeyboardInterrupt:
        print(' *** Ended *** ')
        sys.exit()
