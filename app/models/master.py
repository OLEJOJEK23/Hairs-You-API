from ..utils.database import db
import uuid

from .salon import Salon
from .experiences import Experience


class Master(db.Model):
    __tablename__ = 'masters'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    experience_id = db.Column(db.Integer, db.ForeignKey('experiences.id'), nullable=False)
    photo_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    # Связи
    salon = db.relationship(Salon, backref=db.backref('masters', lazy='dynamic'))
    experience = db.relationship(Experience, backref=db.backref('masters', lazy='dynamic'))
    photos = db.relationship(
        'Photo',
        backref='master',
        lazy='select',  # Используем select вместо dynamic
        primaryjoin="and_(Photo.entity_type == 'master',Photo.entity_id == foreign(Master.id))"
    )

    def __repr__(self):
        return f"<Master {self.id}>"
