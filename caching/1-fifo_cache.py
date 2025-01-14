#!/usr/bin/env python3

"""
Module to practice FIFO caching practices
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class for FIFO caching practices

    Args:
        BaseCaching: parent class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds a new entry to the dictionary known as cache

        Args:
            key: Where something is to be stored
            item: What is being stored
        """
        if key and item:
            self.cache_data[key] = item

        keys = self.cache_data.keys()

        if len(keys) >= BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {keys[0]}")
            self.cache_data.popitem(0)

    def get(self, key):
        """
        Grabs the dictionary entry using the key

        Args:
            key: Where to find the item

        Returns:
            All data associated with the key
        """
        return self.cache_data.get(key)
