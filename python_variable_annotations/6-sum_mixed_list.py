#!/usr/bin/env python3

"""
Modules takes a list of integers and floats and adds them together
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Method that takes a list of integers and floats and adds the list together

    Args:
        mxd_lst (List[Union[float, int]]): a list of integers and floats

    Returns:
        float: The sum of the list
    """

    return sum(mxd_lst)
