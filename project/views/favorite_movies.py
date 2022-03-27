from flask_restx import Namespace, abort, Resource, reqparse
from project.tools.security import auth_required, auth_check
from project.services import FavoriteMoviesService
from project.setup_db import db
from project.exceptions import ItemNotFound

favorite_movies_ns = Namespace("favorites/movies")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('status', type=str)


@favorite_movies_ns.route('/')
class FavoriteMoviesView(Resource):
    @auth_required
    @favorite_movies_ns.response(200, "OK")
    def get(self):
        """Get all favorite movies"""
        user_id = auth_check().get("id")
        try:
            return FavoriteMoviesService(db.session).get_by_user_id(user_id)
        except ItemNotFound:
            abort(404, message="Movies not found")


@favorite_movies_ns.route("/<int:movie_id>")
class FavoriteMovieView(Resource):
    @auth_required
    @favorite_movies_ns.response(200, "OK")
    @favorite_movies_ns.response(404, "Movie not found")
    def post(self, movie_id: int):
        user_id = auth_check().get('id')
        return FavoriteMoviesService(db.session).create(movie_id=movie_id, user_id=user_id)

    def delete(self, movie_id: int):
        user_id = auth_check().get('id')
        return FavoriteMoviesService(db.session).delete(movie_id=movie_id, user_id=user_id)
