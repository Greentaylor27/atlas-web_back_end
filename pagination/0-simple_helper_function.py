#!/usr/bin/env python3

"""
Module used to practice Pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Used to index the page to determine how big the page size is?

    Args:
        page (int): Have no clue
        page_size (int): How big the page is?

    Returns:
        Tuple[int, int]: should return (start_index, end_index)
    """
    if page > 1:
        start = page_size * (page - 1)
    else:
        start = 0

    end = page * page_size

    return (start, end)
