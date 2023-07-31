from vk_api.keyboard import VkKeyboard
from database.database_queries import get_list_name_category


def create_main_menu():
    """Создание главного меню бота"""

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


def create_category_menu(list_catalog):
    """Создание меню категорий"""

    keyboard = VkKeyboard(one_time=False)

    for item in chunk_list(list_catalog):
        for name in item:
            keyboard.add_button(name, color='positive')
        keyboard.add_line()

    keyboard.add_button('Назад', color='negative')

    return keyboard.get_keyboard()


list_categories = get_list_name_category()
button_main_menu = create_main_menu()
button_category_menu = create_category_menu(list_categories)
