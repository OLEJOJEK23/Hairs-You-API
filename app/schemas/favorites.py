from marshmallow import Schema, fields
from .favorite_master import FavoriteMasterSchema
from .favorite_salon import FavoriteSalonSchema


class FavoritesSchema(Schema):
    favorite_masters = fields.List(fields.Nested(FavoriteMasterSchema))
    favorite_salons = fields.List(fields.Nested(FavoriteSalonSchema))
