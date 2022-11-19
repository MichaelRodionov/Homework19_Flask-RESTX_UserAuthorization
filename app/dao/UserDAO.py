from sqlalchemy import desc

from app.dao.models.models import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid) -> object:
        """
        This function is called to query user by user_id
        :param uid:
        :return: user object
        """
        return self.session.query(User).get(uid)

    def get_by_username(self, username) -> object:
        """
        This function is needed to query user by username
        :param username:
        :return: user object
        """
        return self.session.query(User).filter(User.username == username).first()

    def get_all_users(self) -> list[object]:
        """
        This function is needed to query all users
        :return: list of users
        """
        return self.session.query(User).all()

    def create_user(self, data):
        """
        This function is needed to add a new user to the database
        :param data:
        :return: user_id
        """
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        user_id = self.session.query(User.id).order_by(desc(User.id)).limit(1).all()
        return user_id

    def delete(self, uid):
        """
        This function is needed to delete user from the database
        :param uid:
        :return: nothing
        """
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update_data(self, data):
        """
        This function is needed to update user attributes
        :param data:
        :return: nothing
        """
        user = self.get_one(data.get('uid'))
        user.name = data.get('name')
        user.password = data.get('password')
        self.session.add(user)
        self.session.commit()
