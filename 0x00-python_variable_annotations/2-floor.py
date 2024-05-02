#!/usr/bin/env python3
''' Description: takes float n as argument and returns floor of float
    Parameter: n: float
'''


def floor(n: float) -> int:
    ''' Returns the largest int value less than or equal to n '''
    return int(n) if n >= 0 else int(n) - 1
