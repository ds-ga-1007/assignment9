import pandas as pd


def get_int_year(year):
    """
    Check if year is an integer
    :param year
    """
    try:
        y = int(year)
        return y
    except ValueError:
        raise ValueError("The supplied year is not an integer.")


def check_dataframe(df):
    """
    Checks if df is an instance of pandas dataframe
    :param df
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Instance is not a dataframe")
