#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type:
    if auth_type == "auth":
        from api.v1.auth.auth import Auth
        auth = Auth()
    if auth_type == "basic_auth":
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()
    if auth_type == "session_auth":
        from api.v1.auth.session_auth import SessionAuth
        auth = SessionAuth()


@app.errorhandler(403)
def youre_forbidden(error):
    """Forbidden

    Args:
        error (403): forbidden

    Returns:
        Jsonified response
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def not_authorized(error):
    """not authorized user

    Args:
        error: should be 401 error

    Returns:
        JSON
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request():
    """Runs before each request is made

    Returns:
        _type_: Uncertain
    """
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']

    if auth is None:
        return

    request.current_user = auth.current_user(request)

    if auth and auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) and auth.session_cookie(request):
            abort(401)
        if request.current_user is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
