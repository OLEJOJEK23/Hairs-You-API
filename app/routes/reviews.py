import uuid
from werkzeug.exceptions import BadRequest
from flask import Blueprint, jsonify, request
from ..models.reviews import Review
from ..schemas.review import ReviewSchema

reviews_bp = Blueprint('reviews_bp', __name__)


@reviews_bp.route('/reviews', methods=['GET'])
def get_reviews():
    salon_id = request.args.get('salon_id', type=str)
    query = Review.query

    if salon_id:
        try:
            salon_uuid = uuid.UUID(salon_id)
            query = query.filter_by(salon_id=salon_uuid)
        except ValueError:
            raise BadRequest("Invalid salon_id: must be a valid UUID")

    reviews = query.all()
    reviews_schema = ReviewSchema(many=True)
    result = reviews_schema.dump(reviews)
    return jsonify(result), 200
