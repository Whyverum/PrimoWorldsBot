# BotLibrary/analytics/type_chat.py
# Определение типа чата

from aiogram import types

# Настройка экспорта в модули
__all__ = ("type_chat",)

# Проверка на тип чата
async def type_chat(message: types.Message):
    chat_type = message.chat.type
    if chat_type == "private":
        return "Личный"
    elif chat_type == "group" or chat_type == "supergroup":
        return "Группа"
    elif chat_type == "channel":
        return "Канал"
    else:
        return "Неизвестный тип чата."
