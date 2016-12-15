import pandas as pd
from user_explore import user_explore
from check_input import *
from hist_and_boxplot import *
import sys

'''
author: zhaopeng liu
netid: zl1732
this program will visualize the worldwide gdp information of diferent year
take user input than display histogram and boxplot

could detect not integar error, out of range error, keyboard interupting
one thing can't solve, when plot histogram by region, it have a warning.
'''

def main():
    """ This is the main function that take user's input and give output """
    while 1:
        #print("first while")
        try:
            year = input('Enter the year: ')
            if year == 'finish':
                print("Finished")
                break
            check_input(year)
            year=int(year)
            plot_hist(year)
            
        except NotInterror:
            print("Not a Integar!")
        except OutofRangeError as e:
            print('the input of year: {} is out of range, the range should be between {} and {}'.format(e.args, e.min, e.max))
        except EOFError as e:
            print(e)
            sys.exit(0)
        except KeyboardInterrupt as e:
            print(e)
            sys.exit(1)
        
    ## 8
    u = user_explore()    
    for year in range(2007,2013):
        u.save_plot(year)

        
   

if __name__ == "__main__":
    main()