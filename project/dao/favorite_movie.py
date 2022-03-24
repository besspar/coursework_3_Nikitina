from sqlalchemy.orm.scoping import scoped_session
from project.dao.models import FavoriteMovie

class FavoriteMovieDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_user_id(self, user_id):
        return self._db_session.query(FavoriteMovie).filter(FavoriteMovie.user_id == user_id).all()

    def create(self, user_id, movie_id):
        obj = FavoriteMovie(user_id=user_id, movie_id=movie_id)
        self._db_session.add(obj)
        self._db_session.commit()
        return obj

    def delete(self, user_id, movie_id):
        obj = self._db_session.query(FavoriteMovie).filter(
            FavoriteMovie.user_id == user_id,
            FavoriteMovie.movie_id == movie_id
        ).one_or_none()
        self._db_session.delete(obj)
        self._db_session.commit()
        return obj
