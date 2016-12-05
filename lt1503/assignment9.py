import sys
from EconVisualizer import *

if __name__ == '__main__':
    '''
    Main algorithm of economic data visualization. First query the user for
    individual years to graph. Upon receiving word finish,
     create standardized graphs showing years 2007-2012
     ctrl+c or ctrl+d to exit without saving output graphs to file.
    '''
    try:
        countries = pd.read_csv('../countries.csv')
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()
    except FileNotFoundError:
        raise FileNotFoundError("countries.csv and indicator gapminder gdp_per_capita_ppp.xlsx need to be in the parent directory")
        
    while True:

        try:
            user_input = input("What year would you like to see? Finish to complete report, ctrl+c or ctrl+d to exit")

        except KeyboardInterrupt:
            # Exit if the user enters Ctrl+C
            sys.exit(0)

        except EOFError:
            # Exit if the user enters Ctrl+D
            sys.exit(0)

        if user_input.lower() == 'finish':
            break

        try:
            year = int(user_input)
        except ValueError:
            print("year must be an integer")
        else:
            # Raises a ValueError and loops back if user_input is not correctly structured
            # as a sequence of intervals
            merged_df = merge_by_year(income, countries, year)

        try:
            graph_income(income, year)

        except:
            print('year ' + str(year) + " not in range. Try again?")

    #Here out of the while loop, the user had to exit the while loop by typing Finish.
    #Now we generate graphs for the years 2007-2012.
    ev = EconVisualizer(income, countries)
    ev.graph_years(list(range(2007, 2013)))

            
            
            
            

