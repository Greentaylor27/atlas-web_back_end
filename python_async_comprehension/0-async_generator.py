#!/usr/bin/env python3

"""
Module used to make a random generator
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    Method randomly generators a number between 1 and 10

    Returns:
        List[float]: Uncertain if this is the right return 
    """

    for _ in range(10):
        result = await random.randrange(0, 10)
    return result
