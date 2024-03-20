#!/usr/bin/env python3
"""
Async Comprehension Generates a list from an async comprehension
"""
import asyncio
from typing import List
from typing import AsyncGenerator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    Coroutine to collect 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]
