from flask import jsonify, request
from loguru import logger
from werkzeug.exceptions import HTTPException


def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    return request.remote_addr


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_generic_error(e):
        client_ip = get_client_ip()
        logger_with_ip = logger.bind(client_ip=client_ip)
        logger_with_ip.error(f"Unhandled error: {str(e)}")
        response = {
            "error": "Internal Server Error",
            "message": str(e),
            "status_code": 500
        }
        return jsonify(response), 500

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        client_ip = get_client_ip()
        logger_with_ip = logger.bind(client_ip=client_ip)
        logger_with_ip.error(f"HTTP error {e.code}: {e.name} - {e.description}")
        response = {
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }
        return jsonify(response), e.code

    @app.errorhandler(404)
    def handle_not_found(e):
        client_ip = get_client_ip()
        logger_with_ip = logger.bind(client_ip=client_ip)
        request_info = {
            'method': request.method,
            'url': request.url,
            'query_params': request.args.to_dict(),
            'body': request.get_json(silent=True) or request.form.to_dict() or None
        }
        logger_with_ip.error(f"Resource not found: {e.name} | Request: {request_info}")
        response = {
            "error": "Not Found",
            "message": "The requested resource was not found on the server",
            "status_code": 404
        }
        return jsonify(response), 404
