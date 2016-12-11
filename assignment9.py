from functions import *
from module import *
import sys

'''The main program imports self-defined functions and module, which load two files to visualize economic data
by a given year input by users. Boxplots illustrate the median, average, 1st and 3rd quartiles, and histograms of
income conditions shows the numbers of countries in different continents.'''

load_data()
def main():
    try:
        inp = input(
            "Input a year in which the yearly income per person you would like to see(Between 1800 and 2012). "
            "Input 'finish' to stop the program.\n")
        while inp != 'finish':
            input_year = int(inp)
            if input_year > 2012 or input_year < 1800:
                raise ValueError('Invalid input!')

            else:
                try:
                    data = merge_by_year(input_year)
                    graph = tool(input_year, data)
                    graph.histogram() and graph.boxplot()
                    plt.close()
                    sys.exit(0)
                except ValueError:
                    print('Invalid input!')

    except KeyboardInterrupt:
        sys.exit(1)

    except EOFError:
        sys.exit(2)

if __name__ == "__main__":
    main()

