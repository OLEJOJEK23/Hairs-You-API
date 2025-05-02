from ..utils.database import ma
from ..models.salon import Salon
from marshmallow import fields


class ShortSalonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salon
        load_instance = True
        fields = ("name", "street_address", "description", "photo_url", "id", "rating", "city_name")

    rating = fields.Float()
    city_name = ma.Function(lambda obj: obj.city.name if obj.city.name else None)
