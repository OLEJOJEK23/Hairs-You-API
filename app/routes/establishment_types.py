import uuid
from werkzeug.exceptions import BadRequest
from flask import Blueprint, jsonify, request
from app.models.establishment_type import EstablishmentType
from app.schemas.establishment_type import EstablishmentTypeSchema

establishment_types_bp = Blueprint('establishment_types_bp', __name__)


@establishment_types_bp.route('/salons_types', methods=['GET'])
def get_establishment_types():
    salon_id = request.args.get('salon_id', type=str)
    query = EstablishmentType.query

    if salon_id:
        try:
            salon_uuid = uuid.UUID(salon_id)
            query = query.filter_by(salon_id=salon_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    establishment_types = query.all()
    establishment_types_schema = EstablishmentTypeSchema(many=True)
    result = establishment_types_schema.dump(establishment_types)
    return jsonify(result), 200
