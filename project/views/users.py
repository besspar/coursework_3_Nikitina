from flask import request
from flask_restx import Namespace, abort, Resource, reqparse
from project.tools.security import auth_required
from project.services.users_service import UsersService
from project.setup_db import db
from project.exceptions import ItemNotFound

users_ns = Namespace('users')
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)


@users_ns.route('/')
class UsersView(Resource):
    @users_ns.expect(parser)
    @auth_required
    @users_ns.response(200, "OK")
    def get(self):
        """Get all"""
        page = parser.parse_args().get("page")
        if page:
            return UsersService(db.session).get_limit_users(page)
        return UsersService(db.session).get_all_users()


@users_ns.route('/<int:user_id>')
class UserView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Movie not found")
    def get(self, user_id: int):
        """Get one by id"""
        try:
            return UsersService(db.session).get_user_by_id(user_id)
        except ItemNotFound:
            abort(404, message="User not found")

    def patch(self, user_id: int):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad Request")
        if not req_json.get('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update(req_json)
        except ItemNotFound:
            abort(404, message="User not found")


@users_ns.route('/password/<int: usere_id>')
class UserPatchView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Movie not found")
    def put(self, user_id: int):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad Request")
        if not req_json.get('password_1') or not req_json.get('password_2'):
            abort(400, message="Bad Request")
        if not req_json.get('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update_pass(req_json)
        except ItemNotFound:
            abort(404, message="User not found)")


