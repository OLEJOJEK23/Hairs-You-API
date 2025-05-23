from .city import City
from .establishment_type import EstablishmentType
from .photo import Photo
from ..utils.database import db
import uuid


class Salon(db.Model):
    __tablename__ = 'salons'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    place_id = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    street_address = db.Column(db.Text, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    establishment_type_id = db.Column(db.Integer, db.ForeignKey('establishment_types.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Numeric(3, 1), default=0.0, nullable=False)
    photo_url = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False, )
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    city = db.relationship(City, backref='salons')
    establishment_type = db.relationship(EstablishmentType, backref='salons')
    photos = db.relationship(
        'Photo',
        backref='salon',
        lazy='select',
        primaryjoin="and_(Photo.entity_type == 'salon',Photo.entity_id == foreign(Salon.id))")

    def __repr__(self):
        return f"<Salon {self.name}>"
