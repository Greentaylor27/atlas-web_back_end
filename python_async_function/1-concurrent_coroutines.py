#!/usr/bin/env python3

"""
Module used to practice multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes wait_random and does it a number of time for a certain delay

    Args:
        n (int): Number of times task is done
        max_delay (int, optional): Delay. Defaults to 10.

    Returns:
        List[float]: List of floats
    """
    
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    
    return sorted(results)
