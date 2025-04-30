from ..utils.database import ma
from ..models.salon import Salon


class ShortSalonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salon
        load_instance = True
        fields = ("name", "street_address", "description", "photo_url", "id", "rating")
