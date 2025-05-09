from ..models.favorite_masters import FavoriteMaster
from ..utils.database import ma


class FavoriteMasterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FavoriteMaster
        load_instance = True
        include_fk = True
        fields = ("master_id", "name", "description", "experience", "photo_url")

    name = ma.Function(lambda obj: obj.master.full_name if obj.master.full_name else None)
    description = ma.Function(lambda obj: obj.master.description if obj.master.description else None)
    photo_url = ma.Function(lambda obj: obj.master.photo_url if obj.master.photo_url else None)
    experience = ma.Function(lambda obj: obj.master.experience.name if obj.master.experience.name else None)
