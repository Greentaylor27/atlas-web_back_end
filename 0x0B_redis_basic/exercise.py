#!/usr/bin/env python3

"""Module used to practice redis with"""
import redis
import uuid
from typing import Union, Callable, Optional



class Cache():
    """Class used for redis"""
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        retrieved_value = self._redis.get(key)

        if not retrieved_value:
            return None
        
        if fn:
            return fn(retrieved_value)
        
        return retrieved_value

    def get_str(self, key: str):
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key):
        return self.get(key, int)
