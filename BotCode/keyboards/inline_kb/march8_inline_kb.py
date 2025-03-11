# BotCode/keyboards/inline_kb/8march_inline_kb.py
# Создание инлайн-клавиатуры на команду: /march8

from BotLibrary import BaseInlineKeyboard

# Настройка экспорта в модули
__all__ = ("get_march8_inline_kb", "get_return_march8_inline_kb")

# Функция создания клавиатуры
def get_march8_inline_kb(row_width : int = 2):
    buttons = [
        ("🍓Финаки", None, "march8_finaki"),
        ("🍬Финик", None, "march8_finik"),
        ("💋Поля", None, "march8_polina"),
        ("😈Катазик", None, "march8_kataz"),
        ("🪭Слешик", None, "march8_sleshik"),
    ]
    return BaseInlineKeyboard(buttons, row_width=row_width).get_keyboard()


# Функция возвратной клавиатуры
def get_return_march8_inline_kb(row_width : int = 1):
    buttons = [
        ("🥰Назад", None, "march8"),
    ]
    return BaseInlineKeyboard(buttons, row_width=row_width).get_keyboard()