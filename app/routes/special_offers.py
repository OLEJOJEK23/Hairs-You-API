from flask import Blueprint, jsonify
from ..models.special_offers import SpecialOffer
from ..schemas.special_offer import SpecialOfferSchema

special_offers_bp = Blueprint('special_offers', __name__)


@special_offers_bp.route('/special_offers', methods=['GET'])
def get_special_offers():
    query = SpecialOffer.query
    offers = query.all()
    salon_schema = SpecialOfferSchema(many=True)
    result = salon_schema.dump(offers)
    return jsonify(result), 200
