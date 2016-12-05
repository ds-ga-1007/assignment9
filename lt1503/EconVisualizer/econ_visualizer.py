from .visualizer_utils import *


class EconVisualizer(object):
    """
    Economic Visualizer object. Can contain economic information and visualizes information
    from its variables or from external variables
    """
    
    def __init__(self, income = None, countries = None):
        """
        :param income: pandas.DataFrame or None of income data
        :param countries: pandas.DataFrame or None of income data
        """
        if not isinstance(income, pd.DataFrame) and not income is None:
            raise TypeError("income must be None or a pandas DataFrame")
        if not isinstance(countries, pd.DataFrame) and not countries is None:
            raise TypeError("countries must be None or a pandas DataFrame")

        self.income = income
        self.countries = countries
    
    def graph_years(self, years):
        """
        graph income from income and countries dataframes within list of years
        :param years: int-like
        :return: None. Writes boxplots and histograms to file for income and country data
                for years in parameter years
        """
        
        if not isinstance(years, list):
            raise ValueError("can only graph years where years is a list of integers")
            
        if not isinstance(self.income, pd.DataFrame) or not isinstance(self.countries, pd.DataFrame):
            raise ValueError("EconVisualizers must have pandas DataFrames for income and countries to graph lists of years")

        for year in years:

            try:
                year = int(year)
            except TypeError:
                raise ValueError("Every year in years to graph must be numeric")

            if not year in self.income.index.values:
                raise ValueError("year must be between " + str(np.min(self.income.index.values))
                                 + " and " + str(np.min(self.income.index.values)))

            merged_df = merge_by_year(self.income, self.countries, year)

            self._box(merged_df, visualize = False)
            self._hist(merged_df, visualize = False)
            
    def _hist(self, df, visualize = True):
        """
        Show histogram if visualize is set to true.
        Regardless, save histogram of income data to file
        :param df: pandas.DataFrame of income data
        :param visualize: Boolean representing to visualize results or just save to file
        :return: None
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError("hist df must be a pandas DataFrame")

        try:
            df["income"]
        except KeyError:
            raise ValueError("econ visualizer histograms require income columns")
        plt.figure()
        df.hist(column='income', by='Region')
        
        try:
            year_label = "year " + str(df.year)
        except AttributeError:
            year_label = "an unknown year"
            
        plt.title("histograms of incomes from " + year_label)
        plt.xlabel("average income per person")
        plt.ylabel("percent of countries with average income in range")
        plt.savefig("histogram of incomes from " + year_label + ".png")

        if visualize:
            plt.show()
        plt.close()
            
    def _box(self, df, visualize = True):
        """
        Show boxplot if visualize is set to true.
        Regardless, save boxplot of income data to file
        :param df: pandas.DataFrame of income data
        :param visualize: Boolean representing to visualize results or just save to file
        :return: None
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError("box df must be a pandas DataFrame")

        try:
            df[["income"]]
        except KeyError:
            raise KeyError("econ visualizer booxplots require income columns")
        plt.figure()
        df.boxplot(column='income', by='Region')
        
        try:
            year_label = "year " + str(df.year)
        except AttributeError:
            year_label = "an unknown year"
            
        plt.title("box plot of incomes from " + year_label)
        plt.ylabel("average income per person")
        plt.savefig("boxplot of incomes from " + year_label + ".png")

        if visualize:
            plt.show()
        plt.close()
