#!/usr/bin/env python3
""" This module contains the class LIFOCache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ This class implements a LIFO caching system """

    def __init__(self):
        """ Initialize class instance """

        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.cache_queue.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_queue.append(key)

    def get(self, key):
        """ Retrieves the item associated with key """

        if key:
            return self.cache_data.get(key)
