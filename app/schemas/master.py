from ..models.favorite_masters import FavoriteMaster
from ..utils.database import ma, db
from ..models.master import Master


class MasterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Master
        load_instance = True
        include_fk = True
        fields = ("id", "full_name", "salon_id", "description", "experience", "is_favorite", "photo_url", "created_at")

    experience = ma.Function(lambda obj: obj.experience.name if obj.experience else None)
    is_favorite = ma.Method("get_is_favorite")

    def get_is_favorite(self, obj):
        user_id = self.context.get('user_id')
        if not user_id:
            return False
        return db.session.query(
            FavoriteMaster.query.filter_by(user_id=user_id, master_id=obj.id).exists()
        ).scalar()
