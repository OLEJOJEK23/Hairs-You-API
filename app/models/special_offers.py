from .salon import Salon
from ..utils.database import db
import uuid


class SpecialOffer(db.Model):
    __tablename__ = 'special_offers'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    salon = db.relationship(Salon, backref=db.backref('special_offers', lazy='dynamic'))

    def __repr__(self):
        return f"<Offer {self.id}>"
