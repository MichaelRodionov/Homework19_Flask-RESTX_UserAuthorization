from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.models import UserSchema
from implemented import user_service
from helpers import admin_required


user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    @staticmethod
    def get():
        """This view is needed to get all users"""
        return users_schema.dump(user_service.get_users()), 200

    @staticmethod
    def post():
        """This view is needed to add new user"""
        data = request.json
        user_id = user_service.create_user(data)
        return "", 201, {'Location': f"/users/{user_id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @staticmethod
    @admin_required
    def delete(uid):
        """This view is needed to delete user. Only for admin!"""
        return user_service.delete_user(uid), 204
