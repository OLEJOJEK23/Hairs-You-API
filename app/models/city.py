from ..utils.database import db


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    # Опционально: связи для удобного доступа к связанным данным
    region = db.relationship('Region', backref='cities')
    country = db.relationship('Country', backref='cities')

    def __repr__(self):
        return f"<City {self.name}>"
