from .master import Master
from ..utils.database import db
import uuid
from .user import User


class FavoriteMaster(db.Model):
    __tablename__ = 'favorite_masters'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'), nullable=False)
    master_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('masters.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    # Связи
    master = db.relationship(Master, backref=db.backref('favorite_masters', lazy='dynamic'))
    user = db.relationship(User, backref=db.backref('favorite_masters', lazy='dynamic'))

    def __repr__(self):
        return f"<FavoriteMaster user_id={self.user_id}, master_id={self.master_id}>"
