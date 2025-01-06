#!/usr/bin/env python3

"""
Learning duck typing
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    """
    determines the length of an element

    Args:
        lst (Iterable): an iterable list

    Returns:
        List[Tuple[Sequence, int]]: something
    """
    return[(i, len(i)) for i in lst]
