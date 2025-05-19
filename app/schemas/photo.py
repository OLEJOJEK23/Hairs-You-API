from ..models.photo import Photo
from ..utils.database import ma


class PhotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Photo
        load_instance = True
        fields = ("id", "entity_type", "entity_id", "photo_path", "is_primary")
