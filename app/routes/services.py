from flask import Blueprint, jsonify, request
from ..models.service import Service
from ..schemas.service import ServiceSchema
from werkzeug.exceptions import BadRequest
import uuid

services_bp = Blueprint('services', __name__)


@services_bp.route('/services', methods=['GET'])
def get_services():
    # Получение query-параметров для фильтрации
    salon_id = request.args.get('salon_id', type=str)
    service_name_id = request.args.get('service_name_id', type=int)

    # Базовый запрос
    query = Service.query

    # Фильтрация по salon_id (UUID)
    if salon_id:
        try:
            salon_uuid = uuid.UUID(salon_id)
            query = query.filter_by(salon_id=salon_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    # Фильтрация по service_name_id
    if service_name_id:
        query = query.filter_by(service_name_id=service_name_id)

    # Получение всех услуг с учетом фильтров
    services = query.all()

    # Сериализация результата
    service_schema = ServiceSchema(many=True)
    result = service_schema.dump(services)
    return jsonify(result), 200
