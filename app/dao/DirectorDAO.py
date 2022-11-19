from app.dao.models.models import Director


class DirectorDAO:
    """
    This class is needed to work with database
    """
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        """
        This function is called to query all directors from database
        :return: all directors to DirectorService
        """
        directors = self.session.query(Director).all()
        return directors

    def get_director_by_id(self, director_id):
        """
        This function is called to query director from database by director id
        :param director_id:
        :return: director by director id to DirectorService
        """
        try:
            director_by_id = self.session.query(Director).get(director_id)
            return director_by_id
        except Exception as e:
            return str(e)

    def add_new_director_or_update(self, director):
        """
        This function is called to add a new director or update info about a director
        :param director:
        :return: nothing
        """
        self.session.add(director)
        self.session.commit()
        return ""

    def delete_director(self, director):
        self.session.delete(director)
        self.session.commit()
        return ""