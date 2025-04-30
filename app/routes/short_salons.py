from flask import Blueprint, jsonify, request
from ..models.salon import Salon
from ..schemas.short_Salons import ShortSalonSchema

short_salons_bp = Blueprint('short_salons', __name__)


@short_salons_bp.route('/short_salons', methods=['GET'])
def get_short_salons():
    city_id = request.args.get('city_id', type=int)
    sort_by = request.args.get('sort_by', type=str)
    query = Salon.query

    if city_id:
        query = query.filter_by(city_id=city_id)

    if sort_by == 'rating':
        query = query.order_by(Salon.rating.desc())

    salons = query.all()
    salon_schema = ShortSalonSchema(many=True)
    result = salon_schema.dump(salons)
    return jsonify(result), 200
