from ..utils.database import db


class Region(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Region {self.name}>"
