#!/usr/bin/env python3
"""Defines MRU Cache algorithm"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Represents the MRU Cache"""

    def __init__(self):
        """Initializes the MRUCache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Adds new item to MRUCache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.stack.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_key = self.stack[-2]
            del self.cache_data[pop_key]
            print(f"DISCARD: {pop_key}")

    def get(self, key):
        """Retrieves the item assigned to the key"""
        if key is None or key not in self.cache_data:
            return None

        self.stack.remove(key)
        self.stack.append(key)
        return self.cache_data.get(key)
