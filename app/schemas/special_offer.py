from ..utils.database import ma
from ..models.special_offers import SpecialOffer


class SpecialOfferSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SpecialOffer
        load_instance = True
        include_fk = True
        fields = ("description", "id", "photo_url", "title", "salon_id", "address", "city")

    address = ma.Function(lambda obj: obj.salon.street_address if obj.salon.street_address else None)
    city = ma.Function(lambda obj: obj.salon.city.name if obj.salon.city.name else None)
