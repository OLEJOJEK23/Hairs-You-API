from ..utils.database import ma
from ..models.country import Country


class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        load_instance = True
        include_fk = True
