"""
Author: Abhishek Kadian <ak6179@nyu.edu>
Driver program for income analysis.
Requires 'countries.csv' to be present at '../countries.csv' and
'indicator gapminder gdp_per_capita_ppp.xlsx' to be present at '../indicator gapminder gdp_per_capita_ppp.xlsx'.
First part of the program allows user to enter different years and look at histograms for incomes
of different countries for the entered year. The year enterd should be in the range: [1800, 2012]. User can
enter finish to stop plotting histograms.
Second part of the program saves histograms for income of countries grouped by regions (continents).
Third part of the program saves boxplots for income of countries grouped by regions (continents).
"""
import pandas as pd
import sys
import logging
import income_analysis


def main():
    try:
        # Setup logging
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        logging.info("Load \'countries.csv\'.")
        countries = pd.read_csv("../countries.csv")
        logging.info("Load \'indicator gapminder gdp_per_capita_ppp.xlsx\'.")
        country_gdp_per_capita = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx")
        # Taking transpose. After taking the transpose rows are the years and columns are the different countries.
        country_gdp_per_capita = country_gdp_per_capita.set_index('gdp pc test').T
        logging.info("Head of \'country_gdp_per_capita\' dataframe with years as rows and countries as columns:")
        print(country_gdp_per_capita.head(n=5))
        print("-" * 40)
        min_year = country_gdp_per_capita.index.min()
        max_year = country_gdp_per_capita.index.max()
        analysis = income_analysis.IncomeAnalysis(countries, country_gdp_per_capita)
        print(
            "Enter years for displaying histogram of gdp per capita. Enter \'finish\' to stop plotting histograms. "
            "Once the histogram is plotted it should be closed to enter the next year.")
        while True:
            try:
                year = input('Enter year: ')
                if str.lower(year) == "finish":
                    break
                analysis.plot_histogram_income_year(year)
            except Exception as e:
                print(e)
                print("Please enter an integer year in the range [%s, %s] or enter 'finish' to end." % (
                    str(min_year), str(max_year)))
                continue
        # Setting up the exploratory years.
        exploratory_years = [x for x in range(2007, 2013)]
        histogram_paths = ["histogram_" + str(y) + ".pdf" for y in exploratory_years]
        boxplot_paths = ['boxplot_' + str(y) + ".pdf" for y in exploratory_years]
        logging.info("Plotting and saving histograms for exploratory analysis.")
        analysis.plot_regions_histogram(exploratory_years, histogram_paths, bins=20)
        logging.info("Plotting and saving boxplots for exploratory analysis.")
        analysis.plot_regions_boxplot(exploratory_years, boxplot_paths)
    except KeyboardInterrupt:
        print("KeyboardInterrupt, exiting.")
        sys.exit()


if __name__ == "__main__":
    main()
