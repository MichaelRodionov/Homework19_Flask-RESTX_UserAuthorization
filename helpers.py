import jwt
from flask import request, abort
from constants import JWT_SECRET, JWT_ALGORITHM


def admin_required(func):
    """Check admin authorization decorator"""
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get('role')
            if role != 'Admin':
                abort(403)
        except Exception as e:
            if '403 Forbidden' in str(e):
                abort(403)
            if '401 Unauthorized' in str(e):
                abort(401)
            else:
                abort(400)
        return func(*args, **kwargs)
    return wrapper


def auth_required(func):
    """Check user authorization decorator"""
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode Error: ', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper
