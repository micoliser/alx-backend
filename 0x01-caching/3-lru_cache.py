#!/usr/bin/env python3
""" This module contains the class LRUCache """
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """ This class implements a LRU caching system """

    def __init__(self):
        """ Initialize class instance """

        super().__init__()
        self.cache_queue = {}

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            self.cache_queue[key] = datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = min(self.cache_queue, key=self.cache_queue.get)
                del self.cache_data[discard]
                del self.cache_queue[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Retrieves the item associated with key """

        if key and key in self.cache_data:
            self.cache_queue[key] = datetime.now()
            return self.cache_data.get(key)
