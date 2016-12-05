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
        return False


def check_dataframe(df):
    """
    Checks if df is an instance of pandas dataframe
    :param dataframe
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Instance is not a dataframe")
