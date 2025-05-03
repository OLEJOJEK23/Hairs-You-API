from loguru import logger
import sys
import os
from datetime import datetime


def setup_logging():
    # Очистка стандартных обработчиков loguru
    logger.remove()

    # Формат логов с IP-адресом
    log_format = "{time:YYYY-MM-DD HH:mm:ss} | {level}  | Client IP: {extra[client_ip]} | {message}"

    # Логирование в консоль (DEBUG и выше)
    logger.add(sys.stderr, format=log_format, level="DEBUG")

    # Создание директории для логов, если она не существует
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Логирование в файл только для ERROR и выше
    log_file = os.path.join(log_dir, f"api_{datetime.now().strftime('%Y-%m-%d')}.log")
    logger.add(log_file, format=log_format, level="ERROR", rotation="1 day", retention="7 days", compression="zip")

    return logger
