from marshmallow import fields, Schema


class MovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre_id = fields.Int()
    director_id = fields.Int()
