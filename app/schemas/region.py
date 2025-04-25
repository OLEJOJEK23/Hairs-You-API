from ..utils.database import ma
from ..models.region import Region


class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region
        load_instance = True
        include_fk = True
