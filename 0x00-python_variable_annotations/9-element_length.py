#!/usr/bin/env python3
""" lets duck type an iterable object. """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element of lst and its length.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing
        each element of lst and its length.
    """
    return [(i, len(i)) for i in lst]
