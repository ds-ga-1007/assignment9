import pandas as pd
import matplotlib.pyplot as plt
from .PlotError import *
from .UserError import *
import warnings

# Ignore Pyplot warnings.
warnings.filterwarnings("ignore")


class InteractivePlot:

    def __init__(self, year):
        """Provide EDA representation for box/hist interpretation of data."""

        self.year = year

    def __repr__(self):
        """Unambiguous representation of InteractivePlot object -- its instantiation."""
        return "InteractivePlot({})".format(self.year)

    def interpret(self, plot_as):
        """Provide EDA tool for boxplot interpretation of data.

        :param plot_as: plot type denoting aggregation heuristic.
        :return: outputs boxplot or histogram as PNG to local directory.
        """

        # Utilize merge_by_year to isolate year of interest.
        merged = merge_by_year(self.year)

        # Determine which aggregation/exploration to use
        # based on user input to interpret() method.
        if plot_as.lower() in ["hist", "histogram"]:

            # Use a histogram grouped by Region.
            # Rotate x-axis labels 30 degrees for convenience.
            merged.hist(column='Income', by='Region', grid=True, xrot=30)

            # Set tight, non-overlapping layout.
            plt.tight_layout()

            # Set plot super-title.
            plt.suptitle("Distribution of income in {}".format(self.year))

            # Set our suffix reminder.
            suffix = 'hist'

        elif plot_as.lower() in ["box", "boxplot"]:

            # Use a boxplot grouped by Region.
            merged.boxplot(column='Income', by='Region', grid=True, rot=30)

            # Set plot title, x and y labels, etc. Nice-to-haves for looking at plots.
            plt.suptitle("Group-wise central tendency of per-person income in {}".format(self.year))
            plt.xlabel("Region")
            plt.ylabel("Income Tendencies")

            # Set our suffix reminder.
            suffix = 'box'

        else:

            # If :plot_as is neither accepted format,
            # raise an error.
            raise InvalidPlotTypeError(plot_as)

        # Save figure to appropriate location and with distinct filename format.
        plt.savefig("box_hist_output/income_region_{}_{}.png".format(self.year, suffix))

        # Close plot to release memory required for current figure.
        plt.close()


def read_countries() -> pd.DataFrame:
    """Read provided 'countries' data set.

    :return: data from 'countries.csv' as a DataFrame.
    """

    # Try to read and return the countries data set.
    try:
        countries = pd.read_csv('countries.csv')

    # If we can't, inform the user they're running
    # the script somewhere they shouldn't be.
    except FileNotFoundError:
        raise MissingFileError("countries.csv")

    return countries


def read_gapminder(verbose=False) -> pd.DataFrame:
    """Read provided 'gapminder' data set.

    :param verbose: denote whether we want to print data head (True).
    :return: transposed: gapminder data set transposed.
    """

    # Try to read the gapminder excel file and use the 0th
    # column as our data frame's row index.
    try:
        gapminder = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col=0)
        transposed = gapminder.transpose()

    # Inform the user if we can't find our required file.
    except FileNotFoundError:
        raise MissingFileError("indicator gapminder gdp_per_capita_ppp.xlsx")

    # Inform user we successfully read the data set if
    # they requested verbose output.
    if verbose:
        print("Successfully read GapMinder data set:")
        print("-" * 40)
        print(transposed.head())

    # Return transposed data set.
    return transposed


def merge_by_year(year: int) -> pd.DataFrame:
    """Given year integer, join countries and gapminder into 3-col DataFrame.

    :param year: integer representation of the year of interest.
    :return merged_by_year: 3-col DataFrame containing Country, Region, Income.
    """

    # Load initial 'gapminder' data set.
    countries, gapminder = read_countries(), read_gapminder()

    # Extract raw income data for year :year.
    raw_income_year = pd.DataFrame(gapminder.loc[year])

    # Drop rows with NaN (missing) values.
    clean_income_year = raw_income_year.dropna()

    # Reset zeroth index level for proper merging.
    clean_income_year = clean_income_year.reset_index(level=0)

    # Reset clean data set columns to required fields.
    clean_income_year.columns = ['Country', 'Income']

    # Merge clean income and countries data sets on their 'Country' field.
    merged_by_year = pd.merge(clean_income_year, countries, how='inner', on='Country')

    # Return our joined data set.
    return merged_by_year
