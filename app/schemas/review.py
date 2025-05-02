from ..utils.database import ma
from ..models.reviews import Review
from marshmallow import fields


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True
        fields = ("text", "rating", "created_at", "display_name")

    rating = fields.Float()
    display_name = ma.Function(lambda obj: obj.user.display_name if obj.user.display_name else "Аноним")
