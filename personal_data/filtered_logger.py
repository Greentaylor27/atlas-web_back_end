#!/usr/bin/env python3

"""
Module used to practice filtered logging
"""
import logging
from typing import List
import re
import os
from mysql import connector

PII_FIELDS = ('name', 'ssn', 'password', 'email', 'phone')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    obfuscate a data point

    Args:
        fields (List[str]): List of strings that need to be obfuscated
        redaction (str): Sting used to replace the string
        message (str): The log line
        separator (str): a character to seperator the message in the log line

    Returns:
        str: The log message obfuscated
    """
    for field in fields:
        pattern = rf'(?i){field}=[^ {separator}]+'
        message = re.sub(pattern, rf'{field}={redaction}', message)

    return message


def get_logger() -> logging.Logger:
    """Setting up a logger
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    console_handler = logging.StreamHandler()
    
    formatter = RedactingFormatter.format()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

def get_db() -> mysql.connector.connection.MySQLConnection:
    """connects to a secure database using environ variables

    Returns:
        mysql.connector.connection.MySQLConnection: An object
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    conn = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    return conn

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method for formating log message

        Args:
            record (logging.LogRecord): data point containing attributes

        Returns:
            str: Actual log message after obfuscation
        """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.msg,
                                  self.SEPARATOR)
        return super().format(record)
