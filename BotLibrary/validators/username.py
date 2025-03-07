# BotLibrary/validators/username.py
# Получение юзера или ID пользователя

from aiogram.types import Message

# Настройка экспорта из модуля
__all__ = ("username", "username_to_text")

# Функция получения юзера или ID пользователя
def username(message: Message) -> str:
    """
    Возвращает юзернейм пользователя из сообщения, или ID, если юзернейм не указан.

    :param message: Объект сообщения из aiogram.
    :return: Строка с юзернеймом пользователя или его ID.
    """
    if message.from_user:
        return f"@{message.from_user.username}" if message.from_user.username else f"@{message.from_user.id}"
    return "@Unknown_User"  # Если from_user отсутствует


# Функция получение имени пользователя + ссылка на него
def username_to_text(message: Message) -> str:
    return f'<b><a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a></b>'
