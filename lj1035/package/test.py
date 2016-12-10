import unittest
from . import graph, myexception


# This class contains unittests for functions.
class Test(unittest.TestCase):

    def test_merge_by_year(self):
        """
        Unit test for the merge_by_year function.
        """
        merge_df = graph.merge_by_year(1807)
        self.assertEqual(['Country', 'Region', 'Income'], merge_df.columns.values.tolist())
        self.assertEqual(merge_df.ix[0, 'Country'], 'Algeria')
        self.assertEqual(merge_df.ix[0, 'Region'], 'AFRICA')
        self.assertEqual(merge_df.ix[0, 'Income'], 766.121479698518)

    def test_year_string_to_int(self):
        """
        Unit test for the year_string_to_int function.
        """
        self.assertEqual(myexception.year_string_to_int('1806'), 1806)
        with self.assertRaises(myexception.InputError):
            myexception.year_string_to_int('foo')
        with self.assertRaises(myexception.InputError):
            myexception.year_string_to_int('1655')
        with self.assertRaises(myexception.InputError):
            myexception.year_string_to_int('2015')
        with self.assertRaises(myexception.InputError):
            myexception.year_string_to_int('1800.00')

if __name__ == '__main__':
    unittest.main()