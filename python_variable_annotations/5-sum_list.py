#!/usr/bin/env python3

"""
5-sum_list.py

First attempt at complex type annotation
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and adds them together

    Args:
        input_list (List[float]): a list of floats to be added together

    Returns:
        float: sum of the list
    """
    return sum(input_list)
