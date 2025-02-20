#!/usr/bin/env python3
"""Method to query a list of all the documents"""


def list_all(mongo_collection):
    """Writes a mongodb query to list all documents

    Args:
        mongo_collection (Collection): A mongo db list
    """
    return mongo_collection.find()
