from flask import Flask
from config import Config
from setup_db import db
from flask_restx import Api
from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns


def create_app(config_object: Config):
    """
    This function is called to create Flask application
    :param config_object: Config
    :return: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    """
    This function is called to register extensions init database and create api
    :param app: Flask application
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(app, db)


def create_data(app, database):
    """Creating table"""
    with app.app_context():
        database.create_all()


application = create_app(Config())


@application.errorhandler(404)
def get_404_error(error):
    """404 errorhandler"""
    return 'Page not found'


@application.errorhandler(500)
def get_500_error(error):
    """500 errorhandler"""
    return 'Server error'


@application.errorhandler(400)
def get_400_error(error):
    """400 errorhandler"""
    return 'Bad request'


@application.errorhandler(401)
def get_401_error(error):
    """401 errorhandler"""
    return 'You are not authorized'


@application.errorhandler(403)
def get_403_error(error):
    """403 errorhandler"""
    return 'Sorry, access is denied'


if __name__ == '__main__':
    application.run(port=5050)
