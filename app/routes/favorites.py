from flask import Blueprint, request, jsonify
from ..utils.database import db
from ..models.favorite_masters import FavoriteMaster
from ..models.favorite_salon import FavoriteSalon
from ..schemas.favorites import FavoritesSchema

favorites_bp = Blueprint('favorites_bp', __name__)


@favorites_bp.route('/favorites', methods=['GET'])
def get_favorites():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    # Получение избранных мастеров
    favorite_masters = (
        db.session.query(FavoriteMaster)
        .filter(FavoriteMaster.user_id == user_id)
        .all()
    )

    # Получение избранных салонов
    favorite_salons = (
        db.session.query(FavoriteSalon)
        .filter(FavoriteSalon.user_id == user_id)
        .all()
    )

    # Сериализация
    favorites_data = {
        "favorite_masters": favorite_masters,
        "favorite_salons": favorite_salons
    }
    favorites_schema = FavoritesSchema()
    result = favorites_schema.dump(favorites_data)
    return jsonify(result), 200
