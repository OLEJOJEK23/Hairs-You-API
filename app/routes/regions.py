from flask import Blueprint, jsonify
from ..models.region import Region
from ..schemas.region import RegionSchema

regions_bp = Blueprint('regions', __name__)


@regions_bp.route('/regions', methods=['GET'])
def get_regions():
    regions = Region.query.all()
    region_schema = RegionSchema(many=True)
    result = region_schema.dump(regions)
    return jsonify(result), 200
