#!/usr/bin/env python3
""" More involved type annotations. """
from typing import Mapping, Any, TypeVar, Union, Sequence


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Return the value corresponding to the given key in the dictionary.
    If the key is not present, return the default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the
        key is not found (default is None).

    Returns:
        Union[Any, T]: The value corresponding to the given key if present,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
