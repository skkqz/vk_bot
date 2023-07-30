import os
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')

current_path = os.path.abspath(__file__)
config_folder = os.path.dirname(current_path)


def get_root_path():
    """Функция для получения пути корневого каталога"""
    return config_folder
