#!/usr/bin/env python3
"""
Complex types - mixed list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The input list of
        integers and floats.

    Returns:
        float: The sum of the input list.
    """
    return sum(mxd_lst)
