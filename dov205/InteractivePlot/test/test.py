import unittest
from assignment9 import *


class InteractivePlotTest(unittest.TestCase):
    """Unit-testing class that allows us to run tests with expected outcomes.

       Run the test in the project's root directory (e.g. pwd should be '.../dov205/')
       with the following command:

           $ python -m unittest discover
       """

    def test_income_distribution(self):
        """Test income distribution index exception handling."""

        # Define invalid years to index gapminder data frame.
        invalid = [-1, 0, 1, 100, 1799, 9999, "2010"]

        # Assert that none of the above "years" are allowed.
        for candidate in invalid:
            with self.assertRaises(InvalidYearError):
                plot_income_distribution(candidate)

    def test_validate_response(self):
        """Test valid input year validation."""

        # Define valid "years" that should pass validation.
        valid = [str(i) for i in range(-2, 10)] + [str(i) for i in range(1800, 2010, 10)]

        # No exceptions should be raise.
        for candidate in valid:
            validate_response(candidate)

    def test_invalid_interpretation(self):
        """Test plot type exception handling."""

        # Define invalid plot types.
        invalid = ['violin', 'pie', 'line', 'scatter', 'stacked']
        plot = InteractivePlot(2000)

        # All candidates should raise an InvalidPlotTypeError
        for candidate in invalid:
            with self.assertRaises(InvalidPlotTypeError):
                plot.interpret(plot_as=candidate)

    def test_merge_columns(self):
        """Test valid plot structure."""

        # Define merged data set.
        merged = merge_by_year(2010)

        # All columns in merged should be, once sorted, equal to the defined list.
        self.assertEqual(sorted(list(merged.columns)), ['Country', 'Income', 'Region'])

    def test_plot_constructor(self):
        """Test valid plot constructor."""

        # Define our list of valid constructor "years"
        valid = [i for i in range(1, 1000)]

        # All candidates should successfully cosntruct an InteractivePlot object.
        for candidate in valid:
            InteractivePlot(candidate)


