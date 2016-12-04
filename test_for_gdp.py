import unittest
from class_functions import *


class MyTestCase(unittest.TestCase):
    """
    Unit test that tests for merge_by_year() function
    """
    def test_merge_by_year(self):
        merged_data = merge_by_year(1999)
        self.assertEqual(merged_data.columns.values.tolist(), ['Country', 'Region', 'Income'])


if __name__ == '__main__':
    unittest.main()
