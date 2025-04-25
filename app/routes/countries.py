from flask import Blueprint, jsonify
from loguru import logger
from ..models.country import Country
from ..schemas.country import CountrySchema
from ..utils.database import db

countries_bp = Blueprint('countries', __name__)


@countries_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    country_schema = CountrySchema(many=True)
    result = country_schema.dump(countries)
    return jsonify(result), 200
