# BotLibrary/validators/username.py
# Получение юзера пользователя

from aiogram.types import message

# Настройка экспорта из модуля
__all__ = ("username",)

# Функция получения юзера или id пользователя
def username(message: message.Message):
    return f"@{message.from_user.username or message.from_user.id}"
