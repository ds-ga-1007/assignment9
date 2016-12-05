import pandas as pd
import numpy as np
from analysis import *

#load data
countries=pd.read_csv("/Users/zoem/Documents/ds1007/assignment10/assignment9/countries.csv")
income=pd.read_excel("/Users/zoem/Documents/ds1007/assignment10/assignment9/indicator_gapminder_gdp_per_capita_ppp.xlsx")
income=income.transpose()

print("head: \n")
print(income.head(5))



while True:
    try:
        input_year=input("Please enter a year to begin, enter finish if you want to quit: ")

        if input_year.lower() == 'finish':
            for year in range(2007,2013):
                merged_df=merge_by_year(year, countries, income)
                anal=analysis(merged_df, year)
                anal.hist_plot()
                anal.box_plot()
            sys.exit()

        if int(input_year) not in income.index:
            raise ValueError ("Invalid input. Please enter an integer from 1800 to 2012")

        else:
            year=int(input_year)
            income_distribution(income, year)

    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)
