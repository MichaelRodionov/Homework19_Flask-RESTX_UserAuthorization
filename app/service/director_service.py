from app.dao import DirectorDAO
from app.dao.models.models import Director


class DirectorService:
    """
    Service is needed to work with directors views and DirectorDAO
    """
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> list[object]:
        return self.director_dao.get_all_directors()

    def get_director(self, director_id) -> object:
        return self.director_dao.get_director_by_id(director_id)

    def add_director(self, data):
        director = Director(**data)
        director.name = data.get('name')
        return self.director_dao.add_new_director_or_update(director)

    def update(self, director_id, data):
        director = self.get_director(director_id)
        director.name = data.get('name')
        return self.director_dao.add_new_director_or_update(director)

    def delete(self, director_id):
        director = self.get_director(director_id)
        return self.director_dao.delete(director)

