#!/usr/bin/env python3

"""
Module to practice basic caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class for basic caching practice

    Args:
        BaseCaching (class): Needed methods for basic caching
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Updates the cache

        Args:
            key: Where something is stored i.e. ID
            item: What is being stored
        """
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the dictionary entry where data is stored

        Args:
            key: Where you want to pull from

        Returns:
            Return: Full dictionary entry. Key and value
        """
        return self.cache_data.get(key)
