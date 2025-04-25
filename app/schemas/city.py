from ..utils.database import ma
from ..models.city import City


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        load_instance = True
        include_fk = True
