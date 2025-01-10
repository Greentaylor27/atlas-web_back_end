#!/usr/bin/env python3

"""
Module used to practice Tasks
"""
import asyncio
from typing import Awaitable, Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a task

    Args:
        max_delay (int): Delay in seconds

    Returns:
        asyncio.Task: A Task
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
