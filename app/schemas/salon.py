from ..utils.database import ma
from ..models.salon import Salon
from marshmallow import fields


class SalonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salon
        load_instance = True
        include_fk = True
        fields = (
            "name", "rating", "created_at", "description", "photo_url", "city_name", "street_address", "start_time",
            "end_time")

    rating = fields.Float()
    city_name = ma.Function(lambda obj: obj.city.name if obj.city.name else None)
