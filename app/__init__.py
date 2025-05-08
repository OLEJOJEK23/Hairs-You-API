from flask import Flask

from .utils.database import db, ma
from .utils.logging import setup_logging
from .utils.error_handler import register_error_handlers
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация логирования
    logger = setup_logging()

    # Инициализация расширений
    db.init_app(app)
    ma.init_app(app)

    # Создание таблиц в контексте приложения
    with app.app_context():
        db.create_all()

    # Регистрация обработчиков ошибок
    register_error_handlers(app)

    # Регистрация маршрутов
    from .routes.countries import countries_bp
    from .routes.regions import regions_bp
    from .routes.cities import cities_bp
    from .routes.salons import salons_bp
    from .routes.bookings import bookings_bp
    from .routes.services import services_bp
    from .routes.masters import masters_bp
    from .routes.short_salons import short_salons_bp
    from .routes.special_offers import special_offers_bp
    from .routes.reviews import reviews_bp
    from .routes.users import users_bp
    from .routes.establishment_types import establishment_types_bp
    app.register_blueprint(countries_bp, url_prefix='/api')
    app.register_blueprint(regions_bp, url_prefix='/api')
    app.register_blueprint(cities_bp, url_prefix='/api')
    app.register_blueprint(salons_bp, url_prefix='/api')
    app.register_blueprint(bookings_bp, url_prefix='/api')
    app.register_blueprint(services_bp, url_prefix='/api')
    app.register_blueprint(masters_bp, url_prefix='/api')
    app.register_blueprint(short_salons_bp, url_prefix='/api')
    app.register_blueprint(special_offers_bp, url_prefix='/api')
    app.register_blueprint(reviews_bp, url_prefix='/api')
    app.register_blueprint(establishment_types_bp, url_prefix='/api')
    app.register_blueprint(users_bp, url_prefix='/api')

    return app
