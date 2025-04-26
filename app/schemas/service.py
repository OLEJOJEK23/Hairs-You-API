from ..utils.database import ma
from ..models.service import Service


class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        load_instance = True
        include_fk = True

    service_name = ma.Function(lambda obj: obj.service_name.name if obj.service_name else None)
