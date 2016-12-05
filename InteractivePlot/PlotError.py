
class PlotError(Exception):
    pass


class MissingFileError(PlotError):

    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return "Cannot find '{}' in local working directory!" \
               "Make sure you run `python assignment9.py` from the appropriate directory.".format(self.file_name)