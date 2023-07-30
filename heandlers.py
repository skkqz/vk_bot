from keyboards.keyboard import button_main_menu, button_category_menu, \
    list_categories, creating_a_list_button_menu
from database.database_queries import get_user, update_position_user, get_product, get_list_name_products

user_category_dict = {}


def send_message(id_user, id_keyboard, message_text, v):
    """Функция отправки сообщения """

    try:
        v.messages.send(
            user_id=id_user,
            random_id=0,
            keyboard=id_keyboard,
            message=message_text)
    except Exception as ex:
        print(f'Ошибка отправки сообщения у id: {id_user} ({ex})')


def logic(user_id, text, v, u):
    """Логика ответа бота на сообщения от пользователя"""

    user = get_user(user_id, v)

    if user_id not in user_category_dict:
        user_category_dict[user_id] = []

    if user.position == 1:

        send_message(user_id, button_main_menu, 'У Мамы и Папы', v)
        if text == 'наша выпечка':
            update_position_user(user_id, 2)
            send_message(user_id, button_category_menu, 'Наша выпечка', v)

        elif text == 'адреса наших кондитерских':

            v.messages.send(user_id=user_id,
                            message='г. Москва, ул. Охотничий ряд, д.20, центральный вход', random_id=0)

        elif text == 'о нас':

            v.messages.send(user_id=user_id,
                            message='Семейная кондитерская.', random_id=0)

    elif user.position == 2:

        send_message(user_id, button_category_menu, 'Наша выпечка', v)
        if text.title() in list_categories:
            update_position_user(user_id, 3)
            user_category_dict[user_id] = get_list_name_products(text.title())
            send_message(user_id, creating_a_list_button_menu(user_category_dict[user_id]), text.title(), v)
        elif text == 'назад':
            update_position_user(user_id, 0)
            send_message(user_id, button_main_menu, 'Главное меню', v)

    elif user.position == 3:
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

    elif text == 'адреса наших кондитерских':
        v.messages.send(user_id=user_id, message='г. Москва, ул. Охотничий ряд, д.20, центральный вход', random_id=0)
