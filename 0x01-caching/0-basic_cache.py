#!/usr/bin/env python3
"""Defines BasicCache class that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents BasicCache"""

    def __init__(self):
        """Initializes BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Adds new item to the Cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Returns the item assigned to key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
