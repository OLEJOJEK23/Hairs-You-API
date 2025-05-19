from flask import Blueprint, request, jsonify
from ..utils.database import db
from ..models.photo import Photo
from ..schemas.photo import PhotoSchema
import cloudinary.uploader
import uuid

photos_bp = Blueprint('photos', __name__)


@photos_bp.route('/photos', methods=['POST'])
def upload_photo():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files['file']
        entity_type = request.form.get('entity_type')
        entity_id = request.form.get('entity_id')
        is_primary = request.form.get('is_primary', 'false').lower() == 'true'

        if not entity_type or not entity_id:
            return jsonify({"error": "entity_type and entity_id are required"}), 400
        if entity_type not in ['salon', 'master']:
            return jsonify({"error": "Invalid entity_type"}), 400

        # Загрузка в Cloudinary
        upload_result = cloudinary.uploader.upload(file, folder=f"{entity_type}s/{entity_id}")
        photo_path = upload_result['secure_url']

        # Сохранение в базу
        photo = Photo(
            id=uuid.uuid4(),
            entity_type=entity_type,
            entity_id=entity_id,
            photo_path=photo_path,
            is_primary=is_primary
        )
        db.session.add(photo)

        # Если новая фотография основная, снять флаг is_primary с других
        if is_primary:
            db.session.query(Photo).filter(
                Photo.entity_type == entity_type,
                Photo.entity_id == entity_id,
                Photo.id != photo.id
            ).update({"is_primary": False})

        db.session.commit()
        photo_schema = PhotoSchema()
        return jsonify(photo_schema.dump(photo)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to upload photo: {str(e)}"}), 500


@photos_bp.route('/photos', methods=['GET'])
def get_photos():
    try:
        entity_type = request.args.get('entity_type', type=str)
        entity_id = request.args.get('entity_id', type=str)

        if entity_type not in ['salon', 'master']:
            return jsonify({"error": "Invalid entity_type"}), 400

        photos = db.session.query(Photo).filter(
            Photo.entity_type == entity_type,
            Photo.entity_id == entity_id
        ).all()

        photo_schema = PhotoSchema(many=True)
        return jsonify(photo_schema.dump(photos)), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch photos: {str(e)}"}), 500


@photos_bp.route('/photos', methods=['DELETE'])
def delete_photo():
    try:
        photo_id = request.args.get('photo_id', type=str)
        photo = db.session.query(Photo).get(photo_id)
        if not photo:
            return jsonify({"error": "Photo not found"}), 404

        # Удаление из Cloudinary
        public_id = photo.photo_path.split('/')[-1].split('.')[0]
        cloudinary.uploader.destroy(f"{photo.entity_type}s/{photo.entity_id}/{public_id}")

        db.session.delete(photo)
        db.session.commit()
        return jsonify({"message": "Photo deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to delete photo: {str(e)}"}), 500
