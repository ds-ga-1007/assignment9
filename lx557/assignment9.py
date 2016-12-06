'''
Created on 2016.12.2.

This will be used to ask for use for output

@author: xulei
'''

from load_data import *
from Region_class import Region_Income
from excep_class import rangeException #lx557.excep_class can't catch
from year_class import Year
import matplotlib.pyplot as plt

def main():
    
    while True:
        try: 
            input_year=input('Please enter a year\n')
            plt.close('all')
            if input_year.upper()== 'QUIT':
                print()
                print('End')
                raise SystemExit()
            elif input_year.upper()== 'FINISH':
                break
            else:
                year=Year(input_year).yr
                print('Please close the graph to see the next one')
                draw_bar_by_counties(year)
        except ValueError:  #for input is not int
            print('This is not an int,Please enter again')
        except rangeException:
            print('The year you entered is out of range, please reenter')
        except KeyboardInterrupt:
            print('End')
            raise SystemExit()
        
    Region_Income(2007)
    Region_Income(2008)
    Region_Income(2009)
    Region_Income(2010)
    Region_Income(2011)        
    Region_Income(2012) 
    raise SystemExit()


if __name__ == "__main__":
    try:
        print('')
        print('Hint: Exit by finish')
        main()
    except EOFError:
        print()
        print('End') # 
        raise SystemExit()