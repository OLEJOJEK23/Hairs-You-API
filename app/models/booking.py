from ..utils.database import db
import uuid

# Явный импорт связанных моделей
from .user import User
from .salon import Salon
from .service import Service
from .master import Master


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'), nullable=False)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    service_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('services.id'), nullable=False)
    master_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('masters.id'))
    booking_time = db.Column(db.DateTime(timezone=True), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    # Связи без lazy='dynamic' для многие-к-одному
    user = db.relationship(User, backref=db.backref('bookings', lazy='dynamic'))
    salon = db.relationship(Salon, backref=db.backref('bookings', lazy='dynamic'))
    service = db.relationship(Service, backref=db.backref('bookings', lazy='dynamic'))
    master = db.relationship(Master, backref=db.backref('bookings', lazy='dynamic'))

    def __repr__(self):
        return f"<Booking {self.id}>"
