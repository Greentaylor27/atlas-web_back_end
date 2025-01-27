#!/usr/bin/env python3

"""Class used for session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Class use for session authentication

    Args:
        Auth (Object): Class to be inherited from
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session based off the user ID

        Args:
            user_id (str, optional): The user's ID. Defaults to None.

        Returns:
            str: Session ID
        """

        user_validation = isinstance(user_id, str)

        if not user_validation:
            return None

        session_id = uuid.uuid4()

        self.user_id_by_session_id[session_id] = user_id

        return session_id
