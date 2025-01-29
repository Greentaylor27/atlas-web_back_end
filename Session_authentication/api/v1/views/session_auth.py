#!/usr/bin/env python3

"""Module for session authentication
"""
from flask import Response, request, jsonify, abort
from api.v1.views import app_views, User



@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login for site
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400
    
    try:
        user = User.search(email)
    except Exception:
        return jsonify({ "error": "no user found for this email"}), 404
    
    user = user[0]

    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    
    else:
        from api.v1.app import auth

        session = auth.create_session(user.id)

        if not session:
            abort(500)
        user_json = user.to_json()
