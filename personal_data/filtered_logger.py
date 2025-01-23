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
    pattern = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})|(\d{2}/\d{2}/\d{4})")
    return re.sub(pattern, redaction, message)

