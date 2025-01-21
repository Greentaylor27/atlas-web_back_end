#!/usr/bin/env python3

"""
Module used to practice filtered logging
"""
import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator:str) -> str:
    """
    

    Args:
        fields (List[str]): List of strings that need to be obfuscated
        redaction (str): Sting used to replace the string
        message (str): The log line
        separator (str): a character to seperator the message in the log line

    Returns:
        str: The log message obfuscated
    """
    re.sub(message, redaction, message)
    return message

