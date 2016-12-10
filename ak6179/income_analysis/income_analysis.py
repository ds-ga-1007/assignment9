from . import income_analysis_utils as utils
import pandas as pd
import matplotlib.pyplot as plt


class IncomeAnalysis(object):
    """
    Class for analysis income per citizen for countries.
    Uses countries dataframe and country_gdp_per_capita dataframe.

    """
    def _validate_year(self, year):
        """
        Checks if a given year is integer and whether it is present in the data or not.
        Throws ValueError if invalid year passed.
        :param year
        """
        if year not in self._country_gdp_per_capita.index:
            raise ValueError("Year \'%s\' not present in the dataset." % str(year))

    def __init__(self, countries, country_gdp_per_capita, histogram_plots_size=(20, 20), boxplot_size=(10, 6.3),
                 default_plot_size=(8, 6)):
        """
        Constructor for IncomeAnalysis class.
        :param countries: Should contain two columns, 'Country' and 'Region'
        :param country_gdp_per_capita: Should contain years as rows and countries as columns. Each entry in
        the dataframe is income of the country in that year.
        """
        utils.check_dataframe(countries)
        utils.check_dataframe(country_gdp_per_capita)
        self._countries = countries
        self._country_gdp_per_capita = country_gdp_per_capita
        self._histogram_plots_size = histogram_plots_size
        self._boxplot_size = boxplot_size
        self._default_plot_size = default_plot_size

    def plot_histogram_income_year(self, year, bins=50, display_plot=True):
        """
        Plot histogram for incomes in the :param year.
        The histogram is displayed on screen. To move ahead the histogram window should be closed.
        :param year
        :param bins
        :param display_plot
        """
        year = utils.get_int_year(year)
        self._validate_year(year)
        # get the entry for a particular year
        incomes = self._country_gdp_per_capita.loc[year]
        incomes.dropna(inplace=True)
        plt.hist(incomes, bins=bins)
        plt.xlabel('income per person')
        plt.ylabel('number of countries')
        plt.title('Histogram of income per person vs number of countries')
        if display_plot:
            plt.show()
        plt.clf()

    def merge_by_year(self, year, how='left'):
        """
        Merge _countries dataframe and entry for :param year in _country_gdp_per_capita dataframe.
        Throws ValueError if the year passed is not valid. :param how specifies the type of join.
        :param year
        :param how: join type for the merge. Default value is 'left'
        """
        year = utils.get_int_year(year)
        self._validate_year(year)
        # get the entry for a particular year
        incomes = self._country_gdp_per_capita.loc[year]
        # transform series into a dataframe for a convenient merge
        incomes_df = pd.DataFrame(data=incomes.values, index=incomes.index)
        merged_df = self._countries.merge(incomes_df, left_on='Country', right_index=True, how=how)
        merged_df.columns = ['Country', 'Region', 'Income']
        return merged_df

    def plot_regions_histogram(self, years, paths=[], bins=50, save_figs=True, display_fig=False):
        """
        Plot histograms for given years according to the 'Regions' column in _countries dataframe.
        The histograms can be saved to file and can also be displayed on screen.
        :param years: list of years. All years should be present in the dataset.
        :param paths: file paths for saving histograms.
        :param bins: number of bins for histograms.
        :param save_figs: parameter for deciding whether figure is to be saved to file.
        :param display_fig: parameter for deciding whether figure is to be displayed on screen.
        """
        # setting the size of figure
        plt.rcParams['figure.figsize'] = self._histogram_plots_size
        if not save_figs:
            paths = ["" for x in range(len(years))]
        for y, path in zip(years, paths):
            # merge by year
            df = self.merge_by_year(y)
            df.dropna(inplace=True)
            regions = set(df['Region'])
            # setting up a grid of histograms for plotting different regions
            figs, axes = plt.subplots(int((len(regions) + 1) / 2), 2)
            for i, r in enumerate(sorted(regions)):
                mask = (df['Region'] == r)
                region_df = df[mask]
                # get the index of figure in the grid
                ind = (int(i / 2), i % 2)
                axes[ind].hist(region_df['Income'], bins=bins)
                axes[ind].set_xlabel('income per person')
                axes[ind].set_ylabel('number of countries')
                axes[ind].set_title('Histogram for ' + r + ' region')
            if save_figs:
                plt.savefig(path, format='pdf')
            if display_fig:
                plt.show()
            plt.clf()
        # resetting the size of figure to default
        plt.rcParams['figure.figsize'] = self._default_plot_size

    def plot_regions_boxplot(self, years, paths=[], save_figs=True, display_fig=False):
        """
        Plot boxplots for given years according to the 'Regions' column in _countries dataframe.
        The histograms can be saved to file and can also be displayed on screen.
        :param years: list of years. All years should be present in the dataset.
        :param paths: file paths for saving box-plots.
        :param save_figs: parameter for deciding whether figure is to be saved to file.
        :param display_fig: parameter for deciding whether figure is to be displayed on screen.
        """
        # setting the size of figure
        plt.rcParams['figure.figsize'] = self._boxplot_size
        if not save_figs:
            paths = ["" for x in range(len(years))]
        for y, path in zip(years, paths):
            # merge by year
            df = self.merge_by_year(y)
            df.dropna(inplace=True)
            df.boxplot(column='Income', by='Region')
            plt.title("Income per person")
            if save_figs:
                plt.savefig(path, format='pdf')
            if display_fig:
                plt.show()
            plt.clf()
        # resetting the size of figure to default
        plt.rcParams['figure.figsize'] = self._default_plot_size
