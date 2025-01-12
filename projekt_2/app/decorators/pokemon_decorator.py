from flask import jsonify
from functools import wraps


def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return jsonify(response)

    return wrapper