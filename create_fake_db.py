import os
import requests
from database.models import Category, Product, create_a_database


fake_catalog = ['Хлеб', 'Пирожные', 'Кексы', 'Эклеры', 'Печенье', 'Торты', 'Круассаны']

image_product = {
    'Хлеб': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCMVznuubpcJ-_42Uxt9KuNsuHMU6Vj-nv7A&usqp=CAU',
    'Пирожные': 'https://vvkus74.ru/upload/iblock/7ae/ekvcebe6up9coaubb82zqkxl244yy06q/%D0%9C%D0%B5%D0%B4%D0%BE%D0%B2%D0%B8%D1%87%D0%BE%D0%BA%20%D0%9F%D0%B8%D1%80%D0%BE%D0%B6%D0%BD%D1%8B%D0%B5.jpg',
    'Кексы': 'https://xn--b1aqjenlka.xn--p1ai/img/recepty/721/big.jpg',
    'Эклеры': 'https://www.gastronom.ru/binfiles/images/20201223/b07b0915.jpg',
    'Печенье': 'https://cdn.lifehacker.ru/wp-content/uploads/2021/04/shutterstock_345966080_1618569509-1280x640.jpeg',
    'Торты': 'https://british-bakery.ru/upload/resize_cache/iblock/094/400_400_1/0947f48252b0f99a4881981e9f1923fc.jpg',
    'Круассаны': 'https://cdn.lifehacker.ru/wp-content/uploads/2021/04/shutterstock_642373528_1619556387-scaled-e1619556419295-1280x640.jpg'
}


def download_image(url, category, index):
    """Загрузка изображения и возврат пути до него"""

    path_dir_image = os.path.abspath(os.path.join('image'))
    os.makedirs(path_dir_image, exist_ok=True)

    r = requests.get(url)
    path_image = fr'{path_dir_image}\{category}_{index}.jpg'

    with open(path_image, 'wb') as f:
        f.write(r.content)

    return path_image


def create_fake_database():
    """Функция для создания тестовой базы данных"""

    create_a_database()

    for num, category in enumerate(fake_catalog):

        category_obj = Category.create(name=category)

        image_url = image_product.get(category)
        if image_url:
            image_path = download_image(image_url, category, num)
            for i in range(5):
                Product.create(name=f'{category} - {i}',
                               description=f'Тестовое описание {i}', price=100, category=category_obj, image=image_path)

    print('База данных создана')


create_fake_database()
