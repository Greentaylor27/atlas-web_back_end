#!/usr/bin/env python3

"""
Module to practice Hypermedia pagination
"""
from typing import Tuple, List
import csv
import math


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
        """
        Gets the data set to a page

        Args:
            page (int): _description_. Defaults to 1.
            page_size (int): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """

        # Assertion tests
        assert isinstance(page, int) and page > 0, \
            "page must be a positive int"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a postive int"

        # Logic
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Makes a dictionary from the hypermedia

        Args:
            page (int): Number of data points. Defaults to 1.
            page_size (int): How big the amount of data points are. Defaults to 10
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # next and previous page validation

        if page < total_pages:
            next_page = page + 1
        else: 
            next_page = None

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        page_data = {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
        return page_data



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
