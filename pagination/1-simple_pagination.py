#!/usr/bin/env python3

"""
Module to practice more simple pagination
"""
from typing import Tuple, List
import csv
import math


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

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
