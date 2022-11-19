from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.models import GenreSchema
from helpers import auth_required, admin_required
from implemented import genre_service


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    @auth_required
    def get():
        """This view return all genres by GET request"""
        return genres_schema.dump(genre_service.get_genres()), 200

    @staticmethod
    @admin_required
    def post():
        """This view is needed to add new genre by POST request"""
        data = request.json
        return genre_service.add_genre(data), 201


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @staticmethod
    @auth_required
    def get(genre_id):
        """This view return one genre filtered by genre_id by GET request"""
        return genre_schema.dump(genre_service.get_genre(genre_id)), 200

    @staticmethod
    @admin_required
    def put(genre_id):
        """This view is needed to update info about genre by genre_id"""
        data = request.json
        return genre_service.update_genre(genre_id, data), 204

    @staticmethod
    @admin_required
    def delete(genre_id):
        """This view is needed to delete genre by genre_id"""
        return genre_service.delete_genre(genre_id), 204
