#!/usr/bin/env python3
""" Defines a class Cache """
from typing import Union, Callable
import redis
import uuid


class Cache:
    """ Creates a redis cache """
    def __init__(self):
        """ Initializes a redis instance """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid key and stores 'data' in Redis
            using the random key as the key

        Returns:
            The generated uuid string
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """ Returns the value associated with 'key' in its original data-type
        """
        if self.__redis.exists(key):
            if fn is not None:
                return fn(self.__redis.get(key))
            else:
                return self.__redis.get(key)

    def get_str(self, key: str) -> str:
        """ Converts a byte data type returned by the 'get' method
            to a string
        """
        return self.get(key, lambda val: val.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Converts a byte data type returned by the get method to an int
        """
        return self.get(key, lambda val: int(val))
