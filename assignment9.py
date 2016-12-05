"""
    Author:
        Danny Vilela

    Overall program behavior:
        Our program runs from the terminal via the call:

            $ python assignment9.py

        Once run, the program will enter the read-evaluate-respond
        loop as defined in Q7 of the assignment. Once the user is
        done and enters 'finish', the progam will finally generate
        the graphs as required in Q8 and exit.

    Output:
        All plot output is saved in one of two directories:

            - box_hist_output: for user outputs from the loop.
            - output: for general output as made by the program.
"""

from InteractivePlot.InteractivePlot import *
import sys


def main():

    # Load initial data sets. (Q1, Q2, Q3)
    countries = read_countries()
    gapminder = read_gapminder(verbose=True)

    # Plot income distribution across population. (Q4)
    plot_income_distribution(2001)

    # Generate histogram of income distribution from year :year. (Q5)
    merge_by_year(2001)

    # Generate graphs of EDA class InteractivePlot. (Q6)
    plot = InteractivePlot(2002)
    plot.interpret(plot_as='box')
    plot.interpret(plot_as='hist')

    # Switch to read-eval-respond loop. (Q7)
    interactive_input()

    # Generate EDA graphs for years 2007, ..., 2012. (Q8)
    generate_graphs()


def plot_income_distribution(year: int):
    """Plot income distribution across all valid countries for year param.

    :param year: integer representation of year we'd like to visualize.
    :return: generates PNG of
    """

    # Load initial 'gapminder' data set
    gapminder = read_gapminder()

    # Drop countries with missing values.
    none_missing = gapminder.dropna(axis=1)

    try:
        # Isolate year of interest -- will throw KeyError
        # if :year is not a row in :countries_across_years.
        countries_across_years = none_missing.loc[year]

    except KeyError:
        raise InvalidYearError(year)

    # Establish plot content
    plt.hist(countries_across_years)

    # Set plot title, x and y labels, etc. Nice-to-haves for looking at plots.
    plt.title("Distribution of income in {}".format(year))
    plt.xlabel("Country GDP per Capita")
    plt.ylabel("Occurrence Frequency")
    plt.grid(True)

    # Save figure to appropriate file location.
    plt.savefig("output/income_distribution_{}.png".format(year))

    # Close plot to release memory required for current figure.
    plt.close()


def interactive_input():
    """Read-eval-respond loop for interactive data exploration.

    :return: generates PNG file with each successful iteration.
    """

    # Receive exception-safe input method.
    response = receive_input()

    # While our response is not 'finish'
    while not response == 'finish':

        # Attempt to plot income distribution.
        try:
            # Use our response to plot income distribution
            # for that year.
            plot_income_distribution(response)

        # Handle case where provided response
        # is not a valid year.
        except InvalidYearError as iye:
            print(iye, file=sys.stderr)

        # Re-prompt our user and restart.
        response = receive_input()


def receive_input():
    """Rigorous/exception-safe user input wrapper.

    :return response: an integer year or 'finish', depending on user preference.
    """

    while True:

        try:
            # Attempt to obtain user input
            response = input("Enter a year from 1800 to 2012. Enter 'finish' to quit. ").lower()

            # Immediately discontinue if user wishes to quit.
            if response == 'finish':
                return response

            else:
                # Otherwise, evaluate whether their response
                # is a valid integer year.
                validate_response(response)

                # If so, return that validated response.
                return int(response)

        # Handle invalid plot years. e.g., 'finis', '1920k', etc.
        except InvalidPlotYearException as ipy:
            print(ipy, file=sys.stderr)

        # Handle termination errors and interrupts.
        except (EOFError, KeyboardInterrupt, SystemExit):
            print("Exiting.", file=sys.stderr)
            sys.exit(1)


def validate_response(user_input: str):
    """User input validation method.

    :param user_input: user response to prompt as string
    :return returns successfully if input is valid, else raises exception
    """

    # Attempt to convert user's response to an integer and return that.
    try:
        user_input = int(user_input)
        return

    # Handle case where we can't cast string to valid int.
    except ValueError:
        raise InvalidPlotYearException(user_input)


def generate_graphs():
    """Generate boxplots and histograms on years 2007 -> 2012.

    :return generates PNG plots in box_hist_output directory.
    """

    # Define our year interval container.
    years = [val for val in range(2007, 2013)]

    # For each year in our container.
    for year in years:

        # Initialize an InteractivePlot instance
        plot = InteractivePlot(year)

        # Plot both boxplot and histogram representations of the data.
        plot.interpret(plot_as='box')
        plot.interpret(plot_as='hist')


if __name__ == '__main__':
    main()
