from flask import Blueprint, jsonify, request
from ..models.city import City
from ..schemas.city import CitySchema
from ..utils.database import db

cities_bp = Blueprint('cities', __name__)


@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    # Получение query-параметров для фильтрации
    country_id = request.args.get('country_id', type=int)
    region_id = request.args.get('region_id', type=int)

    # Базовый запрос
    query = City.query

    # Фильтрация по country_id, если указан
    if country_id:
        query = query.filter_by(country_id=country_id)

    # Фильтрация по region_id, если указан
    if region_id:
        query = query.filter_by(region_id=region_id)

    # Получение всех городов с учетом фильтров
    cities = query.all()

    # Сериализация результата
    city_schema = CitySchema(many=True)
    result = city_schema.dump(cities)
    return jsonify(result), 200
