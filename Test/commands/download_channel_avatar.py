# BotCode/routers/downloads/download_channel_avatar.py
# Закачка аватарок канала (в разработке + сделать логирование!!!)

import requests
from aiogram import Router
from aiogram.types import Message
from BotLibrary import *

# Создание роутера и настройка экспорта
__all__ = ("router", "download_channel_avatar",)
router = Router(name="avatar_channel_router")
type_messages = "AvatarChannel"


# Функция для скачивания аватарки канала
@router.message(lambda message: message.chat.type == 'channel')
async def download_channel_avatar(message: Message):
    try:
        # Логирование для получения сообщения из канала
        logger.bind(custom_variable=type_messages, user_var=f"{message.chat.id}").info(f"Получено сообщение из канала ID {message.chat.id}: {message.text}")

        # Получаем информацию о чате канала
        chat_info = await bot.get_chat(message.chat.id)  # message.chat.id для получения ID канала

        # Логирование полученной информации
        logger.bind(custom_variable=type_messages, user_var=f"{chat_info.id}").info(f"Информация о канале: {chat_info.title}")

        # Проверка наличия аватара
        if not chat_info.photo:
            text_error = f"Канал с ID {message.chat.id} не имеет аватара."
            logger.error(text_error)
            return text_error

        # Получаем file_id для фото (используем big_file_id для лучшего качества)
        file_info = await bot.get_file(chat_info.photo.big_file_id)

        # Строим URL для скачивания файла
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

        # Формируем имя и путь для сохранения фото
        save_dir = f"{ImportantPath.channel_avatar}/{message.chat.id}"
        os.makedirs(save_dir, exist_ok=True)
        file_name = file_info.file_path.split("/")[-1]  # Имя файла (например, "abc.jpg")
        save_path = os.path.join(save_dir, file_name)

        # Скачиваем аватар
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            text = f"Фото аватара канала с ID {message.chat.id} успешно скачано и сохранено как {save_path}"
            logger.info(text)
            return text

        else:
            text_error = f"Не удалось скачать аватар канала с ID {message.chat.id}. Статус: {response.status_code}"
            logger.bind(custom_variable=type_messages, user_var=f"{message.chat.id}").error(text_error)
            return text_error

    except Exception as e:
        text_error = f"Ошибка при скачивании фото аватара канала с ID {message.chat.id}: {e}"
        logger.bind(custom_variable=type_messages, user_var=f"{message.chat.id}").error(text_error)
        return text_error
