#!/usr/bin/env python3

"""
Module used to practice basic asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Method to wait a random delay of time

    Args:
        max_delay (int): An integer

    Returns:
        (float): A random number
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
