#!/usr/bin/env python3

"""Module used to practice redis with"""
import redis
import uuid



class Cache():
    """Class used for redis"""
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    def store(self, data: any) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
