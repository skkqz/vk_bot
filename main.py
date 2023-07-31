import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_TOKEN
from database.models import create_a_database


def initialize_vk_session():
    """Инкапсулирует создание объектов """

    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    longpoll = VkLongPoll(vk_session)

    return vk, upload, longpoll


def main():

    create_a_database()
    from handlers import main_logic

    print('Бот включен')

    vk, upload, longpoll = initialize_vk_session()

    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text.lower()
                main_logic(event.user_id, text, vk, upload)

    except Exception as ex:
        print(f'Что-то пошло не так: {ex}')


if __name__ == '__main__':
    main()
