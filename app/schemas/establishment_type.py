from ..models.establishment_type import EstablishmentType
from ..utils.database import ma


class EstablishmentTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EstablishmentType
        load_instance = True
        include_fk = True
