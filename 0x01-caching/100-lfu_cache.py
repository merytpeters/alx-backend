#!/usr/bin/env python3
"""Subclass LFUCache, Least frequently used"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Subclass of BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()
        self.frequency = {}
        self.order = []
        self.min_frequency = 1

    def remove_least_frequently_used(self):
        """Remove least frequently used item"""
        min_freq_keys = [
            k for k, v in self.frequency.items()
            if v == self.min_frequency
        ]

        if not min_freq_keys:
            return

        # if there's more thsan one key apply LRU
        if len(min_freq_keys) > 1:
            lru_key = next(key for key in self.order if key in min_freq_keys)
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            self.order.remove(lru_key)
        else:
            lfu_key = min_freq_keys[0]
            print(f"DISCARD: {lfu_key}")
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            self.order.remove(lfu_key)

        if self.frequency:
            self.min_frequency = min(self.frequency.values())

    def put(self, key, item):
        """Puts items in the dictionary"""
        if key is None or item is None:
            return

        # Remove and reinsert key if it already exists to update its order
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            # move the accessed keyy to the end of the order list (LRU)
            self.order.remove(key)
            self.order.append(key)
            return

        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Check if the cache exceeds the maximum
            self.remove_least_frequently_used()

        # Add new item to the cache
        self.cache_data[key] = item
        self.frequency[key] = 1
        self.order.append(key)

    def get(self, key):
        """Gets item from the cached dictionary"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list
        self.order.remove(key)
        self.order.append(key)
        self.frequency[key] += 1
        return self.cache_data[key]
