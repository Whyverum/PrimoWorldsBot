# BotLibrary/analytics/type_chat.py
# Определение типа чата

from aiogram import types

# Настройка экспорта в модули
__all__ = ("type_chat",)

# Проверка на тип чата
async def type_chat(message: types.Message) -> str:
    """
    Преобразует информацию о чате в понятные значения.

    :param message: Объект сообщения из aiogram.
    :return: Тип чата строкой.
    """
    chat_type: str = message.chat.type
    if chat_type == "private":
        return "Личный"
    elif chat_type == "group" or chat_type == "supergroup":
        return "Группа"
    elif chat_type == "channel":
        return "Канал"
    else:
        return "Неизвестный тип чата."
