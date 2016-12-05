
class PlotError(Exception):
    """Base Plot error class"""
    pass


class MissingFileError(PlotError):
    """Raised when unable to find required file in local directory."""

    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return "Cannot find '{}' in local working directory!" \
               "Make sure you run `python assignment9.py` from the appropriate directory.".format(self.file_name)