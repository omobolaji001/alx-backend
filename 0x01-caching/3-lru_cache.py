#!/usr/bin/env python3
"""Defines LRU Cache algorithm"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Represents the LRU Cache"""

    def __init__(self):
        """Initializes the LRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds new item to LRUCache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_key, pop_value = self.cache_data.popitem(last=False)
            print(f"DISCARD: {pop_key}")

    def get(self, key):
        """Retrieves the item assigned to the key"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
