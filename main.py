import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from keyboards.keyboard import button_category_menu, button_main_menu
from config import VK_TOKEN

from heandlers import logic


# def get_user_first_name(user_id, v):
#
#         t = v.users.get(user_ids=user_id)
#
#         return t[0]['first_name']


# def send_message(id_user, id_keyboard, message_text):
#     try:
#         vk.messages.send(
#             user_id=id_user,
#             random_id=0,
#             keyboard=id_keyboard,
#             message=message_text)
#     except:
#         print("Ошибка отправки сообщения у id" + id_user)


if __name__ == '__main__':

    print('Бот включен')

    while True:

        vk_session = vk_api.VkApi(token=VK_TOKEN)
        vk = vk_session.get_api()
        upload = VkUpload(vk_session)
        longpoll = VkLongPoll(vk_session)

        try:
            for even in longpoll.listen():

                if even.type == VkEventType.MESSAGE_NEW and even.to_me:

                    text = even.text.lower()
                    logic(even.user_id, text, vk)

                    # user_name = get_user_first_name(user_id=even.user_id, v=vk)
                    # text = even.text.lower()
                    # if text == 'начать':
                    #     send_message(even.user_id, button_main_menu, f'Здравствуйте {user_name}!')
                    # if text == 'наша выпечка':
                    #     send_message(even.user_id, button_category_menu, 'Выберите интересующий вас раздел')
        except Exception as ex:
            print(f'Что то пошло не так: {ex}')
