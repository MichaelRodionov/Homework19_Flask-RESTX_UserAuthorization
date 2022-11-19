from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthViews(Resource):
    @staticmethod
    def post():
        """This view is needed to user authorization"""
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if None in [username, password]:
            return "", 400
        return auth_service.generate_tokens(username, password)

    @staticmethod
    def put():
        """This view is needed to update tokens"""
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
