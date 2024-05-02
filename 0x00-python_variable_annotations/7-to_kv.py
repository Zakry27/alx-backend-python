#!/usr/bin/env python3
''' Description: Accepts string k and int OR float v as arguments and
                 returns tuple. The first element of tuple is
                 string k.
                 The second element is square of int/float v and
                 should be annotated as float.
    Parameters: k: str, v: Union[int, float]
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Outputs tuple consisting of k and square of v. '''
    return (k, v * v)
