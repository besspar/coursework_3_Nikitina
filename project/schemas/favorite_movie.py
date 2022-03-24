from marshmallow import fields, Schema


class FavoriteMovieSchema(Schema):
    user_id = fields.Int(required=True)
    movie_id = fields.Int(required=True)