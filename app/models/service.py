from ..utils.database import db
import uuid

from .salon import Salon
from .service_names import ServiceName


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    service_name_id = db.Column(db.Integer, db.ForeignKey('service_names.id'), nullable=False)
    price = db.Column(db.Numeric(10, 2))
    duration = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    # Связи
    salon = db.relationship(Salon, backref=db.backref('services', lazy='dynamic'))
    service_name = db.relationship(ServiceName, backref=db.backref('services', lazy='dynamic'))

    def __repr__(self):
        return f"<Service {self.id}>"
