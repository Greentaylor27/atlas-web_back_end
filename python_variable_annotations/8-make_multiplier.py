#!/usr/bin/env python3

"""
Module sets a float as a multiplier to be used later
"""
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float and sets it as a multiplier

    Args:
        multiplier (float): A number to be used as a multiplier

    Returns:
        Callable[[float], float]: a function to be used 
    """
    def use_multiplier(number: float) -> float:
        """
        uses multiplier set by make_multiplier

        Args:
            number (float): Number to be multiplied by

        Returns:
            float: product of number and multiplier
        """
        return number * multiplier
    
    return use_multiplier
