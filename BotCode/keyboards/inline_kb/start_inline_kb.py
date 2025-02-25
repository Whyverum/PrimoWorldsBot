# BotCode/keyboards/inline_kb/start_inline_kb.py
# Создание инлайн-клавиатуры на команду: /start

from BotLibrary import BaseInlineKeyboard

# Настройка экспорта в модули
__all__ = ("get_start_kb",)

# Функция создания клавиатуры
def get_start_kb(row_width : int = 1):
    buttons = [
        ("Я Новичок!", "https://t.me/+3DOBTGhBIEc4ZThi", "novice_cbd"),
        ("Где я?", None, "where_i_am_cbd"),
        ("Мне уже известен этот феномен..", None, "menu"),
    ]
    return BaseInlineKeyboard(buttons, row_width=row_width).get_keyboard()
