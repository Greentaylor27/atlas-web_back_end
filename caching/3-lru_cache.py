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
        """adds to the stack

        Args:
            key (Any): Where something is being stored
            item (Any): What is being stored
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f'DISCARD: {lru_key}')
    
    def get(self, key):
        """finds the value using a key

        Args:
            key (Any): Location where the data is being stored
        """
        try:
            value = self.cache_data[key]
            return value
        except Exception:
            return None
