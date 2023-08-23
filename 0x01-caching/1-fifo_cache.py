#!/usr/bin/env python3
""" This module contains the class FIFOCache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ This class implements a FIFO caching system """

    def __init__(self):
        """ Initialize class instance """

        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            self.cache_queue.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = self.cache_queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Retrieves the item associated with key """

        if key:
            return self.cache_data.get(key)
