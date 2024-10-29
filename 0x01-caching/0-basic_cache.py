#!/usr/bin/env python3
"""Subclass BasicCache Basic Dictionary"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Subclass of BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Puts items in the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets item from the cached dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
