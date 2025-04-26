from flask import Blueprint, jsonify, request
from ..models.salon import Salon
from ..schemas.salon import SalonSchema

salons_bp = Blueprint('salons', __name__)


@salons_bp.route('/salons', methods=['GET'])
def get_salons():
    # Получение query-параметров для фильтрации
    city_id = request.args.get('city_id', type=int)
    address = request.args.get('address', type=str)

    # Базовый запрос
    query = Salon.query

    # Фильтрация по city_id, если указан
    if city_id:
        query = query.filter_by(city_id=city_id)

    # Фильтрация по street_address (частичное совпадение, без учета регистра)
    if address:
        query = query.filter(Salon.street_address.ilike(f'%{address}%'))

    # Получение всех салонов с учетом фильтров
    salons = query.all()

    # Сериализация результата
    salon_schema = SalonSchema(many=True)
    result = salon_schema.dump(salons)
    return jsonify(result), 200
