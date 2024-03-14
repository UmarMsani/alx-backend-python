#!/usr/bin/env python3
""" Type Checking. """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return list containing each element of lst repeated by the factor
    Args:
        lst (Tuple): The input tuple.
        factor (int): The factor by which each element
        should be repeated (default is 2).
    Returns:
        List: A list containing each element of lst
        repeated by the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
