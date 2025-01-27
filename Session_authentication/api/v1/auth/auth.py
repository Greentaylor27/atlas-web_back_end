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
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if excluded_paths == []:
            return True

        if path.endswith("/"):
            pass
        else:
            path = path + "/"

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Set up for later task

        Args:
            request (_type_, optional): Flask object. Defaults to None.

        Returns:
            str: _description_
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
