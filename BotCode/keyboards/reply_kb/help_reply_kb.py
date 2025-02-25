# BotCode/keyboards/reply_kb/help_reply_kb.py
# Создание reply-клавиатуры на команду: /start с использованием всех возможностей

from aiogram.types import ReplyKeyboardMarkup
from BotLibrary import BaseReplyKeyboard

# Настройка экспорта в модули
__all__ = ("get_help_kb",)

# Функция создания клавиатуры
def get_help_kb(row_width: int = 1, resize_kb: bool = True, one_time_kb: bool = True) -> ReplyKeyboardMarkup:
    buttons = [
        ["Я Новичок!"],  # Простая текстовая кнопка
        [("Укажи местоположение", "location")],  # Запрос геолокации
        [("Поделись контактом", "contact")],  # Запрос контакта
        [("Выбери друзей", "users", {"request_id": 1, "max_quantity": 2})],  # Запрос списка пользователей
        [("Выбери чат", "chat", {"request_id": 2, "chat_is_channel": False})],  # Запрос чата
        [("Создай опрос", "poll")],  # Запрос создания опроса
        [("Создай квиз", "quiz")],  # Запрос создания квиза
        [("Открыть руководство", "web_app", {"url": "https://example.com/guide"})],  # Запуск веб-приложения
        [("Поделись пользователем", "user", {"request_id": 3, "user_is_premium": True})],  # Запрос конкретного пользователя
    ]
    return BaseReplyKeyboard(
        buttons,
        resize_keyboard=resize_kb,
        one_time_keyboard=one_time_kb,
        row_width=row_width  # Передаем row_width в класс
    ).get_keyboard()
