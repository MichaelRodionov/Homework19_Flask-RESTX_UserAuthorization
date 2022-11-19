from sqlalchemy import desc
from constants import LIMIT_VALUE, OFFSET_VALUE
from app.dao.models.models import Movie


class MovieDAO:
    """
    This class is needed to work with database
    """
    def __init__(self, session):
        self.session = session

    def get_all_movies(self, director_id=None, genre_id=None, year=0, page=None):
        """
        This function is called to query all movies or movies sorted by Director or/and Genre
        :return: all movies or movies sorted by director/genre/year to MovieService
        """
        movies_query = self.session.query(Movie)
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)
        if year is not None:
            movies_query = movies_query.filter(Movie.year == year)
        else:
            if page and int(page) > 0:
                movies_query = movies_query.limit(LIMIT_VALUE).offset(OFFSET_VALUE * (int(page) - 1))
        return movies_query.all()

    def get_movie_by_id(self, movie_id):
        """
        This function is called to query movie from database by movie_id
        :param movie_id:
        :return: return movie by movie_id to MovieService
        """
        movie_by_id = self.session.query(Movie).get(movie_id)
        return movie_by_id

    def add_new_movie(self, new_movie):
        """
        This function is called to add new movie to database
        """
        self.session.add(new_movie)
        self.session.commit()
        new_movie = self.session.query(Movie.id).order_by(desc(Movie.id)).limit(1).all()
        return new_movie

    def edit_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
        return ""

    def delete_movie(self, movie_id):
        """
        This function is called to delete movie with movie_id from database
        :param movie_id:
        """
        movie_to_delete = self.session.query(Movie).get(movie_id)
        self.session.delete(movie_to_delete)
        self.session.commit()
        return ""
