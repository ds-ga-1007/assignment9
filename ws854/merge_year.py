import pandas as pd
class merge_year():
    """
    This class requires income(database), countries(database), year to analyze.
    """

    def __init__(self,income,countries, year):

        self.income = income
        self.countries = countries
        self.year = year
        # find out the index for the year to analyze
        self.index_location = self.income.index.get_loc(self.year)
        # find out the year and transpose back to merge with countries. left database is on the column, right is on the index
        # also, I will take the outer function since my data_analysis_tools will output unmapped countries
        self.merged_df = pd.merge(self.countries, self.income.iloc[[self.index_location]].T, left_on="Country", right_index=True,
                             how="outer")
        self.merged_df.columns = ['Country', 'Region', 'Income']

    def result(self):
        return self.merged_df