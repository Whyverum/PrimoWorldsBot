# BotCode/keyboards/inline_kb/start_inline_kb.py
# Создания инлайн-клавиатуры на команду: /start

from aiogram.types import InlineKeyboardMarkup
from BotLibrary import ikb

# Создание роутера и настройка экспорта
__all__ = ("get_start_kb",)


# Функция создания клавиатуры на команду: /actor
def get_start_kb() -> InlineKeyboardMarkup:
    # Добавляем кнопки, группируя их по строкам
    ikb.button(text="Посмотреть инфо-канал", url="https://t.me/laveilinfo")
    ikb.button(text="Отправить анкету", url="https://t.me/laveilinfo")
    ikb.button(text="Предложить союз", url="https://t.me/laveilinfo")

    ikb.adjust(1)
    return ikb.as_markup()