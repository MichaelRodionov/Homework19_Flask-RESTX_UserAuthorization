from flask import request
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.dao import MovieDAO
from app.dao.models.models import Movie


class MovieService:
    """
    Service is needed to work with movies views and MovieDAO
    """
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list:
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        page = request.args.get('page')
        return self.movie_dao.get_all_movies(director_id, genre_id, year, page)

    def add_movie(self):
        """
        This
        :return:
        """
        data = request.json
        new_movie = Movie(**data)
        id_new_movie = self.movie_dao.add_new_movie(new_movie)[0][0]
        endpoint = f"/movies/{str(id_new_movie)}"
        return endpoint

    def get_one_movie(self, movie_id: int):
        return self.movie_dao.get_movie_by_id(movie_id)

    def update_movie_full(self, movie_id: int):
        data = request.json
        movie_to_update = self.get_one_movie(movie_id)
        movie_to_update.title = data.get('title')
        movie_to_update.description = data.get('description')
        movie_to_update.trailer = data.get('trailer')
        movie_to_update.year = data.get('year')
        movie_to_update.rating = data.get('rating')
        return self.movie_dao.edit_movie(movie_to_update)

    def update_movie_partial(self, movie_id: int):
        data = request.json
        movie_to_edit = self.get_one_movie(movie_id)
        if 'title' in data:
            movie_to_edit.title = data.get('title')
        if 'description' in data:
            movie_to_edit.description = data.get('description')
        if 'trailer' in data:
            movie_to_edit.trailer = data.get('trailer')
        if 'year' in data:
            movie_to_edit.year = data.get('year')
        if 'rating' in data:
            movie_to_edit.rating = data.get('rating')
        return self.movie_dao.edit_movie(movie_to_edit)

    def delete_one_movie(self, movie_id: int):
        try:
            return self.movie_dao.delete_movie(movie_id), 204
        except UnmappedInstanceError:
            return "nothing to delete"
