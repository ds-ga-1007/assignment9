from .Position_functions import *

def get_position_list(share_list):
    """get list of positions from string of positons, or raise a ValueError"""
    if not isinstance(share_list, str):
        raise ValueError("get_interval_list only takes in strings. \
                         Received %s" % (type(share_list)))
    cleaned_input = share_list.strip()
    no_brackets = cleaned_input.replace('[','').replace(']','')
    split_positions = str.split(no_brackets, ',')
    positions = []
    for num_shares_input in split_positions:
        num_shares_processed = get_integer_if_possible(num_shares_input)
        positions.append(position(num_shares_processed))
    return positions

class position(object):
    """This class represents a position, which is a distribution
    of an initial investment, evenly distributed among num_shares
    separate shares that are invested independently"""
    def __init__(self, num_shares):
        """All positions contain 1000 montetary units, among num_shares
        shares each worth share_value"""
        if not isinstance(num_shares, int):
            raise ValueError("num_shares must be an integer")
        INITIAL_INVESTMENT = 1000
        self.num_shares = num_shares
        self.share_value = INITIAL_INVESTMENT / num_shares
        self.total_value = 0
        
    def bet_shares_independently(self, probabilty = 0.51):
        """bet all shares with probability = probability.
        Tally the total outcome value of the investment in 
        self.total_value"""
        for share in range(self.num_shares):
            if weightedcoinflip(probabilty = probabilty):
                self.total_value += self.share_value * 2
            
    @property
    def num_shares(self):
        return self._num_shares

    @num_shares.setter
    def num_shares(self, num_shares):
        if not num_shares in [1, 10, 100, 1000]:
            raise ValueError('%s needs to be an exponent \
                             of 10 between 1 and 1000' % (num_shares))
        self._num_shares = num_shares