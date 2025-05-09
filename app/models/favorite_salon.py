from .salon import Salon
from ..utils.database import db
import uuid
from .user import User


class FavoriteSalon(db.Model):
    __tablename__ = 'favorite_salons'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'), nullable=False)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    # Связи
    salon = db.relationship(Salon, backref=db.backref('favorite_salons', lazy='dynamic'))
    user = db.relationship(User, backref=db.backref('favorite_salons', lazy='dynamic'))

    def __repr__(self):
        return f"<FavoriteSalon user_id={self.user_id}, master_id={self.salon_id}>"
