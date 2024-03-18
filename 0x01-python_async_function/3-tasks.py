#!/usr/bin/env python3
"""Create a task"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that executes the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        Task: An asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
