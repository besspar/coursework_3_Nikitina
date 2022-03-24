from project.dao.favorite_movie import FavoriteMovieDAO
from project.schemas.favorite_movie import FavoriteMovieSchema
from project.exceptions import ItemNotFound
from project.services.base import BaseService

class FavoriteMoviesService(BaseService):
    def get_by_user_id(self, user_id):
        movies = FavoriteMovieDAO(self._db_session).get_by_user_id(user_id)
        if not movies:
            raise ItemNotFound
        return FavoriteMovieSchema(many=True).dump(movies)

    def create(self, user_id, movie_id):
        movie = FavoriteMovieDAO(self._db_session).create(user_id, movie_id)
        return FavoriteMovieSchema().dump(movie)

    def delete(self, user_id, movie_id):
        movie = FavoriteMovieDAO(self._db_session).delete(user_id, movie_id)
        return FavoriteMovieSchema().dump(movie)

