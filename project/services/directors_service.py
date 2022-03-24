from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services.base import BaseService
from flask import current_app


class DirectorsService(BaseService):
    def get_item_by_id(self, pk):
        director = DirectorDAO(self._db_session).get_by_id(pk)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self):
        directors = DirectorDAO(self._db_session).get_all()
        return DirectorSchema(many=True).dump(directors)

    def get_limit_directors(self, page):
        limit = current_app.config["ITEMS_PER_PAGE"]
        offset = (page - 1) * limit
        directors = DirectorDAO(self._db_session).get_limit(limit=limit, offset=offset)
        return DirectorSchema(many=True).dump(directors)