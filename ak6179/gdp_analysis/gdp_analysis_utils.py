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
