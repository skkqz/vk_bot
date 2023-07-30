import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_TOKEN
from database.models import create_a_database


create_a_database()


def main():

    from heandlers import logic

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
                    logic(even.user_id, text, vk, upload)

        except Exception as ex:
            print(f'Что то пошло не так: {ex}')


if __name__ == '__main__':

    main()
