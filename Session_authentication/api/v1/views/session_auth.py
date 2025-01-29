#!/usr/bin/env python3

"""Module for session authentication
"""
from flask import Response, request, jsonify
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
    
    return (user, email, password)


