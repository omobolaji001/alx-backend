#!/usr/bin/env python3
"""Defines LIFO Cache Algorithm"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """Represents LIFO Cache"""

    def __init__(self):
        """Initializes LIFOCache"""
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Adds new item to LIFO Cache"""
        if key is None or item is None:
            return
        self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_key = self.order[-2]
            del self.cache_data[pop_key]
            print(f"DISCARD: {pop_key}")

    def get(self, key):
        """Retrieves the item assigned to key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
