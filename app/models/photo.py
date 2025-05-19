from ..utils.database import db
import uuid


class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_type = db.Column(db.String(20), nullable=False)
    entity_id = db.Column(db.UUID(as_uuid=True), nullable=False)
    photo_path = db.Column(db.Text, nullable=False)
    is_primary = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Photo id={self.id}, entity_type={self.entity_type}, entity_id={self.entity_id}>"
