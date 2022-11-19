import base64
import hashlib
import hmac
from app.dao import UserDAO
from constants import PWD_SALT, PWD_ITERATIONS, HASH_ALGORITHM, PWD_ENCODE


class UserService:
    """Service is needed to work with users views and UserDAO"""
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_users(self):
        return self.user_dao.get_all_users()

    def get_one_user(self, uid):
        return self.user_dao.get_one(uid)

    def get_user_by_username(self, username):
        return self.user_dao.get_by_username(username)

    def create_user(self, data):
        data['password'] = self.make_user_password_hash(data.get('password'))
        id_new_user = self.user_dao.create_user(data)[0][0]
        return id_new_user

    def update(self, data):
        data['password'] = self.make_user_password_hash(data.get('password'))
        user_id = self.user_dao.update_data(data)
        return user_id

    def delete_user(self, uid):
        return self.user_dao.delete(uid)

    @staticmethod
    def make_user_password_hash(password: str):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            HASH_ALGORITHM,
            password.encode(PWD_ENCODE),
            PWD_SALT,
            PWD_ITERATIONS
        ))

    @staticmethod
    def compare_passwords(password_hash, other_password) -> bool:
        return hmac.compare_digest(base64.b64decode(password_hash), hashlib.pbkdf2_hmac(
            HASH_ALGORITHM,
            other_password.encode(PWD_ENCODE),
            PWD_SALT,
            PWD_ITERATIONS
        ))
