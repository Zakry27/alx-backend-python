#!/usr/bin/env python3
''' Description: accepts list input_list of floats as argument and
    returns their sum as float.
    Arguments: input_list: List[float]
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Output of sum of all elements in input_list. '''
    return sum(input_list)
