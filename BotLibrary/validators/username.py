# BotLibrary/validators/username.py
# Получение юзера или ID пользователя

from aiogram.types import Message

# Настройка экспорта из модуля
__all__ = ("username", "username_to_text")


def username(message: Message) -> str:
    """
    Возвращает юзернейм пользователя из сообщения, или ID, если юзернейм не указан.

    :param message: Объект сообщения из aiogram.
    :return: Строка с юзернеймом пользователя или его ID.
    :raises ValueError: Если в сообщении отсутствует информация о пользователе.
    """
    try:
        if message.from_user:
            return f"@{message.from_user.username}" if message.from_user.username else f"@{message.from_user.id}"
        raise ValueError("Информация о пользователе отсутствует в сообщении.")

    except ValueError as e:
        # Логируем ошибку с использованием Logs.error
        raise e  # Перебрасываем ошибку выше для дальнейшей обработки


def username_to_text(message: Message) -> str:
    """
    Преобразует информацию о пользователе в строку с HTML-ссылкой.

    :param message: Объект сообщения из aiogram.
    :return: Строка с HTML-кодом для ссылки на пользователя.
    :raises ValueError: Если в сообщении отсутствует информация о пользователе.
    """
    try:
        if message.from_user:
            return f'<b><a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a></b>'
        raise ValueError("Информация о пользователе отсутствует в сообщении.")

    except ValueError as e:
        # Логируем ошибку с использованием Logs.error
        raise e  # Перебрасываем ошибку выше для дальнейшей обработки
