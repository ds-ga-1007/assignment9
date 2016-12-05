"""
Author: Luyu Jin
This program graphically visualizes the income distribution across the world from 1800 to 2012.

"""
from package import graph, myexception
import sys


def main():
    while True:
        try:
            year_string = input("Please enter a year between 1800 and 2012 (Enter 'finish' to quit): ")
            if year_string == 'finish':
                sys.exit(1)
            year_int = myexception.year_string_to_int(year_string)
            graph.plot_gdp(year_int)
        except myexception.InputError as e:
            print(e)

if __name__ == '__main__':
    try:
        for year in range(2007, 2013):
            combine_gdp_data = graph.merge_by_year(year)
            gdp_graphs = graph.GraphicalAnalysis(combine_gdp_data, year)
            gdp_graphs.histogram_gdp_by_region()
            gdp_graphs.boxplot_gdp_by_region()
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except EOFError:
        sys.exit(1)