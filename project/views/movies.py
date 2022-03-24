from flask_restx import abort, Namespace, Resource, reqparse
from project.tools.security import auth_required
from project.exceptions import ItemNotFound
from project.services.movies_service import MovieService
from project.setup_db import db

movies_ns = Namespace("movies")
parser = reqparse.RequestParser()
parser.add_argument("page", type=int)
parser.add_argument('status', type=str)

@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.expect(parser)
    @auth_required
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all"""
        req_agrs = parser.parse_args()
        if any(req_agrs.values()):
            return MovieService(db.session).get_filter_movies(req_agrs)
        else:
            return MovieService(db.session).get_all_movies()


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @auth_required
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        """Get one by id"""
        try:
            return MovieService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")

