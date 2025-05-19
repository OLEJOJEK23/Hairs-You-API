import cloudinary

from dotenv import load_dotenv
import os


def init_cloudinary():
    load_dotenv()

    # Получаем переменные окружения
    cloud_name = os.getenv('CLOUD_NAME')
    api_key = os.getenv('CLOUD_API_KEY')
    api_secret = os.getenv('CLOUD_API_SECRET')

    # Проверяем, что все переменные установлены
    if not all([cloud_name, api_key, api_secret]):
        raise ValueError(
            "Missing Cloudinary configuration: CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, or CLOUDINARY_API_SECRET not set")

    # Настраиваем Cloudinary
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret,
        secure=True
    )
