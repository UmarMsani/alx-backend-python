#!/usr/bin/env python3
"""
Module contains measure_runtime coroutine
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to measure the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    started = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    ended = time.perf_counter()
    return ended - started
