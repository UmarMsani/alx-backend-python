#!/usr/bin/env python3
"""Complex types - string and int/float to tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the
        square of v as a float.
    """
    return (k, v**2)
