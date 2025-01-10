#!/usr/bin/env python3

"""
More Task practice
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Method used to complete multiple tasks concurrently

    Args:
        n (int): A number of time coroutine is to be executed
        max_delay (int): Time delay in seconds

    Returns:
        List[float]: Returns a list of time taken
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    return results
