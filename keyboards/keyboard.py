from vk_api.keyboard import VkKeyboard
from database.database_queries import get_list_name_category, get_list_name_products

fake_catalog = ['Хлеб', 'Пирожные', 'Кексы', 'Эклеры', 'Печенье', 'Торты', 'Круассаны', ]


def main_menu():
    """Главное меню бота"""

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Наша выпечка', color='positive')
    keyboard.add_button('Адреса наших кондитерских', color='positive')
    keyboard.add_line()
    keyboard.add_button('О нас', color='positive')

    return keyboard.get_keyboard()


def chunk_list(lst, size=3):
    """Итератор отрезков списка"""

    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def creating_a_list_button_menu(list_catalog):
    """Создание списка кнопок из категорий"""

    keyboards = VkKeyboard(one_time=False)

    for item in chunk_list(list_catalog):
        for name in item:
            keyboards.add_button(name, color='positive')
        keyboards.add_line()

    keyboards.add_button('Назад', color='negative')

    return keyboards.get_keyboard()


list_categories = get_list_name_category()

button_category_menu = creating_a_list_button_menu(list_categories)
button_main_menu = main_menu()

