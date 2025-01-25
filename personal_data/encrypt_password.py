#!/usr/bin/env python3

"""Module to practice Hashing and Salting
"""
import bcrypt



def hash_password(password: str) -> bytestr :
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
