# Copyright (C) Quan Gan <qg323@nyu.edu>
# Not sure whether I should put a license here or not.

# NOTE: this program is supposed to be run in command line:
# python3 assignment9.py
# For unittests, run
# python3 -m unittest discover

from plotter import *
import sys


def get_input():
    return input('Enter year where the GDP per capita is to be plotted > ')


pl = Plotter()

# Question 7
try:
    user_input = get_input()
    while user_input != 'finish':
        try:
            year = int(user_input)
            pl.display(year)
        except ValueError:
            # Could be thrown by int()
            print("Invalid year given")
        except KeyError:
            # Could be thrown by pandas indexing
            print("The year %d does not exist in the dataset" % year)
        user_input = get_input()
except KeyboardInterrupt:
    print()
    sys.exit(1)
except EOFError:
    print()
    sys.exit(0)

# Question 8
for year in range(2007, 2013):
    print ('Generating histogram and boxplot for year %d' % year)
    pl.display_by_region(year, 'histogram-%d.png' % year, 'histogram')
    pl.display_by_region(year, 'boxplot-%d.png' % year, 'boxplot')
