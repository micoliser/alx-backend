#!/usr/bin/env python3
""" This module contains the class BasicCache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ This class implements a basic caching system """

    def put(self, key, item):
        """ Adds a new item to the cache dictionary """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item associated with key """

        if key:
            return self.cache_data.get(key)
