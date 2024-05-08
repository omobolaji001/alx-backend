#!/usr/bin/env python3
"""Defines FIFO Cache class"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """Represents FIFO Cache"""

    def __init__(self):
        """Initializes FIFOCache"""
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Adds new item to the FIFO Cache"""
        if key is None or item is None:
            return

        self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_key = self.order.popleft()
            del self.cache_data[pop_key]
            print(f"DISCARD: {pop_key}")

    def get(self, key):
        """Retrieves the item associated with key"""
        if key is None or key not in self.cache:
            return None

        return self.cache.get(key)
