from app.dao.models.models import Genre


class GenreDAO:
    """
    This class is needed to work with database
    """
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        """
        This function is called to query all genres from database
        :return: all genres to GenreService
        """
        genres = self.session.query(Genre).all()
        return genres

    def get_genre_by_id(self, genre_id):
        """
        This function is called to query genre from database by genre id
        :param genre_id:
        :return: genre by genre id to GenreService
        """
        try:
            genre = self.session.query(Genre).get(genre_id)
            return genre
        except Exception as e:
            return str(e)

    def add_genre_or_update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete_genre(self, genre):
        self.session.delete(genre)
        self.session.commit()

