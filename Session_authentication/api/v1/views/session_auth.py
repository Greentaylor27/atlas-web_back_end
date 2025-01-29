#!/usr/bin/env python3

"""Module for session authentication
"""
from flask import Response, request, jsonify, abort
from api.v1.views import app_views, User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login for site
    """
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    valid_password = user.is_valid_password(password)

    if not valid_password:
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    if not session_id:
        abort(500)

    user_json = user.to_json()

    response = jsonify(user_json)

    session_name = os.getenv('SESSION_NAME', 'session_id')
    response.set_cookie(session_name, session_id)
    return response
