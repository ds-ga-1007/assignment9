import unittest
from Position.Position import *
from Position.Position_functions import *

#The following are test cases to ensure correct functionality of intervals
class MyTest(unittest.TestCase):
    """unit tests for functions relating to the position class
    These should be run by enterring the command "python -m unittest discover"
    from the root directory of this project
    """
    def test_constructor_positive(self):
        """unit tests for the position constructor"""
        positions_input = '1, 10, 100, 1000'
        positions = get_position_list(positions_input)
        for p_idx, position in enumerate(positions):
            self.assertEqual(position.num_shares, 10**p_idx)
            self.assertEqual(position.share_value, 1000/(10**p_idx))
            
    def test_position_list_constructor_positive(self):
        """tests input strings are handled correctly by get_positions_list
        This assures that these user inputs would be translated to
        position lists"""
        pos_list = get_position_list('1 , [10]')
        self.assertTrue(isinstance(pos_list, list))
        for pos in pos_list:
            self.assertTrue(isinstance(pos, position))
            
        pos_list = get_position_list('[ 1, 10, 100, 1000]')
        self.assertTrue(isinstance(pos_list, list))
        for pos in pos_list:
            self.assertTrue(isinstance(pos, position))
            
        pos_list = get_position_list('[ 1, 1, 1, 10, 100')
        self.assertTrue(isinstance(pos_list, list))
        for pos in pos_list:
            self.assertTrue(isinstance(pos, position))
    
    def test_process_one_day(self):
        """Unit test to check that reasonable results are produced
        by running num_trials iterations of processing share positions"""
        positions_input = '1, 10, 100, 1000'
        positions = get_position_list(positions_input)
        num_trials = 10000
        df = process_one_day(positions = positions, 
                             num_trials = num_trials)
        for m in df.ix['means',:]:
            self.assertLess(np.abs(m), .1)
        for std,shares in zip(df.ix['stds',:], df.ix['num shares',:]):
            self.assertLess(std, 2/np.sqrt(shares))
        
    def test_constructor_rejections(self):
        """test expected behavior for incorrectly formatted inputs"""
        with self.assertRaises(ValueError):
            position('12')
        with self.assertRaises(ValueError):
            position('a')
        with self.assertRaises(ValueError):
            position('1.5')
        with self.assertRaises(ValueError):
            position('150')
        with self.assertRaises(ValueError):
            position('')
        with self.assertRaises(ValueError):
            position([])
        with self.assertRaises(ValueError):
            position([1, 10])
        with self.assertRaises(ValueError):
            position([1, 'a'])
        with self.assertRaises(ValueError):
            position([1])
        with self.assertRaises(ValueError):
            position(['p'])
        
    def test_list_interpreter_rejections(self):
        """test expected behavior for incorrectly formatted lists of inputs"""
        with self.assertRaises(ValueError):
            get_position_list('12')
        with self.assertRaises(ValueError):
            get_position_list('1, 12')
        with self.assertRaises(ValueError):
            get_position_list(', 1')
        with self.assertRaises(ValueError):
            get_position_list('[a]')
        with self.assertRaises(ValueError):
            get_position_list('')
            
            
            
            