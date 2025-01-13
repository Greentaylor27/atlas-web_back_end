#!/usr/bin/env python3

"""
More practice with Async Comprehension
"""
import asyncio
import time
comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure run time for list comprehension

    Returns:
        float: seconds it will take to complete
    """

    start_time = time.time()

    tasks = [asyncio.create_task(comprehension()) for _ in range(4)]
    results = await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time
