import os
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')


def get_root_path():
    """Функция для получения пути корневого каталога"""

    return os.path.dirname(os.path.abspath(__file__))
