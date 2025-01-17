#!/usr/bin/env python3

"""
Module to practice FIFO caching practices
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
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
        keys = self.cache_data.keys()
        last_key = list(keys)

        if key and item:
            self.cache_data[key] = item

        if len(keys) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {last_key[-1]}")
            self.cache_data.pop(last_key[-1])

    def get(self, key):
        """
        returns the entry using the key

        Args:
            key: The entry you are trying to look for
        """
        return self.cache_data.get(key)
