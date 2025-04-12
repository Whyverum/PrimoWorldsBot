# BotLibrary/analytics/type_chat.py
# Определение типа чата

from aiogram.types import Message

# Настройка экспорта в модули
__all__ = ("type_chat",)

async def type_chat(message: Message) -> str:
    """
    Преобразует информацию о чате в его тип на русском языке.

    :param message: Объект сообщения из aiogram, содержащий информацию о чате.
    :return: Тип чата строкой.
    """
    chat_types: dict[str, str] = {
        "private": "Личный",
        "group": "Группа",
        "supergroup": "Группа",
        "channel": "Канал",
    }

    return chat_types.get(message.chat.type, "Неизвестный тип чата")
