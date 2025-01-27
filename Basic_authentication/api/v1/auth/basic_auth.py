#!/usr/bin/env python3

"""Module used for Basic Authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """Class used for basic authentication

    Args:
        Auth (class): Parent class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """decodes base64 authorization header
        """
        header_validation = isinstance(base64_authorization_header, str)

        if not header_validation:
            return
        try:
            decoded_header = base64.b64decode(base64_authorization_header)
            return decoded_header.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) ->\
                                (str, str):
        """Pulls user credentials

        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        credential_validation = isinstance(decoded_base64_authorization_header,
                                           str)

        if not credential_validation:
            return (None, None)

        includes_colon = decoded_base64_authorization_header.find(":")
        if includes_colon == -1:
            return (None, None)

        # was told to assume that decoded_base64 only had one :
        split_header = decoded_base64_authorization_header.split(":")

        email = split_header[0]
        password = split_header[1]

        return (email, password)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) ->\
            TypeVar('User'):
        """from the credentials return the instance of the user
        """
        email_validation = isinstance(user_email, str)
        password_validation = isinstance(user_pwd, str)

        if not email_validation and not password_validation:
            return None

        try:
            user = User.search({'email': user_email})
            if user and user[0]:
                if user[0].is_valid_password(user_pwd):
                    return user[0]
        except Exception:
            return None
