from ..utils.database import ma
from ..models.service import Service
from marshmallow import fields


class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        load_instance = True
        include_fk = True
        fields = ("service_name", "duration", "price", "service_id", "id")

    service_name = ma.Function(lambda obj: obj.service_name.name if obj.service_name else None)
    duration = fields.Integer()
    price = fields.Float()
