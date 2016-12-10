
import matplotlib.pyplot as PL
import pandas as PD


# Question 1-3
# Assumes that both datasets are in the parent directory (i.e. assignment9
# directory).
# Also, both datasets are not (supposed to be) accessible outside this
# package.
countries = PD.read_csv('../countries.csv')
income = PD.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',
                       index_col=0).T
# Display the head - shall I print the head like this?
print('Head of the income dataset:')
print(income.head())


# Question 4
def display_gdp_per_capita(year, bins=20):
    '''
    Displays a histogram plotting the distribution of income per person across
    all countries in the world for the given year.

    Parameters
    ----------
    year : int
        The year of which the distribution of GDP per capita is plotted.
    bins : int, default 20
        Number of bins in the histogram.
    '''
    PL.hist(income.loc[year].dropna(), bins=bins)
    PL.show()
    PL.close()


# Question 5
def merge_year(year):
    '''
    Returns a pandas.DataFrame instance with three columns (Country, Region,
    Income), with the Income column fetched from the GDP per capita in the
    given year.

    Note that non-existent values are dropped.

    Parameters
    ----------
    year : int
        The year of which GDP per capita data is merged.
    '''
    income_this_year = income.loc[year]
    income_this_year.name = 'Income'
    return countries.join(income_this_year, on='Country').dropna()


# Question 6
class Plotter:
    '''
    Explores the distribution of GDP per capita and display the distributions
    by region in terms of histograms and boxplots

    Parameters
    ----------
    bins : int, default 20
        Number of bins in the histogram.
    max_hist_y : number, default 50
        The limit of y-axis when plotting histograms.
        Only takes effect when plotting by region.
    max_boxplot_y : number, default 120000
        The limit of y-axis when plotting boxplots
        Only takes effect when plotting by region.
    '''
    def __init__(self, bins=20, max_hist_y=50, max_boxplot_y=120000):
        self.bins = bins
        self.max_hist_y = max_hist_y
        self.max_boxplot_y = 120000

    def display(self, year):
        '''
        Display the GDP per capita in the given year in terms of a histogram.

        Parameters
        ----------
        year : int
            The year of which the distribution of GDP per capita is plotted.
        '''
        display_gdp_per_capita(year, self.bins)

    def display_by_region(self, year, path=None, style='histogram'):
        '''
        Plot the GDP per capita for each region in the given year in terms
        of histogram of boxplot, then either shows it or saves it in a file.

        Parameters
        ----------
        year : int
            The year of which the distribution of GDP per capita is plotted.
        path : None or str
            If None, the figure is displayed in a window.  If a str is given,
            the figure is saved into the path specified in this parameter.
        style : 'histogram' or 'boxplot'
            Plots either histogram or boxplot.
        '''
        # Prepare data
        merged_data = merge_year(year)
        region_gdp = merged_data.groupby('Region').Income.apply(list)
        region_gdp_values = list(region_gdp.values)
        region_gdp_label = list(region_gdp.index)

        # Make actual plot
        if style == 'histogram':
            PL.hist(region_gdp_values, label=region_gdp_label)
            PL.ylim(0, self.max_hist_y)
        elif style == 'boxplot':
            PL.boxplot(region_gdp_values, labels=region_gdp_label)
            PL.ylim(0, self.max_boxplot_y)
        else:
            raise ValueError('style should be "histogram" or "boxplot"')
        PL.legend(loc='best')

        # Show the plot or save it into a file
        if path is None:
            PL.show()
        else:
            PL.savefig(path)

        # Close the figure to release resources
        PL.close()
