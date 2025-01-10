#!/usr/bin/env python3

"""
Module to practicec measuring runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the run time of wait_n

    Args:
        n (int): Number of times the program is to be executed
        max_delay (int): Time delay

    Returns:
        float: The runtime it took to execute
    """

    startTime = time.time()

    asyncio.run(wait_n(n, max_delay))

    endTime = time.time()

    total_time = endTime - startTime

    return total_time / n
