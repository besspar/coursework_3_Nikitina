from project.dao.models.base import BaseMixin
from project.setup_db import db

class FavoriteMovie(BaseMixin, db.Model):
    __tablename__ = "favorite_movies"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("users")
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    movie = db.relationship("movies")

    def __repr__(self):
        return "<FavoriteMovie>"