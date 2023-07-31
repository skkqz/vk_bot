from keyboards.keyboard import button_main_menu, button_category_menu, list_categories, create_category_menu
from database.database_queries import get_user, update_position_user, get_product, get_list_name_products

user_category_dict = {}


def send_message(user_id, keyboard_id, message_text, v):
    """Функция отправки сообщения"""

    try:
        v.messages.send(
            user_id=user_id,
            random_id=0,
            keyboard=keyboard_id,
            message=message_text
        )
    except Exception as ex:
        print(f'Ошибка отправки сообщения у id: {user_id} ({ex})')


def handle_position_1(user_id, text, v):
    """Обработка позиции 1"""

    send_message(user_id, button_main_menu, 'У Мамы и Папы', v)

    if text == 'наша выпечка':
        update_position_user(user_id, 2)
        send_message(user_id, button_category_menu, 'Наша выпечка', v)

    elif text == 'адреса наших кондитерских':
        v.messages.send(user_id=user_id, message='г. Москва, ул. Охотничий ряд, д.20, центральный вход', random_id=0)

    elif text == 'о нас':
        v.messages.send(user_id=user_id, message='Семейная кондитерская.', random_id=0)


def handle_position_2(user_id, text, v):
    """Обработка позиции 2"""

    send_message(user_id, button_category_menu, 'Наша выпечка', v)

    if text.title() in list_categories:
        update_position_user(user_id, 3)
        user_category_dict[user_id] = get_list_name_products(text.title())
        send_message(user_id, create_category_menu(user_category_dict[user_id]), text.title(), v)

    elif text == 'назад':
        update_position_user(user_id, 0)
        send_message(user_id, button_main_menu, 'Главное меню', v)


def handle_position_3(user_id, text, v, u):
    """Обработка позиции 3"""

    if text.title() in user_category_dict[user_id]:
        product = get_product(text.title())

        image = u.photo_messages(product.image)
        attachment = f"photo{image[0]['owner_id']}_{image[0]['id']}"

        template_message = f'Название: {product.name}\n' \
                           f'Описание: {product.description}\n' \
                           f'Цена: {product.price}'

        v.messages.send(user_id=user_id, message=template_message, attachment=attachment, random_id=0)

    elif text == 'назад':
        update_position_user(user_id, 0)
        send_message(user_id, button_category_menu, 'Наша выпечка', v)


def main_logic(user_id, text, v, u):
    """Основная логика ответа бота на сообщения от пользователя"""

    user = get_user(user_id, v)

    if user_id not in user_category_dict:
        user_category_dict[user_id] = []

    if user.position == 1:
        handle_position_1(user_id, text, v)

    elif user.position == 2:
        handle_position_2(user_id, text, v)

    elif user.position == 3:
        handle_position_3(user_id, text, v, u)

    elif text == 'адреса наших кондитерских':
        v.messages.send(user_id=user_id, message='г. Москва, ул. Охотничий ряд, д.20, центральный вход', random_id=0)
