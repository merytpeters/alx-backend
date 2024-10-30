#!/usr/bin/env python3
"""Subclass FIFOCache"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Subclass of BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Puts items in the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Check if the cache exceeds the maximum
            oldest_key = next(iter(self.cache_data))
            print(f"DISCARD: {oldest_key}")
            del self.cache_data[oldest_key]

        # Add new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Gets item from the cached dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
