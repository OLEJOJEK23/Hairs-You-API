from flask import jsonify
from loguru import logger
from werkzeug.exceptions import HTTPException


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_generic_error(e):
        logger.error(f"Unhandled error: {str(e)}")
        response = {
            "error": "Internal Server Error",
            "message": str(e),
            "status_code": 500
        }
        return jsonify(response), 500

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        logger.error(f"HTTP error {e.code}: {e.name} - {e.description}")
        response = {
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }
        return jsonify(response), e.code

    @app.errorhandler(404)
    def handle_not_found(e):
        logger.error(f"Resource not found: {e.description}")
        response = {
            "error": "Not Found",
            "message": "The requested resource was not found on the server",
            "status_code": 404
        }
        return jsonify(response), 404
