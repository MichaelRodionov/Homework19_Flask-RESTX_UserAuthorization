from app.dao import GenreDAO
from app.dao.models.models import Genre


class GenreService:
    """
    Service is needed to work with genres views and GenreDAO
    """
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> list:
        return self.genre_dao.get_all_genres()

    def get_genre(self, genre_id) -> object:
        return self.genre_dao.get_genre_by_id(genre_id)

    def add_genre(self, data):
        genre = Genre(**data)
        genre.name = data.get('name')
        return self.genre_dao.add_genre_or_update(genre)

    def update_genre(self, genre_id, data):
        genre = self.get_genre(genre_id)
        genre.name = data.get('name')
        return self.genre_dao.add_genre_or_update(genre)

    def delete_genre(self, genre_id):
        director = self.get_genre(genre_id)
        return self.genre_dao.delete_genre(director)
