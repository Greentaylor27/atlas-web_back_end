#!/usr/bin/env python3

"""Module to practice Hashing and Salting
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Salts and hashes a password

    Args:
        password (str): A password

    Returns:
        bytestr: A password in bytestr
    """

    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks the validity of a hashed password

    Args:
        hashed_password (bytes): Hashed password
        password (str): password

    Returns:
        bool: True or False
    """
    bytes = password.encode('utf-8')
    if bcrypt.checkpw(bytes, hashed_password):
        return True
    else:
        return False
