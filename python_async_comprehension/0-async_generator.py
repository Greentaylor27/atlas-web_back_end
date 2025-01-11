#!/usr/bin/env python3

"""
Module used to make a random generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Method randomly generators a number between 1 and 10

    Returns:
        List[float]: Uncertain if this is the right return
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
