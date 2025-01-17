#!/usr/bin/env python3

"""
Module used to pracetice LRU caching practices
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Least frequently used caching policy practice

    Args:
        BaseCaching (Class): Parent class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an element to the dictionary

        Args:
            key: Where something is to be stored
            item: What is being stored with Key
        """
        keys = self.cache_data.keys()

        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

        if len(keys) > BaseCaching.MAX_ITEMS:
            least_used = list(self.cache_data.keys())[0]

            print(f"DISCARD: {least_used}")
            self.cache_data.pop(0)

    def get(self, key):
        """
        Grabs an entry from a dictionary using a key

        Args:
            key: Where to find the item
        """
        return self.cache_data.get(key)
