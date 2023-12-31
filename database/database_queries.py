from database.models import User, Category, Product
from database.base_model import db


def get_user_first_name(user_id, vk):
    """Функция возвращает имя пользователя по его id"""

    user_info = vk.users.get(user_ids=user_id)
    user_first_name = user_info[0]['first_name']

    return user_first_name


def get_list_name_category():
    """Получения списка имён категорий"""

    categories = Category.select()
    list_categories_name = [category.name for category in categories]

    return list_categories_name


def get_list_name_products(category_name):
    """Получения списка имён продукта"""

    products = Product.select().join(Category).where(Category.name == category_name)
    product_names = [product.name for product in products]

    return product_names


def get_product(product_name):
    """Функция для получения продукта"""

    product = Product.get(Product.name == product_name)

    return product


def get_user(user_id, vk):
    """Функция для получения пользователя из базы данных. Если его нет, то создаёт пользователя в бд"""

    try:
        user = User.select().where(User.user_id == user_id).get()
    except User.DoesNotExist:
        user_first_name = get_user_first_name(user_id=user_id, vk=vk)
        user = User.create(user_id=user_id, first_name=user_first_name)
        print('Пользователь создан')
    return user


def update_position_user(user_id, new_position):
    """Функция обновления позиции пользователя"""

    with db:
        user = User.get(User.user_id == user_id)
        if new_position == 0:
            user.position -= 1
        else:
            user.position = new_position
        user.save()
