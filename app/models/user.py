from ..utils.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(255), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    display_name = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    photo_url = db.Column(db.Text)
    rating = db.Column(db.Numeric(3, 1), default=5.0, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.id}>"
