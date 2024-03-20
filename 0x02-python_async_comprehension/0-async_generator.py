#!/usr/bin/env python3

"""
Async Generator
This module provides a coroutine called async_generator that
yields random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields random numbers asynchronously.

    Yields:
        int: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
