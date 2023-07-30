import os

from peewee import Model, SqliteDatabase, PrimaryKeyField
from config import get_root_path

db = SqliteDatabase(os.path.abspath(os.path.join(get_root_path(), 'database/db.db')))


class BaseModel(Model):
    """Базовый класс"""

    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'
