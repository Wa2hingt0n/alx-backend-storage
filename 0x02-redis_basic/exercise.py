#!/usr/bin/env python3
""" Defines a class Cache """
from typing import Union
import redis
import uuid


class Cache:
    """ Creates a redis cache """
    def __init__(self):
        """ Initializes a redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid key and stores 'data' in Redis
            using the random key as the key

        Returns:
            The generated uuid string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
