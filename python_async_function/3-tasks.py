#!/usr/bin/env python3

"""
Module used to practice Tasks
"""
import asyncio
from typing import Awaitable, Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Don't really quite know what this is suppose to do I just know it returns a task

    Args:
        max_delay (int): The number being passed off to wait_random

    Returns:
        Awaitable[float]: Not even sure this is the correct annotation for this return
    """

    coro = asyncio.run(wait_random(max_delay))
    task = asyncio.create_task(coro)
    return task
