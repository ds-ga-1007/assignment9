"""
Author: Abhishek Kadian <ak6179@nyu.edu>
"""
import pandas as pd
import sys
import logging
import income_analysis


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
