from flask import Blueprint, jsonify, request
from ..models.booking import Booking
from ..models.user import User
from ..models.salon import Salon
from ..models.service import Service
from ..models.master import Master
from ..schemas.booking import BookingSchema
from ..utils.database import db
from werkzeug.exceptions import BadRequest
import uuid
from datetime import datetime

bookings_bp = Blueprint('bookings', __name__)


@bookings_bp.route('/bookings', methods=['GET'])
def get_bookings():
    # Получение query-параметров для фильтрации
    salon_id = request.args.get('salon_id', type=str)
    user_id = request.args.get('user_id', type=str)
    status = request.args.get('status', type=str)

    # Базовый запрос
    query = Booking.query

    # Фильтрация по salon_id (UUID)
    if salon_id:
        try:
            salon_uuid = uuid.UUID(salon_id)
            query = query.filter_by(salon_id=salon_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    # Фильтрация по user_id
    if user_id:
        if len(user_id) > 255:
            raise BadRequest("Invalid user_id: must be a string up to 255 characters")
        query = query.filter_by(user_id=user_id)

    # Фильтрация по status
    if status:
        if status not in ['pending', 'confirmed', 'cancelled']:
            raise BadRequest("Invalid status: must be 'pending', 'confirmed', or 'cancelled'")
        query = query.filter_by(status=status)

    # Получение всех бронирований с учетом фильтров
    bookings = query.all()

    # Сериализация результата
    booking_schema = BookingSchema(many=True)
    result = booking_schema.dump(bookings)
    return jsonify(result), 200


@bookings_bp.route('/bookings', methods=['POST'])
def create_booking():
    # Получение данных из тела запроса
    data = request.get_json()

    # Проверка обязательных полей
    required_fields = ['user_id', 'salon_id', 'service_id', 'booking_time']
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")

    # Валидация UUID
    try:
        salon_id = uuid.UUID(data['salon_id'])
        service_id = uuid.UUID(data['service_id'])
        master_id = uuid.UUID(data['master_id']) if data.get('master_id') else None
    except ValueError:
        raise BadRequest("Invalid UUID format for salon_id, service_id, or master_id")

    # Валидация user_id
    user_id = data['user_id']
    if not isinstance(user_id, str) or len(user_id) > 255:
        raise BadRequest("Invalid user_id: must be a string up to 255 characters")

    # Валидация booking_time
    try:
        booking_time = datetime.fromisoformat(data['booking_time'])
    except ValueError:
        raise BadRequest("Invalid booking_time: must be in ISO format (e.g., '2025-04-26T14:30:00+00:00')")

    # Валидация status
    status = data.get('status', 'pending')
    if status not in ['pending', 'confirmed', 'cancelled']:
        raise BadRequest("Invalid status: must be 'pending', 'confirmed', or 'cancelled'")

    # Проверка существования записей
    if not User.query.get(user_id):
        raise BadRequest("User does not exist")
    if not Salon.query.get(salon_id):
        raise BadRequest("Salon does not exist")
    if not Service.query.get(service_id):
        raise BadRequest("Service does not exist")
    if master_id and not Master.query.get(master_id):
        raise BadRequest("Master does not exist")

    # Создание бронирования
    booking = Booking(
        user_id=user_id,
        salon_id=salon_id,
        service_id=service_id,
        master_id=master_id,
        booking_time=booking_time,
        status=status
    )

    # Сохранение в базе данных
    db.session.add(booking)
    db.session.commit()

    # Сериализация результата
    booking_schema = BookingSchema()
    result = booking_schema.dump(booking)
    return jsonify(result), 201
