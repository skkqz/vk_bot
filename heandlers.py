from keyboards.keyboard import button_main_menu, button_category_menu


fake_db_user = {}


def get_user_first_name(user_id, v):
    """Функция возвращает имя пользователя по его id"""

    t = v.users.get(user_ids=user_id)

    return t[0]['first_name']


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


def logic(user_id, text, v):

    if not fake_db_user.get(user_id):
        fake_db_user[user_id] = 1

    user_name = get_user_first_name(user_id, v)

    if fake_db_user[user_id] == 1:
        fake_db_user[user_id] = 2
        send_message(user_id, button_main_menu, 'Главное меню', v)

    elif fake_db_user[user_id] == 2:
        fake_db_user[user_id] = 3
        send_message(user_id, button_category_menu, 'Категории', v)

    elif text == 'назад':
        fake_db_user[user_id] = 1
        send_message(user_id, button_main_menu, 'Вы вернулись назад', v)

    else:

        v.messages.send(
            user_id=user_id,
            random_id=0,
            message=f'{user_name}, извините я не знаю такой команды')
