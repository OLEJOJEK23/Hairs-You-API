from ..utils.database import db
import uuid


class Master(db.Model):
    __tablename__ = 'masters'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    salon_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('salons.id'), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    experience_id = db.Column(db.Integer, db.ForeignKey('experiences.id'), nullable=False)
    photo_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Master {self.id}>"
