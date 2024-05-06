#!/usr/bin/env python3
''' Description: asynchronous co-routine that takes an int argument
                 (max_delay, with default value of 10) named wait_random
                 that waits for random delay between 0 and max_delay
                 (included and float value) seconds and eventually returns it
    Arguments: max_delay: int = 10
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay seconds and returns length of delay '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
