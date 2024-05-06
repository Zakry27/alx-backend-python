#!/usr/bin/env python3
''' Description: Creates measure_time function with ints n and
                 max_delay as arguments that measures total execution
                 time for wait_n(n, max_delay), and then it returns total_time / n.
                 Your function should return float.
    Arguments: n: int, max_delay: int
'''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Return execution time for wait_n given `n` and `max_delay`. '''
    time_0 = time()
    run(wait_n(n, max_delay))
    time_1 = time()
    elapsed_time = time_1 - time_0
    return elapsed_time / n
