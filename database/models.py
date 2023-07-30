from peewee import IntegerField, CharField, ForeignKeyField
from database.base_model import BaseModel, db


class User(BaseModel):
    """Класс пользователя"""

    user_id = IntegerField(null=True)
    first_name = CharField(max_length=100)
    position = IntegerField(default=1, null=True)

    class Meta:
        db_table = 'users'


class Category(BaseModel):
    """Класс категории товара"""

    name = CharField(max_length=100, null=True)

    class Meta:
        db_table = 'categories'


class Product(BaseModel):
    """Класс товара"""

    name = CharField(max_length=100, null=True)
    description = CharField(max_length=500)
    price = IntegerField()
    image = CharField()
    category = ForeignKeyField(Category, backref='category', null=True)

    class Meta:
        db_table = 'products'


def create_a_database():
    """Создание таблиц базы данных"""
    with db:
        db.create_tables([User, Product, Category])
