import uuid

from ..utils.database import db
from .user import User


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'), nullable=False)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    rating = db.Column(db.Numeric(3, 1), nullable=False)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    user = db.relationship(User, backref=db.backref('reviews', lazy='dynamic'))

    def __repr__(self):
        return f"<Review {self.id}>"
