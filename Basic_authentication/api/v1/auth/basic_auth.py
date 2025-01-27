#!/usr/bin/env python3

"""Module used for Basic Authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class used for basic authentication

    Args:
        Auth (class): Parent class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the bases64 of the authorization header

        Args:
            authorization_header (str): the basic authorization header

        Returns:
            str: the base64 of the authorization header
        """
        header_validation = isinstance(authorization_header, str)

        if not header_validation:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        
        return authorization_header[6:]
