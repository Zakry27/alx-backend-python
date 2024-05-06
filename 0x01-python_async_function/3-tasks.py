#!/usr/bin/env python3
''' Description: Writes function (do not create async function, use
                 regular function syntax to do this) task_wait_random
                 that takes integer max_delay and returns asyncio.Task.
    Arguments: max_delay: int
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    ''' Returns asyncio.Task object '''
    return asyncio.create_task(wait_random(max_delay))
