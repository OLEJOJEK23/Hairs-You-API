from ..models.favorite_salon import FavoriteSalon
from ..utils.database import ma
from marshmallow import fields


class FavoriteSalonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FavoriteSalon
        load_instance = True
        include_fk = True
        fields = ("salon_id", "street_address", "city_name", "name", "photo_url", "rating")

    street_address = ma.Function(lambda obj: obj.salon.street_address if obj.salon.street_address else None)
    city_name = ma.Function(lambda obj: obj.salon.city.name if obj.salon.city.name else None)
    photo_url = ma.Function(lambda obj: obj.salon.photo_url if obj.salon.photo_url else None)
    name = ma.Function(lambda obj: obj.salon.name if obj.salon.name else None)
    rating = ma.Function(lambda obj: float(obj.salon.rating) if obj.salon.rating else None)
