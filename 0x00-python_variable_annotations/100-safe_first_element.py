#!/usr/bin/env python3
""" duck typing - first element of a sequence. """
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of lst if it exists, otherwise return None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Optional[Any]: The first element of lst if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
