# Solution for DS-GA 1007 Assignment#9
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

import pandas as pd
from income_data import IncomeData
from errors import *


def trans_input_to_int(input_str):
    """transform the input string to an integer, and error handling"""
    # empty string
    if len(input_str) == 0:
        raise InvalidInputException
    # every character should be 0-9
    for ch in input_str:
        if ord(ch) < ord('0') or ord(ch) > ord('9'):
            raise InvalidInputException
    ret = int(input_str)
    # the dataset only contains data for 1800-2012
    if ret < 1800 or ret > 2012:
        raise InvalidInputException
    return ret


def main():
    countries = pd.read_csv("../countries.csv")
    income = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx", index_col=0)
    # The input is the transposition of what we expect
    income = income.transpose()
    i_data = IncomeData(income, countries)
    while True:
        input_line = input("please input a year:")
        # handle the finish condition
        if input_line == "finish":
            break
        try:
            year = trans_input_to_int(input_line)
            i_data.dist_income_per_person(year)
        except InvalidInputException:
            print("Input not valid")
    # handle the output plots
    for year in range(2007, 2013):
        i_data.explore_income(year)

if __name__ == "__main__":
    main()
