from flask import Blueprint, jsonify, request
from ..models.master import Master
from ..schemas.master import MasterSchema
from werkzeug.exceptions import BadRequest, NotFound
import uuid
from ..utils.database import db

masters_bp = Blueprint('masters', __name__)


@masters_bp.route('/masters', methods=['GET'])
def get_masters():
    # Получение query-параметров для фильтрации
    salon_id = request.args.get('salon_id', type=str)
    experience_id = request.args.get('experience_id', type=int)
    user_id = request.args.get('user_id', type=str)
    master_id = request.args.get('master_id', type=str)

    # Базовый запрос
    query = Master.query

    # Фильтрация по salon_id (UUID)
    if salon_id:
        try:
            salon_uuid = uuid.UUID(salon_id)
            query = query.filter_by(salon_id=salon_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    if master_id:
        try:
            master_uuid = uuid.UUID(master_id)
            query = query.filter_by(id=master_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    # Фильтрация по experience_id
    if experience_id:
        query = query.filter_by(experience_id=experience_id)

    # Получение всех мастеров с учетом фильтров
    masters = query.all()

    # Сериализация результата
    if user_id:
        master_schema = MasterSchema(many=True, context={'user_id': user_id})
    else:
        master_schema = MasterSchema(many=True)
    result = master_schema.dump(masters)
    return jsonify(result), 200


@masters_bp.route('/masters', methods=['POST'])
def create_master():
    """
    Создает нового мастера на основе данных из запроса.
    """
    try:
        # Получение данных из запроса
        data = request.get_json()
        if not data:
            raise BadRequest("No data provided")

        # Валидация данных
        full_name = data.get("full_name")
        salon_id = data.get("salon_id")
        experience_id = data.get("experience_id")
        description = data.get("description", "")
        photo_url = data.get("photo_url", "")

        if not full_name or not salon_id or not experience_id:
            raise BadRequest("Fields 'full_name', 'salon_id', and 'experience_id' are required")

        # Проверка валидности salon_id
        try:
            salon_uuid = uuid.UUID(salon_id)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

        # Создание нового мастера
        new_master = Master(
            full_name=full_name,
            salon_id=salon_uuid,
            experience_id=experience_id,
            description=description,
            photo_url=photo_url
        )

        # Сохранение в базе данных
        db.session.add(new_master)
        db.session.commit()

        # Сериализация результата
        master_schema = MasterSchema()
        result = master_schema.dump(new_master)

        return jsonify(result), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@masters_bp.route('/masters/<id>', methods=['PUT'])
def update_master(id):
    """
    Обновление информации о мастере по ID.
    """
    # Проверка на валидный UUID
    try:
        master_id = uuid.UUID(id)
    except ValueError:
        raise NotFound("Invalid ID: must be a valid UUID")

    # Поиск мастера в базе данных
    master = Master.query.get(master_id)
    if not master:
        raise NotFound("Master not found")

    # Получение данных из запроса
    data = request.get_json()
    if not data:
        raise BadRequest("No data provided")

    # Обновление полей мастера
    master.full_name = data.get("full_name", master.full_name)
    master.description = data.get("description", master.description)
    master.photo_url = data.get("photo_url", master.photo_url)
    experience_id = data.get("experience_id")
    if experience_id:
        master.experience_id = experience_id
    salon_id = data.get("salon_id")
    if salon_id:
        try:
            master.salon_id = uuid.UUID(salon_id)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    # Сохранение изменений в базе данных
    db.session.commit()

    # Сериализация результата
    master_schema = MasterSchema()
    result = master_schema.dump(master)

    return jsonify(result), 200


@masters_bp.route('/masters/<id>', methods=['DELETE'])
def delete_master(id):
    """
    Удаление мастера по ID.
    """
    # Проверка на валидный UUID
    try:
        master_id = uuid.UUID(id)
    except ValueError:
        raise NotFound("Invalid ID: must be a valid UUID")

    # Поиск мастера в базе данных
    master = Master.query.get(master_id)
    if not master:
        raise NotFound("Master not found")

    # Удаление мастера из базы данных
    db.session.delete(master)
    db.session.commit()

    return jsonify({"message": "Master deleted successfully"}), 200
