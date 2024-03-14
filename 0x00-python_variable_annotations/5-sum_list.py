#!/usr/bin/env python3
"""Add type-annotated function for summing a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the input list.
    """
    return sum(input_list)
