from flask import Blueprint, jsonify, request
from ..models.user import User
from ..schemas.user import UserSchema

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_users():
    # Получение query-параметров для фильтрации
    user_id = request.args.get('user_id', type=str)

    # Базовый запрос
    query = User.query

    # Фильтрация по user_id, если указан
    if user_id:
        query = query.filter_by(id=user_id)
    else:
        raise ValueError("user_id is required")

    # Получение всех городов с учетом фильтров
    users = query.all()

    # Сериализация результата
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result), 200
