#!/usr/bin/env python3

"""
Module used to practice Async Comprehemsions
"""
import asyncio
from typing import List
generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Takes the returns of generator and makes a list

    Returns:
        List[float]: A list
    """

    results = []
    for number in generator():
        processed = await generator()
        results.append(processed)

    return results
