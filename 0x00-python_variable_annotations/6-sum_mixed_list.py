#!/usr/bin/env python3
''' Description: accepts list mxd_lst of floats and integers and
    returns their sum as float.
    Parameters: mxd_lst: List[Union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Outputs the sum of elements of mxd_list. '''
    return sum(mxd_lst)
