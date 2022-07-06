#!/usr/bin/env python3
""" Defines a class Cache """
from functools import wraps
from typing import Union, Callable, Any
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """ Counts how many times methods of the Cache class are called """
    @wraps(method)
    def count(self, *args, **kwargs) -> Any:
        """ Increments each time a cache method is called """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, *kwargs)
    return count


class Cache:
    """ Creates a redis cache """
    def __init__(self):
        """ Initializes a redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid key and stores 'data' in Redis
            using the random key as the key

        Returns:
            The generated uuid string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """ Returns the value associated with 'key' in its original data-type
        """
        if self._redis.exists(key):
            if fn is not None:
                return fn(self._redis.get(key))
            else:
                return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ Converts a byte data type returned by the 'get' method
            to a string
        """
        return self.get(key, lambda val: val.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Converts a byte data type returned by the get method to an int
        """
        return self.get(key, lambda val: int(val))
