#!/usr/bin/env python3

"""
Module takes a string and an int or float as an argument and returns a tuple
"""
from typing import Tuple, Union, Optional


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Method that takes two arguments and returns them as a tuple

    Args:
        k (str): A word or sentence
        v (Union[int  |  float]): A number

    Returns:
        Tuple: A tuple containing k and v
    """
    empty_tuple = (k, v);
    
    
    return empty_tuple
