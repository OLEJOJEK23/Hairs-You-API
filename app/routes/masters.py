from flask import Blueprint, jsonify, request
from ..models.master import Master
from ..schemas.master import MasterSchema
from werkzeug.exceptions import BadRequest
import uuid

masters_bp = Blueprint('masters', __name__)


@masters_bp.route('/masters', methods=['GET'])
def get_masters():
    # Получение query-параметров для фильтрации
    salon_id = request.args.get('salon_id', type=str)
    experience_id = request.args.get('experience_id', type=int)

    # Базовый запрос
    query = Master.query

    # Фильтрация по salon_id (UUID)
    if salon_id:
        try:
            salon_uuid = uuid.UUID(salon_id)
            query = query.filter_by(salon_id=salon_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    # Фильтрация по experience_id
    if experience_id:
        query = query.filter_by(experience_id=experience_id)

    # Получение всех мастеров с учетом фильтров
    masters = query.all()

    # Сериализация результата
    master_schema = MasterSchema(many=True)
    result = master_schema.dump(masters)
    return jsonify(result), 200
