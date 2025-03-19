import jwt
import datetime
from flask import request, jsonify
from functools import wraps
from config import Config

def generate_token(username):
    return jwt.encode(
        {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)},
        Config.SECRET_KEY, algorithm="HS256"
    )

def verify_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        try:
            jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated
