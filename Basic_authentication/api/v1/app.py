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
    if auth is None:
        return

    if auth and auth.require_auth(request.path, ['/api/v1/status/',
                                                 '/api/v1/unauthorized/',
                                                 '/api/v1/forbidden/']):
        if auth.authorization_header(request) is None:
            abort(401)
            return None
        if auth.current_user(request) is None:
            abort(403)
            return None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
