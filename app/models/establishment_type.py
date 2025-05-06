from ..utils.database import db


class EstablishmentType(db.Model):
    __tablename__ = 'establishment_types'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.Text, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<EstablishmentType {self.name}>"
