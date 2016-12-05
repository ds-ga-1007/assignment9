# The InputError class is an extends from the Exception class.
class InputError(Exception):
    def __str__(self):
        return 'The input is not a valid year between 1800 and 2012.\n'


def year_string_to_int(year_string):
    """
    This function takes year_string as an argument and raises exceptions when necessary.
    If no exception being raised, then the function will convert year_string into a value with type int and
    return this value.
    """
    try:
        int(year_string)
    except:
        raise InputError()
    if int(year_string) < 1800 or int(year_string) > 2012:
        raise InputError()
    return int(year_string)