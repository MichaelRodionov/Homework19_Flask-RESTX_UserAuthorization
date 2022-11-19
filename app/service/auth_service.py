from flask import abort
from app.service.user_service import UserService
from constants import JWT_SECRET, JWT_ALGORITHM
import calendar
import datetime
import jwt


class AuthService:
    """This service is needed to work with users authentication"""
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=True):
        user = self.user_service.get_user_by_username(username)
        if user is None:
            abort(404)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)
        data = {
            'username': user.username,
            'role': user.role
        }
        # 30 min access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
        # 130 days refresh token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get('username')
        return self.generate_tokens(username, None, is_refresh=True)
