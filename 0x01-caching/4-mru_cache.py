#!/usr/bin/env python3
"""Subclass MRUCache, Most recently used"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Subclass of BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Puts items in the dictionary"""
        if key is None or item is None:
            return

        # Remove and reinsert key if it already exists to update its order
        if key in self.cache_data:
            self.order.remove(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Check if the cache exceeds the maximum
            mru_key = self.order[-1]
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]
            self.order.pop()

        # Add new item to the cache
        self.cache_data[key] = item
        # Add the key to the end of the order list
        self.order.append(key)

    def get(self, key):
        """Gets item from the cached dictionary"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
