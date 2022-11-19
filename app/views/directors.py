from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.models import DirectorSchema
from helpers import auth_required
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    @auth_required
    def get():
        """This view return all directors by GET request"""
        return directors_schema.dump(director_service.get_directors()), 200

    @staticmethod
    def post():
        """This view is needed to add new director by POST request"""
        data = request.json
        return director_service.add_director(data), 201


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @staticmethod
    @auth_required
    def get(director_id):
        """This view return one director filtered by director_id by GET request"""
        return directors_schema.dump(director_service.get_director(director_id)), 200

    @staticmethod
    def put(director_id):
        """This view is needed to update info about director by director_id"""
        data = request.json
        return director_service.update(director_id, data)

    @staticmethod
    def delete(director_id):
        """This view is needed to delete director by director_id"""
        return director_service.delete(director_id), 204
