import sys
from EconVisualizer import *

'''
Main algorithm of economic data visualization. First query the user for
individual years to graph. Upon receiving word finish,
create standardized graphs showing years 2007-2012
ctrl+c or ctrl+d to exit without saving output graphs to file.
'''
if __name__ == '__main__':
    '''
    read in country and income data
    '''
    try:
        countries = pd.read_csv('../countries.csv')
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()
    except FileNotFoundError:
        raise FileNotFoundError("countries.csv and indicator gapminder gdp_per_capita_ppp.xlsx need to be in the parent directory")

    prompt = "What year would you like to see? Finish to complete report, ctrl+c or ctrl+d to exit\n"
    while True:
        '''Repeatedly query the user for years to graph income data about'''
        try:

            user_input = input(prompt)

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
            print("year must be an integer. Try again?")
            continue

        try:
            graph_income(income, year)

        except ValueError:
            print('year ' + str(year) + " not in range. Try again?")

        except TypeError:
            print('year must be int-like. Try again?')

    """
    Here out of the while loop, the user had to exit the while loop by typing Finish.
    Now we generate graphs for the years 2007-2012.
    """
    ev = EconVisualizer(income, countries)
    ev.graph_years(list(range(2007, 2013)))
    print("Report completetd. See boxplots and histograms of reported data")

            
            
            
            

