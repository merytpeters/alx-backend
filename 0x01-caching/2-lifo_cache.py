#!/usr/bin/env python3
"""Subclass LIFOCache"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Subclass of BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Puts items in the dictionary"""
        if key is None or item is None:
            return

        # Remove and reinsert key if it already exists to update its order
        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Check if the cache exceeds the maximum
            recent_key = next(reversed(self.cache_data))
            print(f"DISCARD: {recent_key}")
            del self.cache_data[recent_key]

        # Add new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Gets item from the cached dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
