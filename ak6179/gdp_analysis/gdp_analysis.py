from . import gdp_analysis_utils as utils
import pandas as pd
import matplotlib.pyplot as plt


class GdpAnalysis(object):
    def _validate_year(self, year):
        if year not in self._country_gdp_per_capita.index:
            raise ValueError("Year \'%s\' not present in the dataset." % str(year))

    def __init__(self, countries, country_gdp_per_capita, histogram_plots_size=(20, 20), boxplot_size=(10, 6.3),
                 default_plot_size=(8, 6)):
        """
        :param countries: Should contain two columns, 'Country' and 'Region'
        :param country_gdp_per_capita: Should contain years as rows and countries as columns
        """
        self._countries = countries
        self._country_gdp_per_capita = country_gdp_per_capita
        self._histogram_plots_size = histogram_plots_size
        self._boxplot_size = boxplot_size
        self._default_plot_size = default_plot_size

    def plot_histogram_income_year(self, year, bins=50):
        """
        Plot histogram for incomes in the :param year.
        The histogram is displayed on screen. To move ahead the histogram window should be closed.
        :param year
        :param bins
        """
        year = utils.get_int_year(year)
        self._validate_year(year)
        incomes = self._country_gdp_per_capita.loc[year]
        incomes.dropna(inplace=True)
        plt.hist(incomes, bins=bins)
        plt.xlabel('income per person')
        plt.ylabel('number of countries')
        plt.title('Histogram of income per person vs number of countries')
        plt.show()
        plt.clf()

    def merge_by_year(self, year):
        year = utils.get_int_year(year)
        self._validate_year(year)
        incomes = self._country_gdp_per_capita.loc[year]
        incomes_df = pd.DataFrame(data=incomes.values, index=incomes.index)
        merged_df = self._countries.merge(incomes_df, left_on='Country', right_index=True, how='left')
        merged_df.columns = ['Country', 'Region', 'Income']
        return merged_df

    def plot_regions_histogram(self, years, paths, bins=50):
        """
        :param years: list of years. All years should be present in the dataset.
        :param paths: file paths for saving histograms.
        :param bins: number of bins for histograms.
        """
        plt.rcParams['figure.figsize'] = self._histogram_plots_size
        for y, path in zip(years, paths):
            df = self.merge_by_year(y)
            df.dropna(inplace=True)
            regions = set(df['Region'])
            figs, axes = plt.subplots(int((len(regions) + 1) / 2), 2)
            for i, r in enumerate(sorted(regions)):
                mask = (df['Region'] == r)
                region_df = df[mask]
                ind = (int(i / 2), i % 2)
                axes[ind].hist(region_df['Income'], bins=bins)
                axes[ind].set_xlabel('income per person')
                axes[ind].set_ylabel('number of countries')
                axes[ind].set_title('Histogram for ' + r + ' region')
            plt.savefig(path, format='pdf')
            plt.clf()
        plt.rcParams['figure.figsize'] = self._default_plot_size

    def plot_regions_boxplot(self, years, paths):
        """
        :param years: list of years. All years should be present in the dataset.
        :param paths: file paths for saving box-plots.
        """
        plt.rcParams['figure.figsize'] = self._boxplot_size
        for y, path in zip(years, paths):
            df = self.merge_by_year(y)
            df.dropna(inplace=True)
            df.boxplot(column='Income', by='Region')
            plt.savefig(path, format='pdf')
            plt.clf()
        plt.rcParams['figure.figsize'] = self._default_plot_size
