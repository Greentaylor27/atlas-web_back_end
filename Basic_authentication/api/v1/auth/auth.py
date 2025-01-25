#!/usr/bin/env python3

"""Module used for authentacation
"""
from flask import request
from typing import List
from typing import TypeVar


class Auth:
    """Class used to store authentactation methods
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Set up for a later task

        Args:
            path (str): Urls that require authentacation
            excluded_paths (List[str]): These do not

        Returns:
            bool: Returns False
        """

        if path == None:
            return True
        if excluded_paths == None or excluded_paths == []:
            return True
        
        if path.endswith("/"):
            pass
        else:
            path = path + "/"
        
        for items in excluded_paths:
            if items == path:
                return False


    def authorization_header(self, request=None) -> str:
        """Set up for later task

        Args:
            request (_type_, optional): Flask object. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
