#!/usr/bin/env python3

"""Module used to practice redis with"""
import redis



class Cache():
    """Class used for redis"""
    def __init__(self):
        self._redis = redis.Redis(host='localhost')
        
