#!/usr/bin/env python3
''' Description: Build upon following code with correct
                 duck-typed annotations
    Parameters: lst: Sequence[Any]
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Outputs first element of lst if there is any, otherwise None. '''
    if lst:
        return lst[0]
    else:
        return None
