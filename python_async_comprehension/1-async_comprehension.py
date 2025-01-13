#!/usr/bin/env python3

"""
Module used to practice Async Comprehemsions
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Takes the returns of generator and makes a list

    Returns:
        List[float]: A list
    """
    return [await async_generator]
