from ..utils.database import ma
from ..models.salon import Salon


class SalonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salon
        load_instance = True
        include_fk = True
