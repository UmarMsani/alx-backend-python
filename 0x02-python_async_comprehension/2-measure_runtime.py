#!/usr/bin/env python3
"""
Measure Runtime This module provides a coroutine called measure_runtime that measures
total runtime of executing async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to measure the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
