#!/usr/bin/env python3

"""
Async Comprehension
This module provides a coroutine called async_comprehension that collects
10 random numbers using async comprehension over async_generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine to collect 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]
