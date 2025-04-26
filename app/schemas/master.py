from ..utils.database import ma
from ..models.master import Master


class MasterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Master
        load_instance = True
        include_fk = True

    experience = ma.Function(lambda obj: obj.experience.name if obj.experience else None)
