#!/usr/bin/env python3

"""
Module used to practice basic asynchronous coroutine
"""
import random, asyncio


async def wait_random(max_delay: int = 10):
    """
    Method to wait a random delay of time

    Args:
        max_delay (int): 
    """
        
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
