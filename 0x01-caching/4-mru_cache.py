#!/usr/bin/env python3
""" This module contains the class MRUCache """
from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
    """ This class implements a MRU caching system """

    def __init__(self):
        """ Initialize class instance """

        super().__init__()
        self.cache_queue = {}

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = max(self.cache_queue, key=self.cache_queue.get)
                del self.cache_data[discard]
                del self.cache_queue[discard]
                print("DISCARD: {}".format(discard))
            self.cache_queue[key] = datetime.now()

    def get(self, key):
        """ Retrieves the item associated with key """

        if key and key in self.cache_data:
            self.cache_queue[key] = datetime.now()
            return self.cache_data.get(key)
