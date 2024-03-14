#!/usr/bin/env python3
""" Complex types - functions.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    return lambda x: x * multiplier
