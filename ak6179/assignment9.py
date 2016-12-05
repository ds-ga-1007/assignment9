"""
Author: Abhishek Kadian <ak6179@nyu.edu>
"""
import pandas as pd
import sys
import logging
import gdp_analysis


def main():
    try:
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        logging.info("Load \'countries.csv\'.")
        countries = pd.read_csv("../countries.csv")
        logging.info("Load \'indicator gapminder gdp_per_capita_ppp.xlsx\'.")
        country_gdp_per_capita = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx")
        country_gdp_per_capita = country_gdp_per_capita.set_index('gdp pc test').T
        logging.info("Head of \'country_gdp_per_capita\' dataframe with years as rows and countries as columns:")
        print(country_gdp_per_capita.head(n=5))
        min_year = country_gdp_per_capita.index.min()
        max_year = country_gdp_per_capita.index.max()
        analysis = gdp_analysis.Analysis(countries, country_gdp_per_capita)
        print("""Enter years for displaying histogram of gdp per capita. Enter \'finish\' to stop plotting histograms. \
                 Once the histogram is plotted it should be closed to enter the next year.""")
        while True:
            try:
                year = input('Enter year: ')
                if str.lower(year) == "finish":
                    break
                analysis.plot_histogram_income_year(year)
            except Exception as e:
                print(e)
                print("Please enter an integer year in the range [%s, %s]." % (str(min_year), str(max_year)))
                continue
    except KeyboardInterrupt:
        print("KeyboardInterrupt, exiting.")
        sys.exit()


if __name__ == "__main__":
    main()
